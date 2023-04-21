import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Slot

#@Slot()
def say_hello():
 print("Button clicked, Hello!")
 label.setText('Hello')

# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Click me")
label = QLabel('xxxx')
button.clicked.connect(say_hello)
lyt = QVBoxLayout(app)
lyt.addWidget(label)
lyt.addWidget(button)

#button.show()
#label.show()
# Run the main Qt loop
app.exec()
