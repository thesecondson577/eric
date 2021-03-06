# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Previewers/PreviewerHTML.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreviewerHTML(object):
    def setupUi(self, PreviewerHTML):
        PreviewerHTML.setObjectName("PreviewerHTML")
        PreviewerHTML.resize(400, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(PreviewerHTML)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(PreviewerHTML)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.previewView = QtWebKitWidgets.QWebView(PreviewerHTML)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewView.sizePolicy().hasHeightForWidth())
        self.previewView.setSizePolicy(sizePolicy)
        self.previewView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.previewView.setUrl(QtCore.QUrl("about:blank"))
        self.previewView.setObjectName("previewView")
        self.verticalLayout.addWidget(self.previewView)
        self.jsCheckBox = QtWidgets.QCheckBox(PreviewerHTML)
        self.jsCheckBox.setObjectName("jsCheckBox")
        self.verticalLayout.addWidget(self.jsCheckBox)
        self.ssiCheckBox = QtWidgets.QCheckBox(PreviewerHTML)
        self.ssiCheckBox.setObjectName("ssiCheckBox")
        self.verticalLayout.addWidget(self.ssiCheckBox)

        self.retranslateUi(PreviewerHTML)
        QtCore.QMetaObject.connectSlotsByName(PreviewerHTML)

    def retranslateUi(self, PreviewerHTML):
        _translate = QtCore.QCoreApplication.translate
        self.jsCheckBox.setToolTip(_translate("PreviewerHTML", "Select to enable JavaScript for HTML previews"))
        self.jsCheckBox.setText(_translate("PreviewerHTML", "Enable JavaScript"))
        self.ssiCheckBox.setToolTip(_translate("PreviewerHTML", "Select to enable support for Server Side Includes"))
        self.ssiCheckBox.setText(_translate("PreviewerHTML", "Enable Server Side Includes"))

from PyQt5 import QtWebKitWidgets
