# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuDWUGhI.ui'
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from Telas.scr import user_resource_rc

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

        self.btn_usuarios = QPushButton(self.iconeEnome)
        self.btn_usuarios.setObjectName(u"btn_usuarios")
        self.btn_usuarios.setMinimumSize(QSize(0, 40))
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/user-interface.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_usuarios.setIcon(icon1)
        self.btn_usuarios.setIconSize(QSize(20, 20))
        self.btn_usuarios.setCheckable(True)
        self.btn_usuarios.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_usuarios)

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
        self.pgUsuarios = QWidget()
        self.pgUsuarios.setObjectName(u"pgUsuarios")
        self.gridLayout_2 = QGridLayout(self.pgUsuarios)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget = QTableWidget(self.pgUsuarios)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 4)

        self.BtnCadastrarUsuario = QPushButton(self.pgUsuarios)
        self.BtnCadastrarUsuario.setObjectName(u"BtnCadastrarUsuario")

        self.gridLayout_2.addWidget(self.BtnCadastrarUsuario, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(189, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(189, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.BtnAtualizarUsuario = QPushButton(self.pgUsuarios)
        self.BtnAtualizarUsuario.setObjectName(u"BtnAtualizarUsuario")

        self.gridLayout_2.addWidget(self.BtnAtualizarUsuario, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.pgUsuarios)
        self.pgChamados = QWidget()
        self.pgChamados.setObjectName(u"pgChamados")
        self.gridLayout_4 = QGridLayout(self.pgChamados)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.BtnFecharChamado = QPushButton(self.pgChamados)
        self.BtnFecharChamado.setObjectName(u"BtnFecharChamado")

        self.gridLayout_4.addWidget(self.BtnFecharChamado, 2, 2, 1, 1)

        self.BtnAlterarChamado = QPushButton(self.pgChamados)
        self.BtnAlterarChamado.setObjectName(u"BtnAlterarChamado")

        self.gridLayout_4.addWidget(self.BtnAlterarChamado, 2, 3, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.pgChamados)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.lineEdit_2 = QLineEdit(self.pgChamados)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_7.addWidget(self.lineEdit_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.pgChamados)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.gridLayout_4.addWidget(self.widget_2, 0, 1, 2, 3)

        self.TB_Chamados_usuario = QTableWidget(self.pgChamados)
        if (self.TB_Chamados_usuario.columnCount() < 10):
            self.TB_Chamados_usuario.setColumnCount(10)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.TB_Chamados_usuario.setHorizontalHeaderItem(9, __qtablewidgetitem16)
        self.TB_Chamados_usuario.setObjectName(u"TB_Chamados_usuario")

        self.gridLayout_4.addWidget(self.TB_Chamados_usuario, 3, 0, 1, 4)

        self.BtnAbrirChamado = QPushButton(self.pgChamados)
        self.BtnAbrirChamado.setObjectName(u"BtnAbrirChamado")

        self.gridLayout_4.addWidget(self.BtnAbrirChamado, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.pgChamados)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        tecnico.setCentralWidget(self.centralwidget)

        self.retranslateUi(tecnico)
        self.pushButton_7.toggled.connect(self.iconeEnome.setHidden)
        self.pushButton_6.clicked.connect(tecnico.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(tecnico)
    # setupUi

    def retranslateUi(self, tecnico):
        tecnico.setWindowTitle(QCoreApplication.translate("tecnico", u"Tecnico", None))
        self.label_2.setText("")
        self.btn_perfil_aberto.setText(QCoreApplication.translate("tecnico", u"Perfil", None))
        self.btn_usuarios.setText(QCoreApplication.translate("tecnico", u"gerenciar usuarios", None))
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
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tecnico", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tecnico", u"USUARIO", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tecnico", u"EMAIL", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tecnico", u"SENHA", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("tecnico", u"NOME", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("tecnico", u"SETOR", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("tecnico", u"CARGO", None));
        self.BtnCadastrarUsuario.setText(QCoreApplication.translate("tecnico", u"Cadastrar", None))
        self.BtnAtualizarUsuario.setText(QCoreApplication.translate("tecnico", u"ATUALIZAR", None))
        self.BtnFecharChamado.setText(QCoreApplication.translate("tecnico", u"fechar", None))
        self.BtnAlterarChamado.setText(QCoreApplication.translate("tecnico", u"Alterar", None))
        self.pushButton_2.setText(QCoreApplication.translate("tecnico", u"procurar", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("tecnico", u"Enter, Return", None))
#endif // QT_CONFIG(shortcut)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("tecnico", u"Procurar", None))
        ___qtablewidgetitem7 = self.TB_Chamados_usuario.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("tecnico", u"ID", None));
        ___qtablewidgetitem8 = self.TB_Chamados_usuario.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("tecnico", u"Status", None));
        ___qtablewidgetitem9 = self.TB_Chamados_usuario.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("tecnico", u"Prioridade", None));
        ___qtablewidgetitem10 = self.TB_Chamados_usuario.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("tecnico", u"Servi\u00e7o", None));
        ___qtablewidgetitem11 = self.TB_Chamados_usuario.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("tecnico", u"Titulo", None));
        ___qtablewidgetitem12 = self.TB_Chamados_usuario.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("tecnico", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem13 = self.TB_Chamados_usuario.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("tecnico", u"Usuario/abertura", None));
        ___qtablewidgetitem14 = self.TB_Chamados_usuario.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("tecnico", u"Usuario/fechamento", None));
        ___qtablewidgetitem15 = self.TB_Chamados_usuario.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("tecnico", u"Data de abertura", None));
        ___qtablewidgetitem16 = self.TB_Chamados_usuario.horizontalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("tecnico", u"Data de fechamento", None));
        self.BtnAbrirChamado.setText(QCoreApplication.translate("tecnico", u"Abrir", None))
    # retranslateUi

