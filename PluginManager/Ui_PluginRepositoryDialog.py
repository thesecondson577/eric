# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './PluginManager/PluginRepositoryDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PluginRepositoryDialog(object):
    def setupUi(self, PluginRepositoryDialog):
        PluginRepositoryDialog.setObjectName("PluginRepositoryDialog")
        PluginRepositoryDialog.resize(800, 675)
        PluginRepositoryDialog.setProperty("sizeGripEnabled", True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PluginRepositoryDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.repositoryList = QtWidgets.QTreeWidget(PluginRepositoryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.repositoryList.sizePolicy().hasHeightForWidth())
        self.repositoryList.setSizePolicy(sizePolicy)
        self.repositoryList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.repositoryList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.repositoryList.setRootIsDecorated(False)
        self.repositoryList.setItemsExpandable(False)
        self.repositoryList.setAllColumnsShowFocus(True)
        self.repositoryList.setObjectName("repositoryList")
        self.gridlayout.addWidget(self.repositoryList, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(PluginRepositoryDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QTextEdit(PluginRepositoryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.descriptionEdit.sizePolicy().hasHeightForWidth())
        self.descriptionEdit.setSizePolicy(sizePolicy)
        self.descriptionEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.descriptionEdit.setReadOnly(True)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridlayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(PluginRepositoryDialog)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.authorEdit = QtWidgets.QLineEdit(PluginRepositoryDialog)
        self.authorEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.authorEdit.setReadOnly(True)
        self.authorEdit.setObjectName("authorEdit")
        self.gridlayout.addWidget(self.authorEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(PluginRepositoryDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 3, 0, 1, 1)
        self.urlEdit = QtWidgets.QLineEdit(PluginRepositoryDialog)
        self.urlEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.urlEdit.setReadOnly(True)
        self.urlEdit.setObjectName("urlEdit")
        self.gridlayout.addWidget(self.urlEdit, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.line = QtWidgets.QFrame(PluginRepositoryDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.downloadProgress = QtWidgets.QProgressBar(PluginRepositoryDialog)
        self.downloadProgress.setProperty("value", 0)
        self.downloadProgress.setObjectName("downloadProgress")
        self.verticalLayout.addWidget(self.downloadProgress)
        self.statusLabel = QtWidgets.QLabel(PluginRepositoryDialog)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(PluginRepositoryDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.repositoryUrlEdit = QtWidgets.QLineEdit(PluginRepositoryDialog)
        self.repositoryUrlEdit.setReadOnly(True)
        self.repositoryUrlEdit.setObjectName("repositoryUrlEdit")
        self.horizontalLayout.addWidget(self.repositoryUrlEdit)
        self.repositoryUrlEditButton = QtWidgets.QPushButton(PluginRepositoryDialog)
        self.repositoryUrlEditButton.setCheckable(True)
        self.repositoryUrlEditButton.setObjectName("repositoryUrlEditButton")
        self.horizontalLayout.addWidget(self.repositoryUrlEditButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(PluginRepositoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PluginRepositoryDialog)
        QtCore.QMetaObject.connectSlotsByName(PluginRepositoryDialog)
        PluginRepositoryDialog.setTabOrder(self.repositoryList, self.buttonBox)
        PluginRepositoryDialog.setTabOrder(self.buttonBox, self.repositoryUrlEdit)
        PluginRepositoryDialog.setTabOrder(self.repositoryUrlEdit, self.repositoryUrlEditButton)

    def retranslateUi(self, PluginRepositoryDialog):
        _translate = QtCore.QCoreApplication.translate
        PluginRepositoryDialog.setWindowTitle(_translate("PluginRepositoryDialog", "Plugin Repository"))
        self.repositoryList.setSortingEnabled(True)
        self.repositoryList.headerItem().setText(0, _translate("PluginRepositoryDialog", "Name"))
        self.repositoryList.headerItem().setText(1, _translate("PluginRepositoryDialog", "Version"))
        self.repositoryList.headerItem().setText(2, _translate("PluginRepositoryDialog", "Short Description"))
        self.label_2.setText(_translate("PluginRepositoryDialog", "Description:"))
        self.descriptionEdit.setToolTip(_translate("PluginRepositoryDialog", "Displays the description of the selected plugin"))
        self.label_3.setText(_translate("PluginRepositoryDialog", "Author:"))
        self.authorEdit.setToolTip(_translate("PluginRepositoryDialog", "Displays the author of the selected plugin"))
        self.label.setText(_translate("PluginRepositoryDialog", "URL:"))
        self.urlEdit.setToolTip(_translate("PluginRepositoryDialog", "Displays the download URL of the selected plugin"))
        self.downloadProgress.setToolTip(_translate("PluginRepositoryDialog", "Shows the progress of the current download"))
        self.label_4.setText(_translate("PluginRepositoryDialog", "Repository URL:"))
        self.repositoryUrlEdit.setToolTip(_translate("PluginRepositoryDialog", "Shows the repository URL"))
        self.repositoryUrlEditButton.setToolTip(_translate("PluginRepositoryDialog", "Press to edit the plugin repository URL"))
        self.repositoryUrlEditButton.setText(_translate("PluginRepositoryDialog", "Edit URL"))

