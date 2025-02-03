import color_range
from color_range import ColorRange 
colors_with_rgb = {
    "VIOLET": [130, 45, 245],
    "CYAN": [22, 215, 225],
    "BLUE": [11, 74, 233],
    "ORANGE": [193, 130, 7],
    "YELLOW": [186, 188, 20],
    "RED": [197, 0, 6],
    "GREEN": [13, 137, 5],
}

colors_with_rgb = {
    "VIOLET": [130, 45, 245],
    "CYAN": [22, 215, 225],
    "BLUE": [11, 74, 233],
    "ORANGE": [193, 130, 7],
    "YELLOW": [186, 188, 20],
    "RED": [197, 0, 6],
    "GREEN": [13, 137, 5],
}

# Generate ColorRange objects
color_ranges = ColorRange.create_color_ranges(colors_with_rgb)

# Print the generated ranges
for cr in color_ranges:
    print(f"ColorRange({cr.name}, {cr.lower_bound.tolist()}, {cr.upper_bound.tolist()}, {cr.label_color})")
