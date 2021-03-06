# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/HgArchiveDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgArchiveDialog(object):
    def setupUi(self, HgArchiveDialog):
        HgArchiveDialog.setObjectName("HgArchiveDialog")
        HgArchiveDialog.resize(400, 167)
        HgArchiveDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgArchiveDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HgArchiveDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.archiveEdit = QtWidgets.QLineEdit(HgArchiveDialog)
        self.archiveEdit.setObjectName("archiveEdit")
        self.gridLayout.addWidget(self.archiveEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(HgArchiveDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.typeComboBox = QtWidgets.QComboBox(HgArchiveDialog)
        self.typeComboBox.setObjectName("typeComboBox")
        self.gridLayout.addWidget(self.typeComboBox, 1, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(HgArchiveDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.prefixEdit = QtWidgets.QLineEdit(HgArchiveDialog)
        self.prefixEdit.setObjectName("prefixEdit")
        self.gridLayout.addWidget(self.prefixEdit, 2, 1, 1, 2)
        self.subReposCheckBox = QtWidgets.QCheckBox(HgArchiveDialog)
        self.subReposCheckBox.setObjectName("subReposCheckBox")
        self.gridLayout.addWidget(self.subReposCheckBox, 3, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgArchiveDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)
        self.archiveButton = QtWidgets.QToolButton(HgArchiveDialog)
        self.archiveButton.setObjectName("archiveButton")
        self.gridLayout.addWidget(self.archiveButton, 0, 2, 1, 1)

        self.retranslateUi(HgArchiveDialog)
        self.buttonBox.accepted.connect(HgArchiveDialog.accept)
        self.buttonBox.rejected.connect(HgArchiveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgArchiveDialog)
        HgArchiveDialog.setTabOrder(self.archiveEdit, self.archiveButton)
        HgArchiveDialog.setTabOrder(self.archiveButton, self.typeComboBox)
        HgArchiveDialog.setTabOrder(self.typeComboBox, self.prefixEdit)
        HgArchiveDialog.setTabOrder(self.prefixEdit, self.subReposCheckBox)
        HgArchiveDialog.setTabOrder(self.subReposCheckBox, self.buttonBox)

    def retranslateUi(self, HgArchiveDialog):
        _translate = QtCore.QCoreApplication.translate
        HgArchiveDialog.setWindowTitle(_translate("HgArchiveDialog", "Mercurial Archive"))
        self.label.setText(_translate("HgArchiveDialog", "Archive:"))
        self.archiveEdit.setToolTip(_translate("HgArchiveDialog", "Enter the file name of the archive"))
        self.label_3.setText(_translate("HgArchiveDialog", "Type:"))
        self.typeComboBox.setToolTip(_translate("HgArchiveDialog", "Select the archive type"))
        self.label_2.setText(_translate("HgArchiveDialog", "Prefix:"))
        self.prefixEdit.setToolTip(_translate("HgArchiveDialog", "Enter the directory prefix for the files in the archive"))
        self.subReposCheckBox.setToolTip(_translate("HgArchiveDialog", "Select to recurse into subrepositories"))
        self.subReposCheckBox.setText(_translate("HgArchiveDialog", "Include Subrepositories"))
        self.archiveButton.setToolTip(_translate("HgArchiveDialog", "Press to select the archive file name via a file selection dialog"))

