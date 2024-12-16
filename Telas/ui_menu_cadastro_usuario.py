# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu_cadastro_usuarioVZquTd.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from Telas.scr import user_resource_rc

class Ui_cadastroUsuario(object):
    def setupUi(self, cadastroUsuario):
        if not cadastroUsuario.objectName():
            cadastroUsuario.setObjectName(u"cadastroUsuario")
        cadastroUsuario.resize(500, 600)
        cadastroUsuario.setMaximumSize(QSize(500, 600))
        self.centralwidget = QWidget(cadastroUsuario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(100, 100))
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setPixmap(QPixmap(u":/icon/icon/user proile.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.CB_Setor = QComboBox(self.frame)
        self.CB_Setor.setObjectName(u"CB_Setor")
        self.CB_Setor.setMinimumSize(QSize(0, 25))
        self.CB_Setor.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.CB_Setor, 6, 2, 1, 1)

        self.LB_cargo = QLabel(self.frame)
        self.LB_cargo.setObjectName(u"LB_cargo")
        self.LB_cargo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.LB_cargo, 5, 1, 1, 1)

        self.LEnome = QLineEdit(self.frame)
        self.LEnome.setObjectName(u"LEnome")
        self.LEnome.setMinimumSize(QSize(0, 25))
        self.LEnome.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.LEnome, 3, 2, 1, 1)

        self.LEsenha = QLineEdit(self.frame)
        self.LEsenha.setObjectName(u"LEsenha")
        self.LEsenha.setMinimumSize(QSize(0, 25))
        self.LEsenha.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.LEsenha, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.LB_setor = QLabel(self.frame)
        self.LB_setor.setObjectName(u"LB_setor")
        self.LB_setor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.LB_setor, 6, 1, 1, 1)

        self.CB_Cargo = QComboBox(self.frame)
        self.CB_Cargo.setObjectName(u"CB_Cargo")
        self.CB_Cargo.setMinimumSize(QSize(0, 25))
        self.CB_Cargo.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.CB_Cargo, 5, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.LB_email = QLabel(self.frame)
        self.LB_email.setObjectName(u"LB_email")
        self.LB_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.LB_email, 4, 1, 1, 1)

        self.LEconfirmarSenha = QLineEdit(self.frame)
        self.LEconfirmarSenha.setObjectName(u"LEconfirmarSenha")
        self.LEconfirmarSenha.setMinimumSize(QSize(0, 25))
        self.LEconfirmarSenha.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.LEconfirmarSenha, 2, 2, 1, 1)

        self.LEemail = QLineEdit(self.frame)
        self.LEemail.setObjectName(u"LEemail")
        self.LEemail.setMinimumSize(QSize(0, 25))
        self.LEemail.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.LEemail, 4, 2, 1, 1)

        self.LB_login = QLabel(self.frame)
        self.LB_login.setObjectName(u"LB_login")
        self.LB_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.LB_login, 0, 1, 1, 1)

        self.LB_email_2 = QLabel(self.frame)
        self.LB_email_2.setObjectName(u"LB_email_2")
        self.LB_email_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.LB_email_2, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.LElogin = QLineEdit(self.frame)
        self.LElogin.setObjectName(u"LElogin")
        self.LElogin.setMinimumSize(QSize(40, 25))
        self.LElogin.setMaximumSize(QSize(150, 25))

        self.gridLayout.addWidget(self.LElogin, 0, 2, 1, 1)

        self.BTcadastrar = QPushButton(self.frame)
        self.BTcadastrar.setObjectName(u"BTcadastrar")

        self.gridLayout.addWidget(self.BTcadastrar, 7, 1, 1, 2)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        cadastroUsuario.setCentralWidget(self.centralwidget)

        self.retranslateUi(cadastroUsuario)

        QMetaObject.connectSlotsByName(cadastroUsuario)
    # setupUi

    def retranslateUi(self, cadastroUsuario):
        cadastroUsuario.setWindowTitle(QCoreApplication.translate("cadastroUsuario", u"Cadastro", None))
        self.label_4.setText("")
        self.LB_cargo.setText(QCoreApplication.translate("cadastroUsuario", u"cargo:", None))
        self.label_2.setText(QCoreApplication.translate("cadastroUsuario", u"confirmar senha", None))
        self.LB_setor.setText(QCoreApplication.translate("cadastroUsuario", u"setor:", None))
        self.label.setText(QCoreApplication.translate("cadastroUsuario", u"senha:", None))
        self.LB_email.setText(QCoreApplication.translate("cadastroUsuario", u"E-mail", None))
        self.LB_login.setText(QCoreApplication.translate("cadastroUsuario", u"login", None))
        self.LB_email_2.setText(QCoreApplication.translate("cadastroUsuario", u"Nome", None))
        self.BTcadastrar.setText(QCoreApplication.translate("cadastroUsuario", u"Cadastrar", None))
    # retranslateUi

