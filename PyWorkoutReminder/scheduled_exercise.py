#Schedule this py script in task scheduler for constant reminder may be 30min/1 hour

import random
import os
import time


time.sleep(5)
exercise = [
    "jumping jacks",
    "arm circles",
    "high knees",
    "squat",
    "lunges",
    "side lunges",
    "push up",
    "wall sit",
    "mountain climbers",
    "plank hold",
    "superman hold",
    "glute bridges",
    "sit ups",
    "leg raises",
    "burpees"
]



random_exercise = random.choice(exercise)
random_number = random.randint(20,40)

os.system(
    f'edge-playback --voice "en-US-GuyNeural" '
    f'--text "It\'s time for {random_exercise}. Do {random_number} {random_exercise}s. '
    f'And if you can\'t, just tap your legs to stay active."'
)


os.system(
    f'edge-playback --voice "en-US-GuyNeural" '
    f'--text "Ready"'
)


os.system(
    f'edge-playback --voice "en-US-GuyNeural" '
    f'--text "Steady"'
)

os.system(
    f'edge-playback --voice "en-US-GuyNeural" '
    f'--text "Go"'
)


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer

class TransparentGIF(QWidget):
    def __init__(self, gif_path):
        super().__init__()

        # Set window flags for transparent, borderless, always-on-top
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool  # Prevent taskbar icon
        )

        # Enable transparency
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # Optional: click-through

        # QLabel to play the GIF
        self.label = QLabel(self)
        self.label.setAttribute(Qt.WA_TranslucentBackground)

        self.movie = QMovie(gif_path)
        self.label.setMovie(self.movie)
        self.movie.start()

        # Resize window to fit GIF
        self.resize(self.movie.frameRect().size())

        # Move to top-right (adjust as needed)
        self.move(800, 0)

        # Optional: close after x seconds
        QTimer.singleShot(random_number*1000*2, self.close)

gif_folder_path = r"C:\Users\onwei_on_cloud\Documents\exercise_gif"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gif_path = rf"{gif_folder_path}\{random_exercise}.gif"  # Replace with your GIF path
    player = TransparentGIF(gif_path)
    player.show()
    sys.exit(app.exec_())



