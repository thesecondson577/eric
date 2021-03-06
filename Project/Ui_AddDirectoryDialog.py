# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/AddDirectoryDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddDirectoryDialog(object):
    def setupUi(self, AddDirectoryDialog):
        AddDirectoryDialog.setObjectName("AddDirectoryDialog")
        AddDirectoryDialog.resize(391, 174)
        AddDirectoryDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(AddDirectoryDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.filterComboBox = QtWidgets.QComboBox(AddDirectoryDialog)
        self.filterComboBox.setObjectName("filterComboBox")
        self.gridlayout.addWidget(self.filterComboBox, 0, 1, 1, 2)
        self.targetDirLabel = QtWidgets.QLabel(AddDirectoryDialog)
        self.targetDirLabel.setObjectName("targetDirLabel")
        self.gridlayout.addWidget(self.targetDirLabel, 2, 0, 1, 1)
        self.sourceDirEdit = QtWidgets.QLineEdit(AddDirectoryDialog)
        self.sourceDirEdit.setObjectName("sourceDirEdit")
        self.gridlayout.addWidget(self.sourceDirEdit, 1, 1, 1, 1)
        self.recursiveCheckBox = QtWidgets.QCheckBox(AddDirectoryDialog)
        self.recursiveCheckBox.setObjectName("recursiveCheckBox")
        self.gridlayout.addWidget(self.recursiveCheckBox, 3, 0, 1, 3)
        self.targetDirEdit = QtWidgets.QLineEdit(AddDirectoryDialog)
        self.targetDirEdit.setObjectName("targetDirEdit")
        self.gridlayout.addWidget(self.targetDirEdit, 2, 1, 1, 1)
        self.sourceDirLabel = QtWidgets.QLabel(AddDirectoryDialog)
        self.sourceDirLabel.setObjectName("sourceDirLabel")
        self.gridlayout.addWidget(self.sourceDirLabel, 1, 0, 1, 1)
        self.textLabel1 = QtWidgets.QLabel(AddDirectoryDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.sourceDirButton = QtWidgets.QToolButton(AddDirectoryDialog)
        self.sourceDirButton.setObjectName("sourceDirButton")
        self.gridlayout.addWidget(self.sourceDirButton, 1, 2, 1, 1)
        self.targetDirButton = QtWidgets.QToolButton(AddDirectoryDialog)
        self.targetDirButton.setObjectName("targetDirButton")
        self.gridlayout.addWidget(self.targetDirButton, 2, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddDirectoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.targetDirLabel.setBuddy(self.targetDirEdit)
        self.sourceDirLabel.setBuddy(self.sourceDirEdit)
        self.textLabel1.setBuddy(self.filterComboBox)

        self.retranslateUi(AddDirectoryDialog)
        self.buttonBox.accepted.connect(AddDirectoryDialog.accept)
        self.buttonBox.rejected.connect(AddDirectoryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddDirectoryDialog)
        AddDirectoryDialog.setTabOrder(self.filterComboBox, self.sourceDirEdit)
        AddDirectoryDialog.setTabOrder(self.sourceDirEdit, self.sourceDirButton)
        AddDirectoryDialog.setTabOrder(self.sourceDirButton, self.targetDirEdit)
        AddDirectoryDialog.setTabOrder(self.targetDirEdit, self.targetDirButton)
        AddDirectoryDialog.setTabOrder(self.targetDirButton, self.recursiveCheckBox)

    def retranslateUi(self, AddDirectoryDialog):
        _translate = QtCore.QCoreApplication.translate
        AddDirectoryDialog.setWindowTitle(_translate("AddDirectoryDialog", "Add Directory"))
        AddDirectoryDialog.setToolTip(_translate("AddDirectoryDialog", "Add a directory to the current project"))
        AddDirectoryDialog.setWhatsThis(_translate("AddDirectoryDialog", "<b>Add Directory Dialog</b>\n"
"<p>This dialog is used to add a directory to the current project.</p>"))
        self.targetDirLabel.setText(_translate("AddDirectoryDialog", "&Target Directory:"))
        self.sourceDirEdit.setToolTip(_translate("AddDirectoryDialog", "Enter the name of the directory to add"))
        self.sourceDirEdit.setWhatsThis(_translate("AddDirectoryDialog", "<b>Source Directory</b>\n"
"<p>Enter the name of the directory to add to the current project.\n"
" You may select it with a dialog by pressing the button to\n"
" the right.</p>"))
        self.recursiveCheckBox.setToolTip(_translate("AddDirectoryDialog", "Select, whether a recursive add should be performed"))
        self.recursiveCheckBox.setText(_translate("AddDirectoryDialog", "&Recurse into subdirectories"))
        self.targetDirEdit.setToolTip(_translate("AddDirectoryDialog", "Enter the target directory for the file"))
        self.targetDirEdit.setWhatsThis(_translate("AddDirectoryDialog", "<b>Target Directory</b>\n"
"<p>Enter the target directory. You may select it\n"
" with a dialog by pressing the button to the right.</p>"))
        self.sourceDirLabel.setText(_translate("AddDirectoryDialog", "&Source Directory:"))
        self.textLabel1.setText(_translate("AddDirectoryDialog", "&File Type:"))
        self.sourceDirButton.setWhatsThis(_translate("AddDirectoryDialog", "<b>Source Directory</b>\n"
"<p>Select the source directory via a directory selection dialog.</p>"))
        self.targetDirButton.setWhatsThis(_translate("AddDirectoryDialog", "<b>Target Directory</b>\n"
"<p>Select the target directory via a directory selection dialog.</p>"))

