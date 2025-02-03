import cv2
import numpy as np
from perona_malik import automated_perona_malik  # Assuming you have this implemented

class ColorMatcher:
    def __init__(self, bgr_color):
        self.bgr_color = np.array(bgr_color, dtype=np.uint8)
        self.target_hsv = cv2.cvtColor(self.bgr_color.reshape(1, 1, 3), cv2.COLOR_BGR2HSV)[0][0]
        self.lower_limit, self.upper_limit = self.get_limits(self.bgr_color)

    @staticmethod
    def calculate_color_match(target_hsv, detected_hsv):
        distance = np.linalg.norm(target_hsv - detected_hsv)
        max_distance = np.linalg.norm([180, 255, 255])
        similarity = 1 - (distance / max_distance)
        return similarity * 100

    @staticmethod
    def get_limits(color):
        hsv_color = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)[0][0]
        hue = hsv_color[0]
        if hue >= 165:
            lower = np.array([hue - 10, 100, 100], dtype=np.uint8)
            upper = np.array([180, 255, 255], dtype=np.uint8)
        elif hue <= 15:
            lower = np.array([0, 100, 100], dtype=np.uint8)
            upper = np.array([hue + 10, 255, 255], dtype=np.uint8)
        else:
            lower = np.array([hue - 10, 100, 100], dtype=np.uint8)
            upper = np.array([hue + 10, 255, 255], dtype=np.uint8)
        return lower, upper

    def apply_mask(self, hsv_frame):
        return cv2.inRange(hsv_frame, self.lower_limit, self.upper_limit)

    

    def contour_objects_with_overlay(self, frame, mask, original_frame):
        """Detect and label contours with overlay on the original frame."""
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        overlay = original_frame.copy()

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 300:  # Filter out small contours
                x, y, w, h = cv2.boundingRect(contour)
                detected_area = hsv_frame[y:y + h, x:x + w]
                avg_hsv = detected_area.mean(axis=(0, 1))
                match_percentage = self.calculate_color_match(self.target_hsv, avg_hsv)

                # Draw contour and label
                cv2.drawContours(overlay, [contour], -1, (0, 255, 0), thickness=cv2.FILLED)
                cv2.drawContours(overlay, [contour], -1, (0, 255, 0), 2)

                if match_percentage >= 50:
                    label = f"{match_percentage:.2f}% Match"
                    cv2.putText(overlay, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Combine original frame and overlay
        combined_frame = cv2.addWeighted(original_frame, 0.6, overlay, 0.4, 0)
        return combined_frame


def calc_real_time_denoising_with_contours_overlay(iterations=5, tau=0.01, bgr_color=None):
    """Real-time processing with overlay of contours on the original frame."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    matcher = ColorMatcher(bgr_color=bgr_color)

    print("Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Resize frame
        frame = cv2.resize(frame, (320, 240))

        # Convert frame to YUV color space and process luminance channel
        yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        luminance = yuv_frame[:, :, 0]

        # Apply Perona-Malik denoising
        denoised_luminance = automated_perona_malik(luminance.astype(np.float32), iterations, tau)
        denoised_luminance = (denoised_luminance * 255).astype(np.uint8)
        yuv_frame[:, :, 0] = denoised_luminance
        denoised_frame = cv2.cvtColor(yuv_frame, cv2.COLOR_YUV2BGR)

        # Detect matching color and contour objects with overlay
        hsv_frame = cv2.cvtColor(denoised_frame, cv2.COLOR_BGR2HSV)
        mask = matcher.apply_mask(hsv_frame)
        combined_frame = matcher.contour_objects_with_overlay(denoised_frame, mask, frame)

        # Show the combined frame
        cv2.imshow("Processed Frame with Original Background", combined_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
