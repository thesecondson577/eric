# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsPySvn/SvnCopyDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnCopyDialog(object):
    def setupUi(self, SvnCopyDialog):
        SvnCopyDialog.setObjectName("SvnCopyDialog")
        SvnCopyDialog.resize(409, 138)
        SvnCopyDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnCopyDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1 = QtWidgets.QLabel(SvnCopyDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.sourceEdit = QtWidgets.QLineEdit(SvnCopyDialog)
        self.sourceEdit.setReadOnly(True)
        self.sourceEdit.setObjectName("sourceEdit")
        self.gridlayout.addWidget(self.sourceEdit, 0, 1, 1, 1)
        self.targetEdit = QtWidgets.QLineEdit(SvnCopyDialog)
        self.targetEdit.setObjectName("targetEdit")
        self.gridlayout.addWidget(self.targetEdit, 1, 1, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(SvnCopyDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.dirButton = QtWidgets.QToolButton(SvnCopyDialog)
        self.dirButton.setObjectName("dirButton")
        self.gridlayout.addWidget(self.dirButton, 1, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.forceCheckBox = QtWidgets.QCheckBox(SvnCopyDialog)
        self.forceCheckBox.setObjectName("forceCheckBox")
        self.vboxlayout.addWidget(self.forceCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnCopyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnCopyDialog)
        self.buttonBox.accepted.connect(SvnCopyDialog.accept)
        self.buttonBox.rejected.connect(SvnCopyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnCopyDialog)
        SvnCopyDialog.setTabOrder(self.targetEdit, self.dirButton)
        SvnCopyDialog.setTabOrder(self.dirButton, self.forceCheckBox)
        SvnCopyDialog.setTabOrder(self.forceCheckBox, self.buttonBox)
        SvnCopyDialog.setTabOrder(self.buttonBox, self.sourceEdit)

    def retranslateUi(self, SvnCopyDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnCopyDialog.setWindowTitle(_translate("SvnCopyDialog", "Subversion Copy"))
        self.textLabel1.setText(_translate("SvnCopyDialog", "Source:"))
        self.sourceEdit.setToolTip(_translate("SvnCopyDialog", "Shows the name of the source"))
        self.sourceEdit.setWhatsThis(_translate("SvnCopyDialog", "<b>Source name</b>\n"
"<p>This field shows the name of the source.</p>"))
        self.targetEdit.setToolTip(_translate("SvnCopyDialog", "Enter the target name"))
        self.targetEdit.setWhatsThis(_translate("SvnCopyDialog", "<b>Target name</b>\n"
"<p>Enter the new name in this field. The target must be the new name or an absolute path.</p>"))
        self.textLabel2.setText(_translate("SvnCopyDialog", "Target:"))
        self.dirButton.setToolTip(_translate("SvnCopyDialog", "Press to open a selection dialog"))
        self.dirButton.setWhatsThis(_translate("SvnCopyDialog", "<b>Target name</b>\n"
"<p>Select the target name for the operation via a selection dialog.</p>"))
        self.forceCheckBox.setToolTip(_translate("SvnCopyDialog", "Select to force the operation"))
        self.forceCheckBox.setText(_translate("SvnCopyDialog", "Enforce operation"))

