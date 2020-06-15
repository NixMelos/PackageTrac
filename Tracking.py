import sys

import easypost
from PyQt5 import QtWidgets, uic, QtGui

easypost.api_key = ''


# easypost api outputs datetime in ISO 8601

class Ui(QtWidgets.QMainWindow):
    tracking = ""

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__method
        uic.loadUi('updatedTrackingUi.ui', self)  # Load .ui file

        self.trackButton = self.findChild(QtWidgets.QPushButton, 'trackButton')  # find track button
        self.trackButton.clicked.connect(self.trackButtonPressed)

        self.clearall = self.findChild(QtWidgets.QPushButton, 'clearAll')
        self.clearall.clicked.connect(self.clearButtonPressed)

        self.input = self.findChild(QtWidgets.QLineEdit, 'trackingNum')  # get Tracking Number

        self.etaText = self.findChild(QtWidgets.QLineEdit, 'etaText')

        self.output = self.findChild(QtWidgets.QListWidget, 'trackingDisp')
        self.error_dialog = QtWidgets.QErrorMessage()

        self.carrier = self.findChild(QtWidgets.QComboBox, 'comboBox')

        self.apikey = self.findChild(QtWidgets.QLineEdit, 'apiKeyGet')

        self.enter = self.findChild(QtWidgets.QPushButton, 'enter')
        self.enter.clicked.connect(self.enterButtonPressed)

    def trackButtonPressed(self):
        tracking = self.input.text()
        carriers = str(self.carrier.currentText())
        if easypost.api_key == '':
            self.output.addItem('Enter API KEY From https://www.easypost.com/ ')
        elif len(tracking) < 8 or len(tracking) > 40:
            self.output.addItem("Enter valid tracking number")


        else:
            try:

                if carriers == 0 or carriers == "":
                    tracker = easypost.Tracker.create(tracking_code=tracking)

                else:
                    tracker = easypost.Tracker.create(tracking_code=tracking, carrier=carriers)

                self.output.addItem("View on EasyPost: " + tracker["public_url"])

                details = tracker["tracking_details"]
                i = 0
                for k in details:
                    location = str(tracker["tracking_details"][i]["tracking_location"]["city"])
                    time = k["datetime"]
                    status = k["status"]
                    description = k["description"]
                    info = str(time + " " + location + " " + status + " " + description)
                    self.output.addItem(info)

                    i = i + 1

            except easypost.Error as e:
                self.error_dialog.showMessage('Something Went Wrong')

    def clearButtonPressed(self):
        self.clear()

    def clear(self):
        self.input.clear()
        self.output.clear()

    def enterButtonPressed(self):
        easypost.api_key = self.apikey.text()

    def save(self):
        name = QtGui.QfileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
