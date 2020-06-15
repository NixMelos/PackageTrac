import sys

import easypost
from PyQt5 import QtWidgets, uic

easypost.api_key = 'EZAK5fcae8b853c949e7b24517a12059b054pPfZBYqxcoaXBdTD0odlRA'


# easypost api outputs datetime in ISO 8601


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__method
        uic.loadUi('updatedTrackingUi.ui', self)  # Load .ui file
        self.show()

        self.trackButton = self.findChild(QtWidgets.QPushButton, 'trackButton')  # find track button
        self.trackButton.clicked.connect(self.trackButtonPressed)
        self.clearall = self.findChild(QtWidgets.QPushButton, 'clearAll')
        self.clearall.clicked.connect(self.clearButtonPressed)
        self.input = self.findChild(QtWidgets.QLineEdit, 'trackingNum')
        self.output = self.findChild(QtWidgets.QListWidget, 'trackingDisp')
        self.error_dialog = QtWidgets.QErrorMessage()
        self.carrier = self.findChild(QtWidgets.QComboBox, 'comboBox')

    def trackButtonPressed(self):

        try:
            trackingnum = self.input.text()
            carrierselected = str(self.carrier.currentText())

            if (carrierselected == 0):
                tracker = easypost.Tracker.create(tracking_code=trackingnum)
            else:
                tracker = easypost.Tracker.create(tracking_code=trackingnum, carrier=carrierselected)
        except easypost.Error as e:
            self.error_dialog.showMessage("Invalid Tracking Number")
            e.json_body["invalid tracking number"]
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

        # self.output.setText(" Your package that is being delivered by " + carrierselected + " has the tracking number: " + trackingnum +"\n"+ )

    def clearButtonPressed(self):
        self.clear()

    def clear(self):
        self.input.clear()
        self.output.clear()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
