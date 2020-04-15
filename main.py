import sys
import time

import qdarkstyle
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen, QProgressBar

import login_class

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Create and display the splash screen
    splash_pix = QPixmap('conti.jpg')

    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)

    # adding progress bar
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(20)
    progressBar.setGeometry(0, splash_pix.height() - 20, splash_pix.width(), 20)

    splash.show()
    splash.showMessage("<h1 ><font color='white'>Welcome, Product Management System</font></h1>", Qt.AlignBottom, Qt.black)

    for i in range(1, 21):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    time.sleep(2)
    splash.close()
    window = login_class.Login()
    window.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    sys.exit(app.exec_())


