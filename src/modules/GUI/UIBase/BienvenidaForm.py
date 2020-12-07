# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BienvenidaForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BienvenidaForm(object):
    def setupUi(self, BienvenidaForm):
        BienvenidaForm.setObjectName("BienvenidaForm")
        BienvenidaForm.setEnabled(True)
        BienvenidaForm.resize(530, 379)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BienvenidaForm.sizePolicy().hasHeightForWidth())
        BienvenidaForm.setSizePolicy(sizePolicy)
        BienvenidaForm.setMaximumSize(QtCore.QSize(610, 420))
        BienvenidaForm.setWindowOpacity(1.0)
        BienvenidaForm.setStyleSheet("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(BienvenidaForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Container = QtWidgets.QFrame(BienvenidaForm)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.Container.setFont(font)
        self.Container.setStyleSheet("QFrame#Container{\n"
"    background-color: #7D211A;\n"
"    border-radius: 10px;\n"
"}")
        self.Container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Container.setObjectName("Container")
        self.gridLayout = QtWidgets.QGridLayout(self.Container)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.Container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BtnCargar = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnCargar.sizePolicy().hasHeightForWidth())
        self.BtnCargar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.BtnCargar.setFont(font)
        self.BtnCargar.setStyleSheet("QPushButton{\n"
"background-color: #EF8903;\n"
"padding: 7px;\n"
"max-width: 300px;\n"
"border-style: outset;\n"
"border-radius: 16px;\n"
"color:  white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #C57000;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #A96000;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"")
        self.BtnCargar.setObjectName("BtnCargar")
        self.gridLayout_2.addWidget(self.BtnCargar, 2, 0, 1, 1)
        self.BtnNuevo = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.BtnNuevo.sizePolicy().hasHeightForWidth())
        self.BtnNuevo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.BtnNuevo.setFont(font)
        self.BtnNuevo.setStyleSheet("QPushButton{\n"
"background-color: #EF8903;\n"
"padding: 7px;\n"
"max-width: 300px;\n"
"border-style: outset;\n"
"border-radius: 16px;\n"
"color:  white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #C57000;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #A96000;\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.BtnNuevo.setFlat(False)
        self.BtnNuevo.setObjectName("BtnNuevo")
        self.gridLayout_2.addWidget(self.BtnNuevo, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.Container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.Container)

        self.retranslateUi(BienvenidaForm)
        QtCore.QMetaObject.connectSlotsByName(BienvenidaForm)

    def retranslateUi(self, BienvenidaForm):
        _translate = QtCore.QCoreApplication.translate
        BienvenidaForm.setWindowTitle(_translate("BienvenidaForm", "Bienvenido"))
        self.BtnCargar.setText(_translate("BienvenidaForm", "Cargar de Archivo"))
        self.BtnNuevo.setText(_translate("BienvenidaForm", "Nuevo "))
        self.label.setText(_translate("BienvenidaForm", "Bienvenido"))