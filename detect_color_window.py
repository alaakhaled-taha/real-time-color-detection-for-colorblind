from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QMessageBox 
import cv2

from color_matcher import *
import time
import numpy as np
from PyQt5.QtCore import Qt

class DetectColorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.center_color = None
        self.start_detecting()

    def get_center_color(self, frame):
        # Get frame dimensions
        height, width, _ = frame.shape
        # Determine the center point
        center_x, center_y = width // 2, height // 2
        # Get the RGB value of the center pixel
        center_color_bgr = frame[center_y, center_x]
        return center_color_bgr

    def start_detecting(self):
        # Open the camera
        cap = cv2.VideoCapture(0)  # 0 is usually the default camera
        if not cap.isOpened():
            print("Error: Could not open camera.")
            exit()

        print("Press 'q' to exit.")

        last_print_time = time.time()

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame. Exiting.")
                break

            # Flip the frame for a natural webcam view
            frame = cv2.flip(frame, 1)

            # Get the current time
            current_time = time.time()

            self.center_color = self.get_center_color(frame)

            # Print the RGB value every 2 seconds
            if current_time - last_print_time >= 2:
                print(f"Center Color (BGR): {self.center_color}")
                last_print_time = current_time

            # Create a copy of the frame for display
            display_frame = frame.copy()
            
            # Draw a small circle at the center point for visualization
            height, width, _ = frame.shape
            center_x, center_y = width // 2, height // 2
            cv2.circle(display_frame, (center_x, center_y), 5, (0, 255, 0), -1)

            font = cv2.FONT_HERSHEY_SIMPLEX
            text = "Press Space to Capture"
            text_size = cv2.getTextSize(text, font, 0.5, 1)[0]  # Get text size
            text_x = center_x - text_size[0] // 2  # Center the text horizontally
            text_y = center_y + 20  # Position text below the circle

            cv2.putText(display_frame, text, (text_x, text_y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

            # Display the frame with the circle
            cv2.imshow("Camera Feed", display_frame)

            # Exit on 'q' key press
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == 32:  # Space key
                self.captured_color = self.center_color 
                print(f"Captured Color (BGR): {self.captured_color}")
                
                color_preview = np.zeros((100, 100, 3), dtype=np.uint8)
                color_preview[:] = self.captured_color
                cv2.imshow("Captured Color", color_preview)
                self.close()
                self.start_matching()
                
        cap.release()
        cv2.destroyAllWindows()
        
    def start_matching(self):
        try:
            calc_real_time_denoising_with_contours_overlay(bgr_color=self.captured_color)
            QMessageBox.information(self, "Process Complete", "Color matching has been completed.")
            self.close()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid BGR values (e.g., 255,0,0).")