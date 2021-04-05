from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.image_path = "InputData/BasicColorSelection/test_image.jpg"

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 1225)
        MainWindow.setGeometry(50,50, 1032, 1225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img_Gaussian = QtWidgets.QLabel(self.centralwidget)
        self.img_Gaussian.setGeometry(QtCore.QRect(0, 180, 1041, 481))
        self.img_Gaussian.setText("")
        self.img_Gaussian.setPixmap(QtGui.QPixmap(self.image_path))
        self.img_Gaussian.setScaledContents(True)
        self.img_Gaussian.setObjectName("img_Gaussian")
        self.horSlid_kernelSize = QtWidgets.QSlider(self.centralwidget)
        self.horSlid_kernelSize.setGeometry(QtCore.QRect(190, 20, 831, 22))
        self.horSlid_kernelSize.setMinimum(1)
        self.horSlid_kernelSize.setMaximum(15)
        self.horSlid_kernelSize.setSingleStep(2)
        self.horSlid_kernelSize.setPageStep(2)
        self.horSlid_kernelSize.setTracking(True)
        self.horSlid_kernelSize.setOrientation(QtCore.Qt.Horizontal)
        self.horSlid_kernelSize.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horSlid_kernelSize.setTickInterval(2)
        self.horSlid_kernelSize.setObjectName("horSlid_kernelSize")
        self.horSlid_lowThreshold = QtWidgets.QSlider(self.centralwidget)
        self.horSlid_lowThreshold.setGeometry(QtCore.QRect(190, 60, 831, 22))
        self.horSlid_lowThreshold.setMaximum(300)
        self.horSlid_lowThreshold.setTracking(True)
        self.horSlid_lowThreshold.setOrientation(QtCore.Qt.Horizontal)
        self.horSlid_lowThreshold.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horSlid_lowThreshold.setTickInterval(25)
        self.horSlid_lowThreshold.setObjectName("horSlid_lowThreshold")
        self.horSlid_highThreshold = QtWidgets.QSlider(self.centralwidget)
        self.horSlid_highThreshold.setGeometry(QtCore.QRect(190, 100, 831, 22))
        self.horSlid_highThreshold.setMaximum(300)
        self.horSlid_highThreshold.setOrientation(QtCore.Qt.Horizontal)
        self.horSlid_highThreshold.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horSlid_highThreshold.setTickInterval(25)
        self.horSlid_highThreshold.setTracking(True)
        self.horSlid_highThreshold.setObjectName("horSlid_highThreshold")
        self.lab_kernelSize = QtWidgets.QLabel(self.centralwidget)
        self.lab_kernelSize.setGeometry(QtCore.QRect(30, 20, 71, 21))
        self.lab_kernelSize.setObjectName("lab_kernelSize")
        self.lab_lowThreshold = QtWidgets.QLabel(self.centralwidget)
        self.lab_lowThreshold.setGeometry(QtCore.QRect(30, 60, 101, 21))
        self.lab_lowThreshold.setObjectName("lab_lowThreshold")
        self.lab_highThreshold = QtWidgets.QLabel(self.centralwidget)
        self.lab_highThreshold.setGeometry(QtCore.QRect(30, 100, 101, 21))
        self.lab_highThreshold.setObjectName("lab_highThreshold")
        self.lab_kernelSize_val = QtWidgets.QLabel(self.centralwidget)
        self.lab_kernelSize_val.setGeometry(QtCore.QRect(110, 20, 61, 21))
        self.lab_kernelSize_val.setObjectName("lab_kernelSize_val")
        self.lab_lowThreshold_val = QtWidgets.QLabel(self.centralwidget)
        self.lab_lowThreshold_val.setGeometry(QtCore.QRect(130, 60, 41, 21))
        self.lab_lowThreshold_val.setObjectName("lab_lowThreshold_val")
        self.lab_highThreshold_val = QtWidgets.QLabel(self.centralwidget)
        self.lab_highThreshold_val.setGeometry(QtCore.QRect(120, 100, 61, 21))
        self.lab_highThreshold_val.setObjectName("lab_highThreshold_val")
        self.img_Canny = QtWidgets.QLabel(self.centralwidget)
        self.img_Canny.setGeometry(QtCore.QRect(0, 680, 1041, 481))
        self.img_Canny.setText("")
        self.img_Canny.setPixmap(QtGui.QPixmap(self.image_path))
        self.img_Canny.setScaledContents(True)
        self.img_Canny.setObjectName("img_Canny")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionEdit)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)

        self.init_sliders()

        self.image = mpimg.imread(self.image_path)
        self.image_Gaussian = mpimg.imread(self.image_path)
        self.image_Canny = mpimg.imread(self.image_path)

        self.low_threshold = 0
        self.high_threshold = 0


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_kernelSize.setText(_translate("MainWindow", "Kernel Size:"))
        self.lab_lowThreshold.setText(_translate("MainWindow", "Low Threshold:"))
        self.lab_highThreshold.setText(_translate("MainWindow", "High Threshold"))
        self.lab_kernelSize_val.setText(_translate("MainWindow", "0"))
        self.lab_lowThreshold_val.setText(_translate("MainWindow", "0"))
        self.lab_highThreshold_val.setText(_translate("MainWindow", "0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionEdit.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
    
    def init_sliders(self):
        self.horSlid_kernelSize.valueChanged.connect(self.updateKernelSize)
        self.horSlid_lowThreshold.valueChanged.connect(self.updateLowThreshold)
        self.horSlid_highThreshold.valueChanged.connect(self.updateHighThreshold)
    
    def updateKernelSize(self):
        kernel_size = self.horSlid_kernelSize.value()
        self.lab_kernelSize_val.setText(str(kernel_size))
        self.applyGaussian(kernel_size)
        self.applyCanny()

    def updateLowThreshold(self):
        self.low_threshold = self.horSlid_lowThreshold.value()
        self.lab_lowThreshold_val.setText(str(self.low_threshold))
        self.applyCanny()
    
    def updateHighThreshold(self):
        self.high_threshold = self.horSlid_highThreshold.value()
        self.lab_highThreshold_val.setText(str(self.high_threshold))
        self.applyCanny()
    
    def applyGaussian(self, kernel_size):
        if kernel_size % 2 == 0:
            return
        img = np.copy(self.image)
        gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        blur_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
        img_pixMap = self.imageToPixelmap(blur_image)
        self.img_Gaussian.setPixmap(img_pixMap)
        self.image_Gaussian = blur_image
    
    def applyCanny(self):
        img = np.copy(self.image_Gaussian)
        edges_image = cv2.Canny(img, self.low_threshold, self.high_threshold)
        img_pixMap = self.imageToPixelmap(edges_image)
        self.img_Canny.setPixmap(img_pixMap)
        self.image_Canny = edges_image
    
    def imageToPixelmap(self, img):
        height, width = img.shape
        bytes_per_line = 1 * width
        qImg = QImage(img.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        return QPixmap(qImg)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


