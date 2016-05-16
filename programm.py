import sys
from PyQt4 import QtGui, QtCore, uic

class MeinDialog(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = uic.loadUi("hauptdialog.ui", self)

        # Slots einrichten
        self.ui.buttonOK.clicked.connect(self.onOK)
        self.ui.buttonAbbrechen.clicked.connect(self.onAbbrechen)

    def onOK(self):
        # Daten auslesen
        print "Vorname: %s" % self.ui.vorname.text()
        print "Nachname: %s" % self.ui.nachname.text()
        print "Adresse: %s" % self.ui.adresse.toPlainText()
        datum = self.ui.geburtsdatum.date().toString("dd.MM.yyyy")
        print "Geburtsdatum: %s" % datum

        if self.ui.agb.checkState():
            print "AGBs akzeptiert"
        if self.ui.newsletter.checkState():
            print "Katalog bestellt"

    def onAbbrechen(self):
        print "Schade"
        self.close()

app = QtGui.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())
