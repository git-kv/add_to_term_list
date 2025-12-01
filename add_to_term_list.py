import os, sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLineEdit, QPushButton, QSpacerItem, QCalendarWidget, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Assign values for width/height
        text_box_width = 200
        spacer_width = 240
        spacer_height = 15
        calendar_width = 260
        button_width = 260

        self.setWindowTitle("Add to Term List")

        # Create widgets for labels and text input fields
        self.first_name_label = QLabel('First Name:')
        self.first_name_text_box = QLineEdit()
        self.first_name_text_box.setFixedWidth(text_box_width)

        self.last_name_label = QLabel('Last Name:')
        self.last_name_text_box = QLineEdit()
        self.last_name_text_box.setMaximumWidth(text_box_width)

        self.username_label = QLabel('Username:')
        self.username_text_box = QLineEdit()
        self.username_text_box.setFixedWidth(text_box_width)

        self.manager_email_label = QLabel('Manager Email:')
        self.manager_email_text_box = QLineEdit()
        self.manager_email_text_box.setFixedWidth(text_box_width)

        self.hr_email_label = QLabel('HR Email:')
        self.hr_email_text_box = QLineEdit()
        self.hr_email_text_box.setFixedWidth(text_box_width)

        self.term_date_label = QLabel('Term Date:')
        self.term_date_calendar = QCalendarWidget()
        self.term_date_calendar.setFixedWidth(calendar_width)

        self.immediate_term_label = QLabel('Immediate Termination:')
        self.immediate_term_check_box = QCheckBox()

        self.add_to_term_list_button = QPushButton('Add to Term List')
        self.add_to_term_list_button.setFixedWidth(button_width)

        self.open_term_list_button = QPushButton('Open Term List')
        self.open_term_list_button.setFixedWidth(button_width)
        
        self.open_readme_button = QPushButton('Open ReadMe')
        self.open_readme_button.setFixedWidth(button_width)
        
        # Create window layout
        layout = QVBoxLayout()
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_text_box)
        layout.addSpacerItem(QSpacerItem(spacer_width,spacer_height))

        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_text_box)
        layout.addSpacerItem(QSpacerItem(spacer_width,spacer_height))

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_text_box)
        layout.addSpacerItem(QSpacerItem(spacer_width,spacer_height))

        layout.addWidget(self.manager_email_label)
        layout.addWidget(self.manager_email_text_box)
        layout.addSpacerItem(QSpacerItem(spacer_width,spacer_height))

        layout.addWidget(self.hr_email_label)
        layout.addWidget(self.hr_email_text_box)
        layout.addSpacerItem(QSpacerItem(spacer_width,spacer_height))

        layout.addWidget(self.term_date_label)
        layout.addWidget(self.term_date_calendar)
        layout.addSpacerItem(QSpacerItem(spacer_width,spacer_height))

        layout.addWidget(self.immediate_term_label)
        layout.addWidget(self.immediate_term_check_box)
        layout.addSpacerItem(QSpacerItem(spacer_width,spacer_height))
        layout.addSpacerItem(QSpacerItem(spacer_width,spacer_height))

        layout.addWidget(self.add_to_term_list_button)

        layout.addWidget(self.open_term_list_button)

        layout.addWidget(self.open_readme_button)

        # Prevent items from stretching vertically
        layout.insertStretch(-1,1)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()