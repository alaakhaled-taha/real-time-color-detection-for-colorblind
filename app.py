import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox , QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
from color_detector import process_webcam_with_overlay
from color_matcher import calc_real_time_denoising_with_contours_overlay
from detect_color_window import DetectColorWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Blindness Tool")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Welcome to Color Identification App")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 24px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title_label)

        # Color Detection Button
        detection_button = QPushButton("Color Detection with Predefined Ranges")
        detection_button.setStyleSheet(self.get_button_style())
        detection_button.clicked.connect(self.open_label_choice)
        layout.addWidget(detection_button)

        # Color Matching Button
        matching_button = QPushButton("Color Matching for a Specific Color")
        matching_button.setStyleSheet(self.get_button_style())
        matching_button.clicked.connect(self.open_color_input)
        layout.addWidget(matching_button)

        btn3 = QPushButton('Test')
        btn3.setStyleSheet(self.get_button_style())
        btn3.clicked.connect(self.open_ishihara_test)
        layout.addWidget(btn3)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_label_choice(self):
        self.label_choice_window = DiseaseChoiceWindow()
        self.label_choice_window.show()
        self.close()

    def open_ishihara_test(self):
    # Persist the web window as a global variable
        global web_window
        web_window = QtWidgets.QMainWindow()
        web_window.setWindowTitle("Ishihara Test")
        
        web_view = QWebEngineView()
        url = QtCore.QUrl("https://www.colorlitelens.com/color-blindness-test.html#Blue")  # Convert the URL string to a QUrl object
        web_view.setUrl(url)
        
        # Set QWebEngineView as the central widget of the new window
        web_window.setCentralWidget(web_view)
        web_window.resize(1024, 768)  # Resize the window
        web_window.show()        

    def open_color_input(self):
        self.color_detect_window = DetectColorWindow()
        self.color_detect_window.show()

    @staticmethod
    def get_button_style():
        return """
            QPushButton {
                background-color: #007BFF;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """


class DiseaseChoiceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Disease Choice")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: black;")

        # Main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Label
        label = QLabel("Options")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(label)

        # # First case
        # normal_button = QPushButton("Normal")
        # normal_button.setStyleSheet(self.get_button_style())
        # normal_button.clicked.connect(self.open_label_choice)
        # layout.addWidget(normal_button)

        # first case
        protanpia_button = QPushButton("Protanpia")
        protanpia_button.setStyleSheet(self.get_button_style())
        protanpia_button.clicked.connect(self.open_label_choice_1)
        layout.addWidget(protanpia_button)

        # second case
        deuteranopia_button = QPushButton("Deuteranopia")
        deuteranopia_button.setStyleSheet(self.get_button_style())
        deuteranopia_button.clicked.connect(self.open_label_choice_2)
        layout.addWidget(deuteranopia_button)

        # third case
        tritanopia_button = QPushButton("Tritanopia")
        tritanopia_button.setStyleSheet(self.get_button_style())
        tritanopia_button.clicked.connect(self.open_label_choice_3)
        layout.addWidget(tritanopia_button)

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #007BFF;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """

    def open_label_choice_1(self):
        self.label_choice_window = ColorSelectionWindow1()
        self.label_choice_window.show()
        self.close()

    def open_label_choice_2(self):
        self.label_choice_window = ColorSelectionWindow1()
        self.label_choice_window.show()
        self.close()
    def open_label_choice_3(self):
        self.label_choice_window = ColorSelectionWindow2()
        self.label_choice_window.show()
        self.close()




