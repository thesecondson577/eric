# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/AddLanguageDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddLanguageDialog(object):
    def setupUi(self, AddLanguageDialog):
        AddLanguageDialog.setObjectName("AddLanguageDialog")
        AddLanguageDialog.resize(245, 77)
        AddLanguageDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(AddLanguageDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.languageLabel = QtWidgets.QLabel(AddLanguageDialog)
        self.languageLabel.setObjectName("languageLabel")
        self.hboxlayout.addWidget(self.languageLabel)
        self.languageCombo = QtWidgets.QComboBox(AddLanguageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.languageCombo.sizePolicy().hasHeightForWidth())
        self.languageCombo.setSizePolicy(sizePolicy)
        self.languageCombo.setEditable(True)
        self.languageCombo.setDuplicatesEnabled(False)
        self.languageCombo.setObjectName("languageCombo")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.languageCombo.addItem("")
        self.hboxlayout.addWidget(self.languageCombo)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddLanguageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.languageLabel.setBuddy(self.languageCombo)

        self.retranslateUi(AddLanguageDialog)
        self.buttonBox.accepted.connect(AddLanguageDialog.accept)
        self.buttonBox.rejected.connect(AddLanguageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddLanguageDialog)

    def retranslateUi(self, AddLanguageDialog):
        _translate = QtCore.QCoreApplication.translate
        AddLanguageDialog.setWindowTitle(_translate("AddLanguageDialog", "Add Language"))
        AddLanguageDialog.setToolTip(_translate("AddLanguageDialog", "Add a language to the current project"))
        AddLanguageDialog.setWhatsThis(_translate("AddLanguageDialog", "<b>Add Language Dialog</b>\n"
"<p>This dialog is used to add a language to the current project.</p>"))
        self.languageLabel.setText(_translate("AddLanguageDialog", "&Language:"))
        self.languageCombo.setToolTip(_translate("AddLanguageDialog", "Select a language to add to the current project"))
        self.languageCombo.setWhatsThis(_translate("AddLanguageDialog", "<b>Language</b>\n"
"<p>Select a language to add to the current project.</p>"))
        self.languageCombo.setItemText(0, _translate("AddLanguageDialog", "af"))
        self.languageCombo.setItemText(1, _translate("AddLanguageDialog", "ar"))
        self.languageCombo.setItemText(2, _translate("AddLanguageDialog", "bg"))
        self.languageCombo.setItemText(3, _translate("AddLanguageDialog", "bo"))
        self.languageCombo.setItemText(4, _translate("AddLanguageDialog", "br"))
        self.languageCombo.setItemText(5, _translate("AddLanguageDialog", "bs"))
        self.languageCombo.setItemText(6, _translate("AddLanguageDialog", "ca"))
        self.languageCombo.setItemText(7, _translate("AddLanguageDialog", "cs"))
        self.languageCombo.setItemText(8, _translate("AddLanguageDialog", "cy"))
        self.languageCombo.setItemText(9, _translate("AddLanguageDialog", "da"))
        self.languageCombo.setItemText(10, _translate("AddLanguageDialog", "de"))
        self.languageCombo.setItemText(11, _translate("AddLanguageDialog", "el"))
        self.languageCombo.setItemText(12, _translate("AddLanguageDialog", "en"))
        self.languageCombo.setItemText(13, _translate("AddLanguageDialog", "en_GB"))
        self.languageCombo.setItemText(14, _translate("AddLanguageDialog", "en_US"))
        self.languageCombo.setItemText(15, _translate("AddLanguageDialog", "eo"))
        self.languageCombo.setItemText(16, _translate("AddLanguageDialog", "es"))
        self.languageCombo.setItemText(17, _translate("AddLanguageDialog", "et"))
        self.languageCombo.setItemText(18, _translate("AddLanguageDialog", "eu"))
        self.languageCombo.setItemText(19, _translate("AddLanguageDialog", "fi"))
        self.languageCombo.setItemText(20, _translate("AddLanguageDialog", "fr"))
        self.languageCombo.setItemText(21, _translate("AddLanguageDialog", "ga"))
        self.languageCombo.setItemText(22, _translate("AddLanguageDialog", "gl"))
        self.languageCombo.setItemText(23, _translate("AddLanguageDialog", "gu"))
        self.languageCombo.setItemText(24, _translate("AddLanguageDialog", "he"))
        self.languageCombo.setItemText(25, _translate("AddLanguageDialog", "hi"))
        self.languageCombo.setItemText(26, _translate("AddLanguageDialog", "hu"))
        self.languageCombo.setItemText(27, _translate("AddLanguageDialog", "id"))
        self.languageCombo.setItemText(28, _translate("AddLanguageDialog", "is"))
        self.languageCombo.setItemText(29, _translate("AddLanguageDialog", "it"))
        self.languageCombo.setItemText(30, _translate("AddLanguageDialog", "ja"))
        self.languageCombo.setItemText(31, _translate("AddLanguageDialog", "km"))
        self.languageCombo.setItemText(32, _translate("AddLanguageDialog", "ko"))
        self.languageCombo.setItemText(33, _translate("AddLanguageDialog", "lt"))
        self.languageCombo.setItemText(34, _translate("AddLanguageDialog", "lv"))
        self.languageCombo.setItemText(35, _translate("AddLanguageDialog", "mi"))
        self.languageCombo.setItemText(36, _translate("AddLanguageDialog", "mk"))
        self.languageCombo.setItemText(37, _translate("AddLanguageDialog", "mr"))
        self.languageCombo.setItemText(38, _translate("AddLanguageDialog", "nl"))
        self.languageCombo.setItemText(39, _translate("AddLanguageDialog", "no"))
        self.languageCombo.setItemText(40, _translate("AddLanguageDialog", "no_NY"))
        self.languageCombo.setItemText(41, _translate("AddLanguageDialog", "oc"))
        self.languageCombo.setItemText(42, _translate("AddLanguageDialog", "pl"))
        self.languageCombo.setItemText(43, _translate("AddLanguageDialog", "pt"))
        self.languageCombo.setItemText(44, _translate("AddLanguageDialog", "pt_BR"))
        self.languageCombo.setItemText(45, _translate("AddLanguageDialog", "ro"))
        self.languageCombo.setItemText(46, _translate("AddLanguageDialog", "ru"))
        self.languageCombo.setItemText(47, _translate("AddLanguageDialog", "sk"))
        self.languageCombo.setItemText(48, _translate("AddLanguageDialog", "sl"))
        self.languageCombo.setItemText(49, _translate("AddLanguageDialog", "sr"))
        self.languageCombo.setItemText(50, _translate("AddLanguageDialog", "sv"))
        self.languageCombo.setItemText(51, _translate("AddLanguageDialog", "ta"))
        self.languageCombo.setItemText(52, _translate("AddLanguageDialog", "th"))
        self.languageCombo.setItemText(53, _translate("AddLanguageDialog", "tr"))
        self.languageCombo.setItemText(54, _translate("AddLanguageDialog", "uk"))
        self.languageCombo.setItemText(55, _translate("AddLanguageDialog", "vn"))
        self.languageCombo.setItemText(56, _translate("AddLanguageDialog", "wa"))
        self.languageCombo.setItemText(57, _translate("AddLanguageDialog", "zh_CN.GB2312"))
        self.languageCombo.setItemText(58, _translate("AddLanguageDialog", "zh_TW.Big5"))
