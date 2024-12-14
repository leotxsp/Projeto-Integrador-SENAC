# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu.tecnico.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import user_resource_rc


class Ui_tecnico(object):
    def setupUi(self, tecnico):
        if not tecnico.objectName():
            tecnico.setObjectName(u"tecnico")
        tecnico.resize(800, 599)
        self.centralwidget = QWidget(tecnico)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.iconeEnome = QWidget(self.widget)
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
        icon = QIcon()
        icon.addFile(u":/icon/icon/vecteezy_user-profile-icon-profile-avatar-user-icon-male-icon_20911739.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_perfil_aberto.setIcon(icon)
        self.btn_perfil_aberto.setIconSize(QSize(20, 20))
        self.btn_perfil_aberto.setCheckable(True)
        self.btn_perfil_aberto.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_perfil_aberto)

        self.btn_chamados_aberto_2 = QPushButton(self.iconeEnome)
        self.btn_chamados_aberto_2.setObjectName(u"btn_chamados_aberto_2")
        self.btn_chamados_aberto_2.setMinimumSize(QSize(0, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/user-interface.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_chamados_aberto_2.setIcon(icon1)
        self.btn_chamados_aberto_2.setIconSize(QSize(20, 20))
        self.btn_chamados_aberto_2.setCheckable(True)
        self.btn_chamados_aberto_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_chamados_aberto_2)

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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/sair.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(20, 20))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_6)


        self.horizontalLayout_6.addWidget(self.iconeEnome)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.pushButton_7.setIcon(icon3)
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pgPerfil = QWidget()
        self.pgPerfil.setObjectName(u"pgPerfil")
        self.gridLayout_3 = QGridLayout(self.pgPerfil)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_7 = QSpacerItem(20, 126, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.frame = QFrame(self.pgPerfil)
        self.frame.setObjectName(u"frame")
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

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.LB_login = QLabel(self.frame)
        self.LB_login.setObjectName(u"LB_login")
        self.LB_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.LB_login)

        self.LB_email_2 = QLabel(self.frame)
        self.LB_email_2.setObjectName(u"LB_email_2")
        self.LB_email_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.LB_email_2)

        self.LB_email = QLabel(self.frame)
        self.LB_email.setObjectName(u"LB_email")
        self.LB_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.LB_email)

        self.LB_cargo = QLabel(self.frame)
        self.LB_cargo.setObjectName(u"LB_cargo")
        self.LB_cargo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.LB_cargo)

        self.LB_setor = QLabel(self.frame)
        self.LB_setor.setObjectName(u"LB_setor")
        self.LB_setor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.LB_setor)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.BtnEditar = QPushButton(self.frame)
        self.BtnEditar.setObjectName(u"BtnEditar")

        self.verticalLayout_7.addWidget(self.BtnEditar)

        self.BtnLogoff = QPushButton(self.frame)
        self.BtnLogoff.setObjectName(u"BtnLogoff")

        self.verticalLayout_7.addWidget(self.BtnLogoff)


        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 2)

        self.horizontalSpacer_8 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 1, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 125, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pgPerfil)
        self.pgChamados = QWidget()
        self.pgChamados.setObjectName(u"pgChamados")
        self.TB_Chamados_usuario = QTableWidget(self.pgChamados)
        if (self.TB_Chamados_usuario.columnCount() < 4):
            self.TB_Chamados_usuario.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.TB_Chamados_usuario.setObjectName(u"TB_Chamados_usuario")
        self.TB_Chamados_usuario.setGeometry(QRect(10, 350, 581, 231))
        self.BtnAbrirChamado = QPushButton(self.pgChamados)
        self.BtnAbrirChamado.setObjectName(u"BtnAbrirChamado")
        self.BtnAbrirChamado.setGeometry(QRect(80, 80, 75, 24))
        self.BtnFecharChamado = QPushButton(self.pgChamados)
        self.BtnFecharChamado.setObjectName(u"BtnFecharChamado")
        self.BtnFecharChamado.setGeometry(QRect(80, 110, 75, 24))
        self.BtnAlterarChamado = QPushButton(self.pgChamados)
        self.BtnAlterarChamado.setObjectName(u"BtnAlterarChamado")
        self.BtnAlterarChamado.setGeometry(QRect(80, 140, 75, 24))
        self.widget_2 = QWidget(self.pgChamados)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(320, 60, 271, 251))
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 16777215))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.CBStatus = QComboBox(self.widget_2)
        self.CBStatus.setObjectName(u"CBStatus")
        self.CBStatus.setMinimumSize(QSize(150, 0))
        self.CBStatus.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.CBStatus)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(50, 16777215))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.horizontalSpacer_6 = QSpacerItem(5, 5, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.edtTitulo = QLineEdit(self.widget_2)
        self.edtTitulo.setObjectName(u"edtTitulo")

        self.horizontalLayout_5.addWidget(self.edtTitulo)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(50, 16777215))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11)

        self.verticalSpacer_3 = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.TEdescricao = QTextEdit(self.widget_2)
        self.TEdescricao.setObjectName(u"TEdescricao")

        self.verticalLayout_11.addWidget(self.TEdescricao)


        self.verticalLayout_10.addLayout(self.verticalLayout_11)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(50, 16777215))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_21)

        self.horizontalSpacer_11 = QSpacerItem(5, 5, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.dateEdit = QDateEdit(self.widget_2)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_11.addWidget(self.dateEdit)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.pgChamados)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        tecnico.setCentralWidget(self.centralwidget)

        self.retranslateUi(tecnico)
        self.pushButton_7.toggled.connect(self.iconeEnome.setHidden)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(tecnico)
    # setupUi

    def retranslateUi(self, tecnico):
        tecnico.setWindowTitle(QCoreApplication.translate("tecnico", u"Tecnico", None))
        self.label_2.setText("")
        self.btn_perfil_aberto.setText(QCoreApplication.translate("tecnico", u"Perfil", None))
        self.btn_chamados_aberto_2.setText(QCoreApplication.translate("tecnico", u"gerenciar usuarios", None))
        self.btn_chamados_aberto.setText(QCoreApplication.translate("tecnico", u"chamados", None))
        self.pushButton_6.setText(QCoreApplication.translate("tecnico", u"Sair", None))
        self.pushButton_7.setText("")
        self.label_4.setText("")
        self.LB_login.setText(QCoreApplication.translate("tecnico", u"login", None))
        self.LB_email_2.setText(QCoreApplication.translate("tecnico", u"Nome", None))
        self.LB_email.setText(QCoreApplication.translate("tecnico", u"E-mail", None))
        self.LB_cargo.setText(QCoreApplication.translate("tecnico", u"cargo", None))
        self.LB_setor.setText(QCoreApplication.translate("tecnico", u"setor", None))
        self.BtnEditar.setText(QCoreApplication.translate("tecnico", u"Editar", None))
        self.BtnLogoff.setText(QCoreApplication.translate("tecnico", u"Logoff", None))
        ___qtablewidgetitem = self.TB_Chamados_usuario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tecnico", u"Status", None));
        ___qtablewidgetitem1 = self.TB_Chamados_usuario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tecnico", u"Titulo", None));
        ___qtablewidgetitem2 = self.TB_Chamados_usuario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tecnico", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem3 = self.TB_Chamados_usuario.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tecnico", u"Data de abertura", None));
        self.BtnAbrirChamado.setText(QCoreApplication.translate("tecnico", u"Abrir", None))
        self.BtnFecharChamado.setText(QCoreApplication.translate("tecnico", u"fechar", None))
        self.BtnAlterarChamado.setText(QCoreApplication.translate("tecnico", u"Alterar", None))
        self.label_9.setText(QCoreApplication.translate("tecnico", u"Status", None))
        self.label_10.setText(QCoreApplication.translate("tecnico", u"Titulo", None))
        self.label_11.setText(QCoreApplication.translate("tecnico", u"Descri\u00e7\u00e3o", None))
        self.label_21.setText(QCoreApplication.translate("tecnico", u"Data", None))
    # retranslateUi

