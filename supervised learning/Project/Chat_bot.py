import os
from dotenv import load_dotenv
import google.generativeai as ai
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QIcon

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the API
ai.configure(api_key=API_KEY)

# Initialize the chatbot
model = ai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST AI ")
        self.setGeometry(100, 100, 500, 600)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\chat-bot.png"))

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Chat display
        self.chat_display = QTextEdit(self)
        self.chat_display.setObjectName("chat")
        self.chat_display.setReadOnly(True)
        self.chat_display.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.chat_display)


        # Input field
        self.input_field = QLineEdit(self)
        self.input_field.setObjectName("text")
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.returnPressed.connect(self.send_message)
        self.layout.addWidget(self.input_field)
        self.input_field.setFixedSize(500,50) # width ,height in px

        # Send button
        self.send_button = QPushButton("Send",self)
       # self.send_button.setIcon(QIcon("send.png"))
        #self.send_button.setIconSize(self.send_button.size())
       # self.send_button.show()
        self.send_button.setObjectName("Send")
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)
        self.INITUI()

    def send_message(self):
        user_message = self.input_field.text().strip()
        if not user_message:
            return

        if user_message.lower() == "bye":
            self.append_message("You", user_message)
            self.append_message("GHOST", "Goodbye!")
            QApplication.quit()
            return

        self.append_message("You", user_message)
        self.input_field.clear()

        try:
            response = chat.send_message(user_message)
            self.append_message("GHOST", response.text.capitalize())
        except Exception as e:
            self.append_message("GHOST", f"Error: {e}")

    def append_message(self, sender, message):
        self.chat_display.append(f"<b>{sender}:</b> {message}")
    def INITUI(self):
        self.setStyleSheet("""
        QPushButton#Send{
                           background-color:hsl(44, 6%, 60%);
                           font-size:25px;
                           padding: 15px 75px;    
                           margin: 25px;
                           border: 3px solid;
                           border-radius: 15px;
                           }
        QPushButton#Send:hover{
                           background-color:hsl(44, 6%, 80%);
                           }
        QTextEdit#chat{   
                           font-size:25px;
                           font-family:calibri;
                           }
        QLineEdit#chat{
                           font-size:25px;
                           font-family:calibri;
                           }
                           """)

# Main Application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    chatbot_app = ChatbotApp()
    chatbot_app.show()
    sys.exit(app.exec_())
