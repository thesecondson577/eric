# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Helpviewer/UrlBar/BookmarkActionSelectionDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookmarkActionSelectionDialog(object):
    def setupUi(self, BookmarkActionSelectionDialog):
        BookmarkActionSelectionDialog.setObjectName("BookmarkActionSelectionDialog")
        BookmarkActionSelectionDialog.resize(291, 153)
        BookmarkActionSelectionDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(BookmarkActionSelectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon = QtWidgets.QLabel(BookmarkActionSelectionDialog)
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.verticalLayout.addWidget(self.icon)
        self.label_2 = QtWidgets.QLabel(BookmarkActionSelectionDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.bookmarkPushButton = QtWidgets.QPushButton(BookmarkActionSelectionDialog)
        self.bookmarkPushButton.setObjectName("bookmarkPushButton")
        self.verticalLayout.addWidget(self.bookmarkPushButton)
        self.speeddialPushButton = QtWidgets.QPushButton(BookmarkActionSelectionDialog)
        self.speeddialPushButton.setObjectName("speeddialPushButton")
        self.verticalLayout.addWidget(self.speeddialPushButton)

        self.retranslateUi(BookmarkActionSelectionDialog)
        QtCore.QMetaObject.connectSlotsByName(BookmarkActionSelectionDialog)

    def retranslateUi(self, BookmarkActionSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("BookmarkActionSelectionDialog", "<b>Add/Edit Bookmark</b>"))

