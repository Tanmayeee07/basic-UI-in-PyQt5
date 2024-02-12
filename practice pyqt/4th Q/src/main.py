import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
class NameInputDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Output")
        self.setGeometry(1000, 400, 800, 600)

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Enter your name:", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.name_input = QLineEdit(self)
        self.layout.addWidget(self.name_input)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.show_greeting_message)
        self.layout.addWidget(self.ok_button)

    def show_greeting_message(self):
        user_name = self.name_input.text()
        if user_name:
            greeting_message = user_name
            QMessageBox.information(self, "My Name", greeting_message)
            self.accept()  # Close the dialog

if __name__ == "__main__":
    app = QApplication(sys.argv)

    name_dialog = NameInputDialog()
    name_dialog.exec_()

    sys.exit(app.exec_())
