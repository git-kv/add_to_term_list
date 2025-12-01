import os, sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLineEdit, QPushButton, QSpacerItem, QCalendarWidget, QCheckBox, QMessageBox

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
        self.first_name_text_box.textChanged.connect(self.check_fields_filled)

        self.last_name_label = QLabel('Last Name:')
        self.last_name_text_box = QLineEdit()
        self.last_name_text_box.setMaximumWidth(text_box_width)
        self.last_name_text_box.textChanged.connect(self.check_fields_filled)

        self.username_label = QLabel('Username:')
        self.username_text_box = QLineEdit()
        self.username_text_box.setFixedWidth(text_box_width)
        self.username_text_box.textChanged.connect(self.check_fields_filled)       

        self.manager_email_label = QLabel('Manager Email:')
        self.manager_email_text_box = QLineEdit()
        self.manager_email_text_box.setFixedWidth(text_box_width)
        self.manager_email_text_box.textChanged.connect(self.check_fields_filled)

        self.hr_email_label = QLabel('HR Email:')
        self.hr_email_text_box = QLineEdit()
        self.hr_email_text_box.setFixedWidth(text_box_width)
        self.hr_email_text_box.textChanged.connect(self.check_fields_filled)

        self.term_date_label = QLabel('Term Date:')
        self.term_date_calendar = QCalendarWidget()
        self.term_date_calendar.setFixedWidth(calendar_width)

        self.immediate_term_label = QLabel('Immediate Termination:')
        self.immediate_term_check_box = QCheckBox()

        self.add_to_term_list_button = QPushButton('Add to Term List')
        self.add_to_term_list_button.setFixedWidth(button_width)
        self.add_to_term_list_button.setEnabled(False)
        self.add_to_term_list_button.clicked.connect(self.add_to_term_list)

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
    
    def check_fields_filled(self):
        first_name_text = str(self.first_name_text_box.text())
        last_name_text = str(self.last_name_text_box.text())
        username_text = str(self.username_text_box.text())
        manager_email_text = str(self.manager_email_text_box.text())
        hr_email_text = str(self.hr_email_text_box.text())

        if first_name_text == '' \
            or last_name_text == '' \
            or username_text == '' \
            or manager_email_text == '' \
            or hr_email_text == '':
            self.add_to_term_list_button.setEnabled(False)
        else:
            self.add_to_term_list_button.setEnabled(True)

    def add_to_term_list(self):
        first_name_text = str(self.first_name_text_box.text())
        last_name_text = str(self.last_name_text_box.text())
        username_text = str(self.username_text_box.text())
        manager_email_text = str(self.manager_email_text_box.text())
        hr_email_text = str(self.hr_email_text_box.text())
        immediate_checked = self.immediate_term_check_box.isChecked()
        term_date = self.term_date_calendar.selectedDate().toString('MM/dd/yyyy')

        self.update_csv(first_name_text,
                        last_name_text,
                        username_text,
                        manager_email_text,
                        hr_email_text,
                        term_date)

        if (immediate_checked):
            self.disable_immediately(username_text)

        # Popup notifiying what was submitted and where to find logs.
        message_box = QMessageBox()
        message_box.setWindowTitle('Term List Updated')
        message_box.setText('The termination list has been updated with the following information\n' + \
                            '\nFirst name: ' + first_name_text + \
                            '\nLast name: ' + last_name_text + \
                            '\nFull name: ' + first_name_text + ' ' + last_name_text + \
                            '\nUsername: ' + username_text + \
                            '\nManager email: ' + manager_email_text + \
                            '\nHR email: ' + hr_email_text + \
                            '\nImmediate disablement: ' + str(immediate_checked) + \
                            '\nTerm date: ' + term_date + \
                            '\n\nLogs can be reviewed from \\\\eocservices.dartadvantage.com\\apps$\\programs\\path'
                            )
        message_box.exec()

    def update_csv(self, first_name, last_name, username, manager, hr, term_date):
        print(first_name)
        print(last_name)
        print(username)
        print(manager)
        print(hr)
        print(term_date)

    def disable_immediately(self, username):
        immediate_term_path = 'C:\\Users\\KVoelker\\' + username
        if not os.path.exists(immediate_term_path):
            with open(immediate_term_path, 'w') as file:
                file.write(username)
            print('file created')
        else:
            print('file already exists')
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()