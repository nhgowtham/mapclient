# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapclient/view/managers/options/qt/optionsdialog.ui'
#
# Created: Mon Mar  5 13:03:19 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_OptionsDialog(object):
    def setupUi(self, OptionsDialog):
        OptionsDialog.setObjectName("OptionsDialog")
        OptionsDialog.resize(525, 579)
        self.gridLayout = QtGui.QGridLayout(OptionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(OptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(OptionsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGeneral = QtGui.QWidget()
        self.tabGeneral.setObjectName("tabGeneral")
        self.gridLayout_3 = QtGui.QGridLayout(self.tabGeneral)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        self.checkBoxShowStepNames = QtGui.QCheckBox(self.tabGeneral)
        self.checkBoxShowStepNames.setChecked(True)
        self.checkBoxShowStepNames.setObjectName("checkBoxShowStepNames")
        self.gridLayout_3.addWidget(self.checkBoxShowStepNames, 0, 0, 1, 1)
        self.checkBoxCheckToolsOnStartup = QtGui.QCheckBox(self.tabGeneral)
        self.checkBoxCheckToolsOnStartup.setChecked(True)
        self.checkBoxCheckToolsOnStartup.setObjectName("checkBoxCheckToolsOnStartup")
        self.gridLayout_3.addWidget(self.checkBoxCheckToolsOnStartup, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabToolSettings = QtGui.QWidget()
        self.tabToolSettings.setObjectName("tabToolSettings")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabToolSettings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtGui.QGroupBox(self.tabToolSettings)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelVirtualEnvironmentPath = QtGui.QLabel(self.groupBox_3)
        self.labelVirtualEnvironmentPath.setObjectName("labelVirtualEnvironmentPath")
        self.gridLayout_4.addWidget(self.labelVirtualEnvironmentPath, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditVirtualEnvironmentPath = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVirtualEnvironmentPath.sizePolicy().hasHeightForWidth())
        self.lineEditVirtualEnvironmentPath.setSizePolicy(sizePolicy)
        self.lineEditVirtualEnvironmentPath.setObjectName("lineEditVirtualEnvironmentPath")
        self.horizontalLayout_2.addWidget(self.lineEditVirtualEnvironmentPath)
        self.pushButtonVirtualEnvironmentPath = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonVirtualEnvironmentPath.setObjectName("pushButtonVirtualEnvironmentPath")
        self.horizontalLayout_2.addWidget(self.pushButtonVirtualEnvironmentPath)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonCreate = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.horizontalLayout_4.addWidget(self.pushButtonCreate)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.tabToolSettings)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEditPySideRCC = QtGui.QLineEdit(self.groupBox_4)
        self.lineEditPySideRCC.setObjectName("lineEditPySideRCC")
        self.gridLayout_2.addWidget(self.lineEditPySideRCC, 0, 1, 1, 1)
        self.pushButtonPySideRCC = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonPySideRCC.setObjectName("pushButtonPySideRCC")
        self.gridLayout_2.addWidget(self.pushButtonPySideRCC, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.tabToolSettings)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBoxUseExternalGit = QtGui.QCheckBox(self.groupBox_5)
        self.checkBoxUseExternalGit.setObjectName("checkBoxUseExternalGit")
        self.verticalLayout_5.addWidget(self.checkBoxUseExternalGit)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelGitExecutable = QtGui.QLabel(self.groupBox_5)
        self.labelGitExecutable.setObjectName("labelGitExecutable")
        self.horizontalLayout_3.addWidget(self.labelGitExecutable)
        self.lineEditGitExecutable = QtGui.QLineEdit(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditGitExecutable.sizePolicy().hasHeightForWidth())
        self.lineEditGitExecutable.setSizePolicy(sizePolicy)
        self.lineEditGitExecutable.setObjectName("lineEditGitExecutable")
        self.horizontalLayout_3.addWidget(self.lineEditGitExecutable)
        self.pushButtonGitExecutable = QtGui.QPushButton(self.groupBox_5)
        self.pushButtonGitExecutable.setObjectName("pushButtonGitExecutable")
        self.horizontalLayout_3.addWidget(self.pushButtonGitExecutable)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox = QtGui.QGroupBox(self.tabToolSettings)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEditToolTestOutput = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEditToolTestOutput.setObjectName("plainTextEditToolTestOutput")
        self.verticalLayout.addWidget(self.plainTextEditToolTestOutput)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonRunChecks = QtGui.QPushButton(self.groupBox)
        self.pushButtonRunChecks.setObjectName("pushButtonRunChecks")
        self.horizontalLayout.addWidget(self.pushButtonRunChecks)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.tabWidget.addTab(self.tabToolSettings, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(OptionsDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), OptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), OptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialog)

    def retranslateUi(self, OptionsDialog):
        OptionsDialog.setWindowTitle(QtGui.QApplication.translate("OptionsDialog", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowStepNames.setText(QtGui.QApplication.translate("OptionsDialog", "Show step names", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCheckToolsOnStartup.setText(QtGui.QApplication.translate("OptionsDialog", "Check tools on application start", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), QtGui.QApplication.translate("OptionsDialog", "&General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("OptionsDialog", "Virtual Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.labelVirtualEnvironmentPath.setText(QtGui.QApplication.translate("OptionsDialog", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditVirtualEnvironmentPath.setToolTip(QtGui.QApplication.translate("OptionsDialog", "The virtual environment path has some restrictions, for instance it cannot have any spaces in it.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonVirtualEnvironmentPath.setText(QtGui.QApplication.translate("OptionsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCreate.setToolTip(QtGui.QApplication.translate("OptionsDialog", "Create a virtual environment at the virtual environment path", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCreate.setText(QtGui.QApplication.translate("OptionsDialog", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("OptionsDialog", "Step Wizard", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("OptionsDialog", "pyside-rcc", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPySideRCC.setToolTip(QtGui.QApplication.translate("OptionsDialog", "The PySide Resource Compiler executable.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPySideRCC.setText(QtGui.QApplication.translate("OptionsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("OptionsDialog", "PMR", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxUseExternalGit.setText(QtGui.QApplication.translate("OptionsDialog", "Use external Git", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGitExecutable.setText(QtGui.QApplication.translate("OptionsDialog", "Git:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditGitExecutable.setToolTip(QtGui.QApplication.translate("OptionsDialog", "The Git version control executable", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGitExecutable.setText(QtGui.QApplication.translate("OptionsDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("OptionsDialog", "Tool test output", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRunChecks.setText(QtGui.QApplication.translate("OptionsDialog", "Run Checks", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabToolSettings), QtGui.QApplication.translate("OptionsDialog", "Tool Settings", None, QtGui.QApplication.UnicodeUTF8))