class ColorSelectionWindow1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Selection")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: black;")
        
        # Main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Instructions label
        self.label = QLabel("Select up to 3 colors:")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(self.label)

        # Checkboxes
        self.checkboxes = []
        colors = ["Red", "Green", "Orange", "Yellow"]
        for color in colors:
            checkbox = QCheckBox(color)
            checkbox.stateChanged.connect(self.limit_selection)
            checkbox.setStyleSheet("font-size: 24px; color : white ; ")
            self.checkboxes.append(checkbox)
            layout.addWidget(checkbox)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet( """
            QPushButton {
                background-color: #007BFF;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.submit_button.clicked.connect(self.submit_colors)
        layout.addWidget(self.submit_button)

    def limit_selection(self):
        # Count the number of currently selected checkboxes
        selected_checkboxes = [cb for cb in self.checkboxes if cb.isChecked()]
        if len(selected_checkboxes) >= 3:
            for checkbox in self.checkboxes:
                if not checkbox.isChecked():
                    # Disable unchecked checkboxes
                    checkbox.setEnabled(False)
        else:
            # Enable all checkboxes if less than 3 are selected
            for checkbox in self.checkboxes:
                checkbox.setEnabled(True)

    def submit_colors(self):
        # Get the selected colors
        selected_colors = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        
        # Print the selected colors (for debugging or demonstration purposes)
        print("Selected Colors:", selected_colors)
    
        # You can pass these colors to another window or function
        self.label_choice_window = LabelChoiceWindow(selected_colors)
        self.label_choice_window.show()
        self.close()




class ColorSelectionWindow2(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Selection")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: black;")
        
        # Main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Instructions label
        self.label = QLabel("Select up to 3 colors:")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(self.label)

        # Checkboxes
        self.checkboxes = []
        colors = ["Blue", "Violet", "Cyan"]
        for color in colors:
            checkbox = QCheckBox(color)
            checkbox.stateChanged.connect(self.limit_selection)
            checkbox.setStyleSheet("font-size: 24px; color : white ; ")
            self.checkboxes.append(checkbox)
            layout.addWidget(checkbox)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet( """
            QPushButton {
                background-color: #007BFF;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.submit_button.clicked.connect(self.submit_colors)
        layout.addWidget(self.submit_button)

    def limit_selection(self):
        # Count the number of currently selected checkboxes
        selected_checkboxes = [cb for cb in self.checkboxes if cb.isChecked()]
        if len(selected_checkboxes) >= 3:
            for checkbox in self.checkboxes:
                if not checkbox.isChecked():
                    # Disable unchecked checkboxes
                    checkbox.setEnabled(False)
        else:
            # Enable all checkboxes if less than 3 are selected
            for checkbox in self.checkboxes:
                checkbox.setEnabled(True)

    def submit_colors(self):
        # Get the selected colors
        selected_colors = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        
        # Print the selected colors (for debugging or demonstration purposes)
        print("Selected Colors:", selected_colors)
    
        # You can pass these colors to another window or function
        self.label_choice_window = LabelChoiceWindow(selected_colors)
        self.label_choice_window.show()
        self.close()





class LabelChoiceWindow(QMainWindow):
    def __init__(self,selected_colors):
        super().__init__()
        self.setWindowTitle("Label Choice")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: black;")
        self.selected_colors = selected_colors;
        layout = QVBoxLayout()

        label = QLabel("Choose the Labeling Method")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(label)

        # Rectangle Button
        rectangle_button = QPushButton("Rectangle Labels")
        rectangle_button.setStyleSheet(MainWindow.get_button_style())
        rectangle_button.clicked.connect(lambda: self.open_text_choice(self.selected_colors,"rectangle"))
        layout.addWidget(rectangle_button)

        # Contour Button
        contour_button = QPushButton("Contour Labels")
        contour_button.setStyleSheet(MainWindow.get_button_style())
        contour_button.clicked.connect(lambda: self.open_text_choice(self.selected_colors,"contour"))
        layout.addWidget(contour_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_text_choice(self, selected_colors ,label_type):
        self.text_choice_window = TextChoiceWindow(selected_colors,label_type)
        self.text_choice_window.show()
        self.close()


class TextChoiceWindow(QMainWindow):
    def __init__(self, selected_colors,label_type):
        super().__init__()
        self.label_type = label_type
        self.selected_colors = selected_colors
        self.setWindowTitle("Text Choice")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()

        label = QLabel("Do you want to display text on labels?")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(label)

        yes_button = QPushButton("Yes")
        yes_button.setStyleSheet(MainWindow.get_button_style())
        yes_button.clicked.connect(lambda: self.start_detection(True))
        layout.addWidget(yes_button)

        no_button = QPushButton("No")
        no_button.setStyleSheet(MainWindow.get_button_style())
        no_button.clicked.connect(lambda: self.start_detection(False))
        layout.addWidget(no_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_detection(self, show_text):
        process_webcam_with_overlay(self.selected_colors,label_type=self.label_type, show_text=show_text)
        QMessageBox.information(self, "Process Complete", "Color detection has been completed.")
        self.close()

        
class ColorInputWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Matching")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: black;")

        layout = QVBoxLayout()

        label = QLabel("Enter a BGR Color (e.g., 255,0,0 for blue):")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(label)

        self.bgr_input = QLineEdit()
        self.bgr_input.setPlaceholderText("Enter a BGR color (e.g., 255,0,0 for blue)")
        self.bgr_input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
                font-size: 16px;
                padding: 10px;
                border: 2px solid gray;
                border-radius: 5px;
            }
        """)
        layout.addWidget(self.bgr_input)

        confirm_button = QPushButton("Start Matching")
        confirm_button.setStyleSheet(MainWindow.get_button_style())
        confirm_button.clicked.connect(self.start_matching)
        layout.addWidget(confirm_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_matching(self):
        try:
            bgr_input = self.bgr_input.text()
            bgr_color = [int(c) for c in bgr_input.split(",")]
            calc_real_time_denoising_with_contours_overlay(bgr_color=bgr_color)
            QMessageBox.information(self, "Process Complete", "Color matching has been completed.")
            self.close()
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid BGR values (e.g., 255,0,0).")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
