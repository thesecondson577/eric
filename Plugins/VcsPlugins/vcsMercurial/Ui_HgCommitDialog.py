# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/HgCommitDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgCommitDialog(object):
    def setupUi(self, HgCommitDialog):
        HgCommitDialog.setObjectName("HgCommitDialog")
        HgCommitDialog.resize(450, 350)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(HgCommitDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logGroup = QtWidgets.QGroupBox(HgCommitDialog)
        self.logGroup.setObjectName("logGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.logGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logEdit = QtWidgets.QTextEdit(self.logGroup)
        self.logEdit.setTabChangesFocus(True)
        self.logEdit.setAcceptRichText(False)
        self.logEdit.setObjectName("logEdit")
        self.verticalLayout.addWidget(self.logEdit)
        self.label = QtWidgets.QLabel(self.logGroup)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.recentComboBox = QtWidgets.QComboBox(self.logGroup)
        self.recentComboBox.setObjectName("recentComboBox")
        self.verticalLayout.addWidget(self.recentComboBox)
        self.verticalLayout_2.addWidget(self.logGroup)
        self.amendCheckBox = QtWidgets.QCheckBox(HgCommitDialog)
        self.amendCheckBox.setObjectName("amendCheckBox")
        self.verticalLayout_2.addWidget(self.amendCheckBox)
        self.subrepoCheckBox = QtWidgets.QCheckBox(HgCommitDialog)
        self.subrepoCheckBox.setObjectName("subrepoCheckBox")
        self.verticalLayout_2.addWidget(self.subrepoCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgCommitDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(HgCommitDialog)
        QtCore.QMetaObject.connectSlotsByName(HgCommitDialog)
        HgCommitDialog.setTabOrder(self.logEdit, self.recentComboBox)
        HgCommitDialog.setTabOrder(self.recentComboBox, self.amendCheckBox)
        HgCommitDialog.setTabOrder(self.amendCheckBox, self.subrepoCheckBox)
        HgCommitDialog.setTabOrder(self.subrepoCheckBox, self.buttonBox)

    def retranslateUi(self, HgCommitDialog):
        _translate = QtCore.QCoreApplication.translate
        HgCommitDialog.setWindowTitle(_translate("HgCommitDialog", "Mercurial"))
        self.logGroup.setTitle(_translate("HgCommitDialog", "Commit Message"))
        self.logEdit.setToolTip(_translate("HgCommitDialog", "Enter the log message."))
        self.logEdit.setWhatsThis(_translate("HgCommitDialog", "<b>Log Message</b>\n"
"<p>Enter the log message for the commit action.</p>"))
        self.label.setText(_translate("HgCommitDialog", "Recent commit messages"))
        self.recentComboBox.setToolTip(_translate("HgCommitDialog", "Select a recent commit message to use"))
        self.amendCheckBox.setToolTip(_translate("HgCommitDialog", "Select to amend the last commit (leave message empty to keep it)"))
        self.amendCheckBox.setText(_translate("HgCommitDialog", "Amend the last commit"))
        self.subrepoCheckBox.setToolTip(_translate("HgCommitDialog", "Select to commit sub-repositories as well"))
        self.subrepoCheckBox.setText(_translate("HgCommitDialog", "Commit sub-repositories"))

