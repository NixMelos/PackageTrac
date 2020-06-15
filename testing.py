# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrackingApp.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.trackButton = QtWidgets.QPushButton(self.centralwidget)
        self.trackButton.setGeometry(QtCore.QRect(290, 370, 161, 61))
        self.trackButton.setObjectName("trackButton")
        self.clearAll = QtWidgets.QPushButton(self.centralwidget)
        self.clearAll.setGeometry(QtCore.QRect(550, 370, 161, 61))
        self.clearAll.setObjectName("clearAll")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(100, 0, 561, 81))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 120, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.trackingNum = QtWidgets.QLineEdit(self.centralwidget)
        self.trackingNum.setGeometry(QtCore.QRect(230, 120, 411, 41))
        self.trackingNum.setText("")
        self.trackingNum.setObjectName("trackingNum")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(105, 170, 601, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(110, 80, 507, 37))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.fedex = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fedex.setFont(font)
        self.fedex.setObjectName("fedex")
        self.ups = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ups.setFont(font)
        self.ups.setObjectName("ups")
        self.usps = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.usps.setFont(font)
        self.usps.setObjectName("usps")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSetting)
        self.menuFile.addAction(self.actionExit)
        self.menuExit.addAction(self.actionCopy)
        self.menuExit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.trackButton.setStatusTip(_translate("MainWindow", "Track "))
        self.trackButton.setText(_translate("MainWindow", "Track!"))
        self.clearAll.setText(_translate("MainWindow", "Clear"))
        self.label1.setText(_translate("MainWindow", "Lets Get Tracking"))
        self.label.setText(_translate("MainWindow", "Tracking Number:"))
        self.fedex.setText(_translate("MainWindow", "FedEx"))
        self.ups.setText(_translate("MainWindow", "UPS"))
        self.usps.setText(_translate("MainWindow", "USPS"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "New Tracking Number"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Saves current tracking"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
        self.actionSetting.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())