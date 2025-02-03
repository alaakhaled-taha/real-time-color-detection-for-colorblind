
from color_detector import process_webcam_with_overlay
from color_matcher import calc_real_time_denoising_with_contours_overlay

if __name__ == "__main__":
    print("Choose functionality:")
    print("1. Color Detection with predefined ranges")
    print("2. Color Matching for a specific color")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("Enter the type of CVD simulation:")
        print("Options: normal, protanopia, deuteranopia, tritanopia")
        cvd_type = input("Enter CVD type: ").lower()
        print("Choose the labeling method:")
        print("1. Rectangle labels")
        print("2. Contour labels")
        label_choice = input("Enter 1 or 2: ")
        label_type = "rectangle" if label_choice == "1" else "contour"

        text_choice = input("Do you want to display text on labels? (yes/no): ").lower()
        show_text = text_choice == "yes"
   
        process_webcam_with_overlay(label_type=label_type, show_text=show_text,cvd=cvd_type)
       
    elif choice == "2":
        bgr_input = input("Enter a BGR color (e.g., 255,0,0 for blue): ")
        bgr_color = [int(c) for c in bgr_input.split(",")]
        calc_real_time_denoising_with_contours_overlay(bgr_color=bgr_color)


       