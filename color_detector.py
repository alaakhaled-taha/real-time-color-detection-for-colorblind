
import cv2
import numpy as np
from perona_malik import automated_perona_malik  
from color_range import ColorRange 

class ColorDetector:
    def __init__(self, color_ranges, show_text=True, label_type="rectangle"):
        self.kernel = np.ones((5, 5), "uint8")
        self.color_ranges = color_ranges
        self.show_text = show_text
        self.label_type = label_type 

    def apply_mask(self, hsv_frame, color_range):
        """Apply the color mask to the HSV image."""
        mask = cv2.inRange(hsv_frame, color_range.lower_bound, color_range.upper_bound)
        return cv2.dilate(mask, self.kernel)

    def contour_objects(self, frame, mask, color_range):
        """Detect and label contours based on the color mask."""
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 300:  # Filter out small contours
                overlay = frame.copy()
                cv2.drawContours(overlay, [contour], -1, color_range.label_color, thickness=cv2.FILLED)
                frame = cv2.addWeighted(overlay, 0.4, frame, 0.6, 0)
                cv2.drawContours(frame, [contour], -1, color_range.label_color, 2)
                x, y, _, _ = cv2.boundingRect(contour)
                if self.show_text:
                    cv2.putText(
                        frame, color_range.name, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2
                    )
        return frame
    
    def label_objects(self, frame, mask, color_range):
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 300:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color_range.label_color, 2)
                if self.show_text:
                    cv2.putText(
                        frame, color_range.name, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color_range.label_color, 2
                    )

    def contour_edges(self, frame, edges):
        """Detect and draw contours based on edge detection without labeling."""
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 300:  # Filter out small contours
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
        return frame

    # First Code: Display original frame with contours overlaid
    def process_frame_with_overlay(self, frame):
       
        yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        luminance = yuv_frame[:, :, 0]

        denoised_luminance = automated_perona_malik(luminance, iterations=10, tau=0.08)
        denoised_luminance = (denoised_luminance * 255).astype(np.uint8)
        yuv_frame[:, :, 0] = denoised_luminance
        denoised_frame = cv2.cvtColor(yuv_frame, cv2.COLOR_YUV2BGR)

        hsv_frame = cv2.cvtColor(denoised_frame, cv2.COLOR_BGR2HSV)

        overlay = frame.copy()
        for color_range in self.color_ranges:
            mask = self.apply_mask(hsv_frame, color_range)
            # Only call the selected labeling method
            if self.label_type == "rectangle":
                self.label_objects(overlay, mask, color_range)  # Draw rectangles only
            elif self.label_type == "contour":
                overlay = self.contour_objects(overlay, mask, color_range)  # Draw contours only

        gray_denoised = cv2.cvtColor(denoised_frame, cv2.COLOR_BGR2GRAY)
        edges_denoised = cv2.Canny(gray_denoised, 50, 150)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        closed_edges_denoised = cv2.morphologyEx(edges_denoised, cv2.MORPH_CLOSE, kernel)

        overlay = self.contour_edges(overlay, closed_edges_denoised)

        # Combine original frame and overlay
        combined_frame = cv2.addWeighted(frame, 0.6, overlay, 0.4, 0)

        return combined_frame, closed_edges_denoised  # Return combined frame and edges for display


# Update the real-time processing loop
def process_webcam_with_overlay(colors_list, label_type="rectangle", show_text=True, cvd="protanopia"):
    """Main function for processing webcam feed with overlay."""
    cap = cv2.VideoCapture(0)  # Use 0 for the default webcam; adjust if needed
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Define color ranges
    color_ranges = ColorRange.get_color_ranges(colors_list)
    color_detector = ColorDetector(color_ranges, label_type=label_type, show_text=show_text)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Resize frame
        frame = cv2.resize(frame, (320, 240))
        
        
        # Process the frame for edge and color detection
        combined_frame, edges = color_detector.process_frame_with_overlay(frame)

        # Display the combined frame
        cv2.imshow("Processed Frame with Original Background", combined_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


