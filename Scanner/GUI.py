# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Tyler\PycharmProjects\WebScanner\GUI\Version1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from Scanner import Whois
from Scanner import Output
from Scanner import CrossSite
from Scanner import Injection2_electric_boogaloo as inj
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(340, 150, 75, 23))
        self.scanButton.setObjectName("scanButton")
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(350, 210, 111, 31))
        self.outputlabel.setObjectName("outputlabel")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(170, 60, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.heading.setFont(font)
        self.heading.setObjectName("heading")
        self.Injection = QtWidgets.QRadioButton(self.centralwidget)
        self.Injection.setGeometry(QtCore.QRect(60, 210, 111, 21))
        self.Injection.setObjectName("Injection")
        self.crossSite = QtWidgets.QRadioButton(self.centralwidget)
        self.crossSite.setGeometry(QtCore.QRect(60, 230, 82, 17))
        self.crossSite.setObjectName("crossSite")
        self.domainLookup = QtWidgets.QRadioButton(self.centralwidget)
        self.domainLookup.setGeometry(QtCore.QRect(60, 250, 101, 16))
        self.domainLookup.setObjectName("domainLookup")
        self.all = QtWidgets.QRadioButton(self.centralwidget)
        self.all.setGeometry(QtCore.QRect(60, 270, 82, 17))
        self.all.setObjectName("all")
        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(270, 240, 221, 31))
        self.output.setObjectName("output")
        self.website = QtWidgets.QTextEdit(self.centralwidget)
        self.website.setGeometry(QtCore.QRect(100, 140, 221, 31))
        self.website.setObjectName("website")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.scanButton.clicked.connect(self.scan)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scanButton.setText(_translate("MainWindow", "Scan"))
        self.outputlabel.setText(_translate("MainWindow", "Output File"))
        self.heading.setText(_translate("MainWindow", "Web Scanner"))
        self.Injection.setText(_translate("MainWindow", "SQL Injection"))
        self.crossSite.setText(_translate("MainWindow", "XSS"))
        self.domainLookup.setText(_translate("MainWindow", "Domain Lookup"))
        self.all.setText(_translate("MainWindow", "All"))

    def scan(self):
        output = Output.Output(self.output.toPlainText())
        output.openingMessage()
        output.append("\n")
        thisWebsite = self.website.toPlainText()

        if(self.domainLookup.isChecked()):
            self.whois(self.website.toPlainText(), output)

        if(self.Injection.isChecked()):
            self.injection(thisWebsite, output)

        if(self.crossSite.isChecked()):
            self.cross(thisWebsite, output)

        if(self.all.isChecked()):
            self.cross(thisWebsite, output)
            output.append("")
            self.whois(self.website.toPlainText(), output)
            self.injection(thisWebsite, output)


    def cross(self, website, output):
        output.append("Looking for CrossSite Vulnerabilities for: " + website + "\n")
        cross = CrossSite.CrossSite(website)
        output.append(cross.scan_xss())


    def whois(self, website, output):
        output.append("Looking up Domain Information for: " + website + "\n")
        whoIs_hold = Whois.Whois(website)
        results = whoIs_hold.lookup()
        output.append(results)


    def injection(self, website, output):
        output.append("Looking for Injection Vulnerabilities for: " + website + "\n")
        inject = inj.Injection_2(website)
        output.append(inject.inject())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
