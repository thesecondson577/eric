# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './E5Network/E5SslCertificatesInfoDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_E5SslCertificatesInfoDialog(object):
    def setupUi(self, E5SslCertificatesInfoDialog):
        E5SslCertificatesInfoDialog.setObjectName("E5SslCertificatesInfoDialog")
        E5SslCertificatesInfoDialog.resize(556, 486)
        E5SslCertificatesInfoDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(E5SslCertificatesInfoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sslWidget = E5SslCertificatesInfoWidget(E5SslCertificatesInfoDialog)
        self.sslWidget.setObjectName("sslWidget")
        self.verticalLayout.addWidget(self.sslWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(E5SslCertificatesInfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(E5SslCertificatesInfoDialog)
        self.buttonBox.accepted.connect(E5SslCertificatesInfoDialog.accept)
        self.buttonBox.rejected.connect(E5SslCertificatesInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(E5SslCertificatesInfoDialog)

    def retranslateUi(self, E5SslCertificatesInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        E5SslCertificatesInfoDialog.setWindowTitle(_translate("E5SslCertificatesInfoDialog", "SSL Certificate Info"))

from E5Network.E5SslCertificatesInfoWidget import E5SslCertificatesInfoWidget