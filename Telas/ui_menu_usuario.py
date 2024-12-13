# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuKLZGQj.ui'
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
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from Telas.scr import user_resource

class Ui_Usuario(object):
    def setupUi(self, Usuario):
        if not Usuario.objectName():
            Usuario.setObjectName(u"Usuario")
        Usuario.resize(826, 600)
        Usuario.setAnimated(True)
        self.centralwidget = QWidget(Usuario)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.apenasIcone = QWidget(self.centralwidget)
        self.apenasIcone.setObjectName(u"apenasIcone")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apenasIcone.sizePolicy().hasHeightForWidth())
        self.apenasIcone.setSizePolicy(sizePolicy)
        self.apenasIcone.setMaximumSize(QSize(75, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.apenasIcone)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.apenasIcone)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icon/icon/computador.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_perfil = QPushButton(self.apenasIcone)
        self.btn_perfil.setObjectName(u"btn_perfil")
        icon = QIcon()
        icon.addFile(u":/icon/icon/vecteezy_user-profile-icon-profile-avatar-user-icon-male-icon_20911739.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_perfil.setIcon(icon)
        self.btn_perfil.setIconSize(QSize(30, 30))
        self.btn_perfil.setCheckable(True)
        self.btn_perfil.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_perfil)

        self.btn_chamado = QPushButton(self.apenasIcone)
        self.btn_chamado.setObjectName(u"btn_chamado")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/user-interface.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_chamado.setIcon(icon1)
        self.btn_chamado.setIconSize(QSize(30, 30))
        self.btn_chamado.setCheckable(True)
        self.btn_chamado.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_chamado)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 393, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_3 = QPushButton(self.apenasIcone)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/sair.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.gridLayout.addWidget(self.apenasIcone, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.pushButton_7.setIcon(icon3)
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(False)

        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.iconeEnome = QWidget(self.centralwidget)
        self.iconeEnome.setObjectName(u"iconeEnome")
        self.verticalLayout_4 = QVBoxLayout(self.iconeEnome)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.iconeEnome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/icon/icon/computador.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_perfil_aberto = QPushButton(self.iconeEnome)
        self.btn_perfil_aberto.setObjectName(u"btn_perfil_aberto")
        self.btn_perfil_aberto.setMinimumSize(QSize(0, 40))
        self.btn_perfil_aberto.setIcon(icon)
        self.btn_perfil_aberto.setIconSize(QSize(20, 20))
        self.btn_perfil_aberto.setCheckable(True)
        self.btn_perfil_aberto.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_perfil_aberto)

        self.btn_chamados_aberto = QPushButton(self.iconeEnome)
        self.btn_chamados_aberto.setObjectName(u"btn_chamados_aberto")
        self.btn_chamados_aberto.setMinimumSize(QSize(0, 40))
        self.btn_chamados_aberto.setIcon(icon1)
        self.btn_chamados_aberto.setIconSize(QSize(20, 20))
        self.btn_chamados_aberto.setCheckable(True)
        self.btn_chamados_aberto.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_chamados_aberto)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 387, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_6 = QPushButton(self.iconeEnome)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 40))
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(20, 20))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.iconeEnome, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pgPerfil = QWidget()
        self.pgPerfil.setObjectName(u"pgPerfil")
        self.frame = QFrame(self.pgPerfil)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(200, 100, 214, 294))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
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

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_8)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_7.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.pgPerfil)
        self.pgChamados = QWidget()
        self.pgChamados.setObjectName(u"pgChamados")
        self.tableWidget = QTableWidget(self.pgChamados)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(180, 330, 411, 231))
        self.stackedWidget.addWidget(self.pgChamados)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 3, 1, 1)

        Usuario.setCentralWidget(self.centralwidget)

        self.retranslateUi(Usuario)
        self.pushButton_7.toggled.connect(self.apenasIcone.setVisible)
        self.pushButton_7.toggled.connect(self.iconeEnome.setHidden)
        self.pushButton_3.clicked.connect(Usuario.close)
        self.pushButton_6.clicked.connect(Usuario.close)
        self.btn_perfil.toggled.connect(self.btn_perfil_aberto.setChecked)
        self.btn_chamado.toggled.connect(self.btn_chamados_aberto.setChecked)
        self.pushButton_3.toggled.connect(self.pushButton_6.setChecked)
        self.btn_perfil_aberto.toggled.connect(self.btn_perfil.setChecked)
        self.btn_chamados_aberto.toggled.connect(self.btn_chamado.setChecked)
        self.pushButton_6.toggled.connect(self.pushButton_3.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Usuario)
    # setupUi

    def retranslateUi(self, Usuario):
        Usuario.setWindowTitle(QCoreApplication.translate("Usuario", u"Usuario", None))
        self.label.setText("")
        self.btn_perfil.setText("")
        self.btn_chamado.setText("")
        self.pushButton_3.setText("")
        self.pushButton_7.setText("")
        self.label_2.setText("")
        self.btn_perfil_aberto.setText(QCoreApplication.translate("Usuario", u"Perfil", None))
        self.btn_chamados_aberto.setText(QCoreApplication.translate("Usuario", u"chamados", None))
        self.pushButton_6.setText(QCoreApplication.translate("Usuario", u"Sair", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("Usuario", u"login", None))
        self.label_7.setText(QCoreApplication.translate("Usuario", u"Nome", None))
        self.label_5.setText(QCoreApplication.translate("Usuario", u"E-mail", None))
        self.label_6.setText(QCoreApplication.translate("Usuario", u"cargo", None))
        self.label_8.setText(QCoreApplication.translate("Usuario", u"setor", None))
        self.pushButton_2.setText(QCoreApplication.translate("Usuario", u"Editar", None))
        self.pushButton.setText(QCoreApplication.translate("Usuario", u"Logoff", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Usuario", u"Status", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Usuario", u"Titulo", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Usuario", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Usuario", u"Data de abertura", None));
    # retranslateUi

