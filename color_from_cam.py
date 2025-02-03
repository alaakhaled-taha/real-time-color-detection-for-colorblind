import cv2
import time

def get_center_color(frame):
    # Get frame dimensions
    height, width, _ = frame.shape
    # Determine the center point
    center_x, center_y = width // 2, height // 2
    # Get the RGB value of the center pixel
    center_color_bgr = frame[center_y, center_x]
    # Convert BGR to RGB
    # center_color_rgb = list(center_color_bgr[::-1])
    return center_color_bgr

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

    # Print the BGR value every 2 seconds
    if current_time - last_print_time >= 2:
        center_color = get_center_color(frame)
        print(f"Center Color (RGB): {center_color}")
        last_print_time = current_time

    # Draw a small circle at the center point for visualization
    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2
    cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
