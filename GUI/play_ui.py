# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hughd/Documents/python/SudokuSolver/SudokuAgent/GUI/play.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Play(object):
    def setupUi(self, Play):
        Play.setObjectName("Play")
        Play.resize(689, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Play.sizePolicy().hasHeightForWidth())
        Play.setSizePolicy(sizePolicy)
        Play.setAutoFillBackground(False)
        Play.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Play)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.topmiddle = QtWidgets.QTableWidget(Play)
        self.topmiddle.setRowCount(3)
        self.topmiddle.setColumnCount(3)
        self.topmiddle.setObjectName("topmiddle")
        self.topmiddle.horizontalHeader().setVisible(False)
        self.topmiddle.horizontalHeader().setDefaultSectionSize(30)
        self.topmiddle.horizontalHeader().setMinimumSectionSize(23)
        self.topmiddle.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.topmiddle, 0, 1, 1, 1)
        self.topright = QtWidgets.QTableWidget(Play)
        self.topright.setRowCount(3)
        self.topright.setColumnCount(3)
        self.topright.setObjectName("topright")
        self.topright.horizontalHeader().setVisible(False)
        self.topright.horizontalHeader().setDefaultSectionSize(30)
        self.topright.horizontalHeader().setMinimumSectionSize(23)
        self.topright.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.topright, 0, 2, 1, 1)
        self.middleleft = QtWidgets.QTableWidget(Play)
        self.middleleft.setRowCount(3)
        self.middleleft.setColumnCount(3)
        self.middleleft.setObjectName("middleleft")
        self.middleleft.horizontalHeader().setVisible(False)
        self.middleleft.horizontalHeader().setDefaultSectionSize(30)
        self.middleleft.horizontalHeader().setMinimumSectionSize(23)
        self.middleleft.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.middleleft, 1, 0, 1, 1)
        self.middlemiddle = QtWidgets.QTableWidget(Play)
        self.middlemiddle.setRowCount(3)
        self.middlemiddle.setColumnCount(3)
        self.middlemiddle.setObjectName("middlemiddle")
        self.middlemiddle.horizontalHeader().setVisible(False)
        self.middlemiddle.horizontalHeader().setDefaultSectionSize(30)
        self.middlemiddle.horizontalHeader().setMinimumSectionSize(23)
        self.middlemiddle.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.middlemiddle, 1, 1, 1, 1)
        self.middleright = QtWidgets.QTableWidget(Play)
        self.middleright.setRowCount(3)
        self.middleright.setColumnCount(3)
        self.middleright.setObjectName("middleright")
        self.middleright.horizontalHeader().setVisible(False)
        self.middleright.horizontalHeader().setDefaultSectionSize(30)
        self.middleright.horizontalHeader().setMinimumSectionSize(23)
        self.middleright.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.middleright, 1, 2, 1, 1)
        self.topleft = QtWidgets.QTableWidget(Play)
        self.topleft.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topleft.sizePolicy().hasHeightForWidth())
        self.topleft.setSizePolicy(sizePolicy)
        self.topleft.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.topleft.setLineWidth(1)
        self.topleft.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.topleft.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.topleft.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.topleft.setAutoScroll(True)
        self.topleft.setAutoScrollMargin(16)
        self.topleft.setAlternatingRowColors(True)
        self.topleft.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.topleft.setShowGrid(True)
        self.topleft.setGridStyle(QtCore.Qt.SolidLine)
        self.topleft.setWordWrap(True)
        self.topleft.setCornerButtonEnabled(True)
        self.topleft.setRowCount(3)
        self.topleft.setColumnCount(3)
        self.topleft.setObjectName("topleft")
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(125, 125, 125))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.topleft.setItem(0, 0, item)
        self.topleft.horizontalHeader().setVisible(False)
        self.topleft.horizontalHeader().setCascadingSectionResizes(False)
        self.topleft.horizontalHeader().setDefaultSectionSize(30)
        self.topleft.horizontalHeader().setHighlightSections(True)
        self.topleft.horizontalHeader().setMinimumSectionSize(23)
        self.topleft.horizontalHeader().setSortIndicatorShown(False)
        self.topleft.horizontalHeader().setStretchLastSection(False)
        self.topleft.verticalHeader().setVisible(False)
        self.topleft.verticalHeader().setCascadingSectionResizes(False)
        self.topleft.verticalHeader().setDefaultSectionSize(30)
        self.topleft.verticalHeader().setHighlightSections(True)
        self.topleft.verticalHeader().setMinimumSectionSize(21)
        self.topleft.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.topleft, 0, 0, 1, 1)
        self.bottomleft = QtWidgets.QTableWidget(Play)
        self.bottomleft.setRowCount(3)
        self.bottomleft.setColumnCount(3)
        self.bottomleft.setObjectName("bottomleft")
        self.bottomleft.horizontalHeader().setVisible(False)
        self.bottomleft.horizontalHeader().setDefaultSectionSize(30)
        self.bottomleft.horizontalHeader().setMinimumSectionSize(23)
        self.bottomleft.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.bottomleft, 2, 0, 1, 1)
        self.bottommiddle = QtWidgets.QTableWidget(Play)
        self.bottommiddle.setRowCount(3)
        self.bottommiddle.setColumnCount(3)
        self.bottommiddle.setObjectName("bottommiddle")
        self.bottommiddle.horizontalHeader().setVisible(False)
        self.bottommiddle.horizontalHeader().setDefaultSectionSize(30)
        self.bottommiddle.horizontalHeader().setMinimumSectionSize(23)
        self.bottommiddle.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.bottommiddle, 2, 1, 1, 1)
        self.bottomright = QtWidgets.QTableWidget(Play)
        self.bottomright.setRowCount(3)
        self.bottomright.setColumnCount(3)
        self.bottomright.setObjectName("bottomright")
        self.bottomright.horizontalHeader().setVisible(False)
        self.bottomright.horizontalHeader().setDefaultSectionSize(30)
        self.bottomright.horizontalHeader().setMinimumSectionSize(23)
        self.bottomright.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.bottomright, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_btn = QtWidgets.QPushButton(Play)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.check_btn = QtWidgets.QPushButton(Play)
        self.check_btn.setObjectName("check_btn")
        self.horizontalLayout.addWidget(self.check_btn)
        self.new_btn = QtWidgets.QPushButton(Play)
        self.new_btn.setObjectName("new_btn")
        self.horizontalLayout.addWidget(self.new_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Play)
        QtCore.QMetaObject.connectSlotsByName(Play)

    def retranslateUi(self, Play):
        _translate = QtCore.QCoreApplication.translate
        Play.setWindowTitle(_translate("Play", "PyDoku Player"))
        self.topleft.setSortingEnabled(False)
        __sortingEnabled = self.topleft.isSortingEnabled()
        self.topleft.setSortingEnabled(False)
        self.topleft.setSortingEnabled(__sortingEnabled)
        self.cancel_btn.setText(_translate("Play", "Cancel"))
        self.check_btn.setText(_translate("Play", "Check"))
        self.new_btn.setText(_translate("Play", "New Puzzle"))
