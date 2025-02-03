import numpy as np
import cv2

# Color detection with OpenCV
class ColorRange:
    def __init__(self, name, lower_bound, upper_bound, label_color):
        self.name = name
        self.lower_bound = np.array(lower_bound, np.uint8)
        self.upper_bound = np.array(upper_bound, np.uint8)
        self.label_color = label_color
    color_dic = {
        "Red"    : [[6,0,197], (0, 0, 255)] ,
        "Green"  : [[5,137,13],(0, 255, 0)] ,
        "Blue"   : [[233,74,11],(255, 0, 0)] ,
        "Yellow" : [[20,188,186],(255, 255, 0)] ,
        "Orange" : [[7,130,193] ,(255, 165, 0)],
        "Violet" : [[245,45,130],(128, 0, 128)] ,
        "Cyan"   : [[225,215,22],(0, 255, 255)] 
    }
    def __str__(self):
        return f"ColorRange(name={self.name}, lower_bound={self.lower_bound}, upper_bound={self.upper_bound}, label_color={self.label_color})"
    def __repr__(self):
        return self.__str__()

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

    @classmethod 
    def get_color_ranges(cls, colors_list):  # Remove self parameter
        color_ranges = []
        for color in colors_list:
            color_value = cls.color_dic.get(color)[0]  # Use cls instead of self
            target_color = cls.color_dic.get(color)[1]
            lower, upper = cls.get_limits(color_value)
            color_ranges.append(ColorRange(color.upper() , lower, upper, target_color))  # Fixed ColorRange creation
        return color_ranges

    def get_color_ranges_for_cvd(cvd_type="protanopia"):
        
        
        # Adjusted ranges for different types of color blindness
        if cvd_type == "protanopia":
            # Simulate red blindness (no red perception)
            return [
                ColorRange("RED", [0, 120, 70], [10, 255, 255], (0, 0, 255)),  # Adjusted red range, unable to see red
                ColorRange("BLUE", [95, 100, 50], [150, 255, 255], (255, 0, 0)),  # Unchanged blue perception
                ColorRange("GREEN", [40, 50, 50], [80, 255, 255], (0, 255, 0)),  # Unchanged green perception
                ColorRange("YELLOW", [20, 100, 100], [30, 255, 255], (255, 255, 0)),
                ColorRange("ORANGE", [10, 100, 100], [25, 255, 255], (255, 165, 0)),
                ColorRange("VIOLET", [130, 50, 50], [160, 255, 255], (128, 0, 128)),
                ColorRange("CYAN", [80, 100, 100], [100, 255, 255], (0, 255, 255)),
            ]
        
        elif cvd_type == "deuteranopia":
            # Simulate green blindness (no green perception)
            return [
                ColorRange("RED", [0, 120, 70], [10, 255, 255], (0, 0, 255)),  # Unchanged red
                ColorRange("BLUE", [95, 100, 50], [150, 255, 255], (255, 0, 0)),  # Unchanged blue
                ColorRange("GREEN", [40, 50, 50], [80, 255, 255], (0, 255, 0)),  # Adjusted green range, unable to see green
            ]
        
        elif cvd_type == "tritanopia":
            # Simulate blue-yellow blindness (no blue perception)
            return [
                ColorRange("RED", [0, 120, 70], [10, 255, 255], (0, 0, 255)),  # Unchanged red perception
                ColorRange("BLUE", [95, 100, 50], [150, 255, 255], (255, 0, 0)),  # Adjusted blue range, unable to see blue
                ColorRange("GREEN", [40, 50, 50], [80, 255, 255], (0, 255, 0)),  # Unchanged green perception
            ]
        
        # Default (for normal vision)
        return [
            ColorRange("RED", [0, 120, 70], [10, 255, 255], (0, 0, 255)),
            ColorRange("RED", [136, 87, 111], [180, 255, 255], (0, 0, 255)),
            ColorRange("BLUE", [95, 100, 50], [150, 255, 255], (255, 0, 0)),
            ColorRange("GREEN", [40, 50, 50], [80, 255, 255], (0, 255, 0)),
        ]



colors_list = ["Red","Blue","Orange"]
color_ranges = ColorRange.get_color_ranges(colors_list)
print(color_ranges)