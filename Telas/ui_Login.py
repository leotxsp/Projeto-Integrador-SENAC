# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginoHsqRI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(300, 500)
        login.setMinimumSize(QSize(150, 500))
        login.setMaximumSize(QSize(300, 500))
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.BtnEntrar = QPushButton(self.centralwidget)
        self.BtnEntrar.setObjectName(u"BtnEntrar")
        self.BtnEntrar.setGeometry(QRect(80, 270, 131, 41))
        self.BtnEntrar.setStyleSheet(u"color: rgb(47, 47, 47);\n"
"background-color: rgb(243, 134, 2);\n"
"font: 14pt \"Impact\";\n"
"border-radius:12;")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(40, 130, 222, 96))
        self.frame_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.edtUsuario = QLineEdit(self.frame_2)
        self.edtUsuario.setObjectName(u"edtUsuario")

        self.gridLayout.addWidget(self.edtUsuario, 0, 2, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(14)
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(10, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.edtSenha = QLineEdit(self.frame)
        self.edtSenha.setObjectName(u"edtSenha")

        self.horizontalLayout.addWidget(self.edtSenha)


        self.verticalLayout.addWidget(self.frame)

        self.validou = QLabel(self.centralwidget)
        self.validou.setObjectName(u"validou")
        self.validou.setGeometry(QRect(30, 30, 241, 41))
        self.validou.setFont(font)
        self.validou.setStyleSheet(u"")
        self.validou.setAlignment(Qt.AlignmentFlag.AlignCenter)
        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Login", None))
        self.BtnEntrar.setText(QCoreApplication.translate("login", u"Entrar", None))
#if QT_CONFIG(shortcut)
        self.BtnEntrar.setShortcut(QCoreApplication.translate("login", u"Return, Enter", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("login", u"Usuario", None))
        self.label.setText(QCoreApplication.translate("login", u"Senha", None))
        self.validou.setText("")
    # retranslateUi

