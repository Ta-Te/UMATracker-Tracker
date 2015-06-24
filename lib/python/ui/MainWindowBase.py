# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindowBase.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowBase(object):
    def setupUi(self, MainWindowBase):
        MainWindowBase.setObjectName("MainWindowBase")
        MainWindowBase.resize(592, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindowBase)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setObjectName("gridWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gridWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsBox = QtWidgets.QGroupBox(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.graphicsBox.sizePolicy().hasHeightForWidth())
        self.graphicsBox.setSizePolicy(sizePolicy)
        self.graphicsBox.setObjectName("graphicsBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.graphicsBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.inputGraphicsView = QtWidgets.QGraphicsView(self.graphicsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.inputGraphicsView.sizePolicy().hasHeightForWidth())
        self.inputGraphicsView.setSizePolicy(sizePolicy)
        self.inputGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputGraphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.inputGraphicsView.setObjectName("inputGraphicsView")
        self.verticalLayout_6.addWidget(self.inputGraphicsView)
        self.videoPlaybackWidget = QtWidgets.QWidget(self.graphicsBox)
        self.videoPlaybackWidget.setObjectName("videoPlaybackWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.videoPlaybackWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.videoPlaybackButtons = QtWidgets.QHBoxLayout()
        self.videoPlaybackButtons.setObjectName("videoPlaybackButtons")
        self.videoGoHeadButton = QtWidgets.QPushButton(self.videoPlaybackWidget)
        self.videoGoHeadButton.setObjectName("videoGoHeadButton")
        self.videoPlaybackButtons.addWidget(self.videoGoHeadButton)
        self.videoGoBackwardButton = QtWidgets.QPushButton(self.videoPlaybackWidget)
        self.videoGoBackwardButton.setObjectName("videoGoBackwardButton")
        self.videoPlaybackButtons.addWidget(self.videoGoBackwardButton)
        self.videoPlayStopButton = QtWidgets.QPushButton(self.videoPlaybackWidget)
        self.videoPlayStopButton.setObjectName("videoPlayStopButton")
        self.videoPlaybackButtons.addWidget(self.videoPlayStopButton)
        self.videoGoForwardButton = QtWidgets.QPushButton(self.videoPlaybackWidget)
        self.videoGoForwardButton.setObjectName("videoGoForwardButton")
        self.videoPlaybackButtons.addWidget(self.videoGoForwardButton)
        self.videoGoLastButton = QtWidgets.QPushButton(self.videoPlaybackWidget)
        self.videoGoLastButton.setObjectName("videoGoLastButton")
        self.videoPlaybackButtons.addWidget(self.videoGoLastButton)
        self.verticalLayout_7.addLayout(self.videoPlaybackButtons)
        self.videoPlaybackSlider = QtWidgets.QSlider(self.videoPlaybackWidget)
        self.videoPlaybackSlider.setOrientation(QtCore.Qt.Horizontal)
        self.videoPlaybackSlider.setObjectName("videoPlaybackSlider")
        self.verticalLayout_7.addWidget(self.videoPlaybackSlider)
        self.verticalLayout_6.addWidget(self.videoPlaybackWidget)
        self.outputGraphicsView = QtWidgets.QGraphicsView(self.graphicsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.outputGraphicsView.sizePolicy().hasHeightForWidth())
        self.outputGraphicsView.setSizePolicy(sizePolicy)
        self.outputGraphicsView.setObjectName("outputGraphicsView")
        self.verticalLayout_6.addWidget(self.outputGraphicsView)
        self.horizontalLayout.addWidget(self.graphicsBox)
        self.groupBox = QtWidgets.QGroupBox(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.clusteringMethodComboBox = QtWidgets.QComboBox(self.groupBox)
        self.clusteringMethodComboBox.setObjectName("clusteringMethodComboBox")
        self.clusteringMethodComboBox.addItem("")
        self.clusteringMethodComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.clusteringMethodComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.clusterSizeNumSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.clusterSizeNumSpinBox.setMinimum(1)
        self.clusterSizeNumSpinBox.setObjectName("clusterSizeNumSpinBox")
        self.horizontalLayout_2.addWidget(self.clusterSizeNumSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.cpuCoreNumSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.cpuCoreNumSpinBox.setMinimum(1)
        self.cpuCoreNumSpinBox.setObjectName("cpuCoreNumSpinBox")
        self.horizontalLayout_4.addWidget(self.cpuCoreNumSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(self.gridWidget, 0, 0, 1, 1)
        MainWindowBase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowBase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        MainWindowBase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowBase)
        self.statusbar.setObjectName("statusbar")
        MainWindowBase.setStatusBar(self.statusbar)
        self.actionOpenVideo = QtWidgets.QAction(MainWindowBase)
        self.actionOpenVideo.setObjectName("actionOpenVideo")
        self.actionOpenImage = QtWidgets.QAction(MainWindowBase)
        self.actionOpenImage.setObjectName("actionOpenImage")
        self.actionOpenFilterSetting = QtWidgets.QAction(MainWindowBase)
        self.actionOpenFilterSetting.setObjectName("actionOpenFilterSetting")
        self.actionSaveBlockData = QtWidgets.QAction(MainWindowBase)
        self.actionSaveBlockData.setObjectName("actionSaveBlockData")
        self.actionQuit = QtWidgets.QAction(MainWindowBase)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFiles.addAction(self.actionOpenVideo)
        self.menuFiles.addAction(self.actionOpenImage)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionOpenFilterSetting)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindowBase)
        self.actionQuit.triggered.connect(MainWindowBase.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindowBase)

    def retranslateUi(self, MainWindowBase):
        _translate = QtCore.QCoreApplication.translate
        MainWindowBase.setWindowTitle(_translate("MainWindowBase", "MainWindow"))
        self.graphicsBox.setTitle(_translate("MainWindowBase", "Object Tracking"))
        self.videoGoHeadButton.setText(_translate("MainWindowBase", "<<"))
        self.videoGoBackwardButton.setText(_translate("MainWindowBase", "<"))
        self.videoPlayStopButton.setText(_translate("MainWindowBase", "Play/Stop"))
        self.videoGoForwardButton.setText(_translate("MainWindowBase", ">"))
        self.videoGoLastButton.setText(_translate("MainWindowBase", ">>"))
        self.groupBox.setTitle(_translate("MainWindowBase", "Settings"))
        self.label_3.setText(_translate("MainWindowBase", "Method:"))
        self.clusteringMethodComboBox.setItemText(0, _translate("MainWindowBase", "K-means"))
        self.clusteringMethodComboBox.setItemText(1, _translate("MainWindowBase", "GMM"))
        self.label.setText(_translate("MainWindowBase", "Cluster size:"))
        self.label_2.setText(_translate("MainWindowBase", "CPU Core:"))
        self.menuFiles.setTitle(_translate("MainWindowBase", "Files"))
        self.actionOpenVideo.setText(_translate("MainWindowBase", "Open Video"))
        self.actionOpenImage.setText(_translate("MainWindowBase", "Open Image"))
        self.actionOpenFilterSetting.setText(_translate("MainWindowBase", "Open Filter Setting"))
        self.actionSaveBlockData.setText(_translate("MainWindowBase", "Save Block Data"))
        self.actionQuit.setText(_translate("MainWindowBase", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindowBase", "Ctrl+Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowBase = QtWidgets.QMainWindow()
    ui = Ui_MainWindowBase()
    ui.setupUi(MainWindowBase)
    MainWindowBase.show()
    sys.exit(app.exec_())

