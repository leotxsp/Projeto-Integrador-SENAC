# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_alterar_chamadoptUOCC.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AlterarCadastro(object):
    def setupUi(self, AlterarCadastro):
        if not AlterarCadastro.objectName():
            AlterarCadastro.setObjectName(u"AlterarCadastro")
        AlterarCadastro.resize(800, 600)
        self.centralwidget = QWidget(AlterarCadastro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.TEdescricao = QTextEdit(self.centralwidget)
        self.TEdescricao.setObjectName(u"TEdescricao")

        self.verticalLayout.addWidget(self.TEdescricao)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(50, 16777215))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.horizontalSpacer_6 = QSpacerItem(5, 5, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.edtTitulo = QLineEdit(self.widget)
        self.edtTitulo.setObjectName(u"edtTitulo")

        self.horizontalLayout_5.addWidget(self.edtTitulo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(50, 16777215))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.CBStatus_2 = QComboBox(self.widget)
        self.CBStatus_2.setObjectName(u"CBStatus_2")
        self.CBStatus_2.setMinimumSize(QSize(150, 0))
        self.CBStatus_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.CBStatus_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.CBStatus = QComboBox(self.widget)
        self.CBStatus.setObjectName(u"CBStatus")
        self.CBStatus.setMinimumSize(QSize(150, 0))
        self.CBStatus.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.CBStatus)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_11 = QSpacerItem(74, 40, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout.addWidget(self.dateEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_12 = QSpacerItem(74, 40, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.dateEdit_2 = QDateEdit(self.widget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.horizontalLayout_2.addWidget(self.dateEdit_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_2)

        self.TEdescricao_2 = QTextEdit(self.centralwidget)
        self.TEdescricao_2.setObjectName(u"TEdescricao_2")

        self.verticalLayout_12.addWidget(self.TEdescricao_2)


        self.gridLayout.addLayout(self.verticalLayout_12, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        AlterarCadastro.setCentralWidget(self.centralwidget)

        self.retranslateUi(AlterarCadastro)

        QMetaObject.connectSlotsByName(AlterarCadastro)
    # setupUi

    def retranslateUi(self, AlterarCadastro):
        AlterarCadastro.setWindowTitle(QCoreApplication.translate("AlterarCadastro", u"ALTERAR", None))
        self.label.setText(QCoreApplication.translate("AlterarCadastro", u"Descri\u00e7\u00e3o de entrada", None))
        self.label_10.setText(QCoreApplication.translate("AlterarCadastro", u"Titulo", None))
        self.label_12.setText(QCoreApplication.translate("AlterarCadastro", u"Status", None))
        self.label_3.setText(QCoreApplication.translate("AlterarCadastro", u"Prioridade", None))
        self.label_4.setText(QCoreApplication.translate("AlterarCadastro", u"Data de abertura", None))
        self.label_5.setText(QCoreApplication.translate("AlterarCadastro", u"Data de fechamento", None))
        self.label_2.setText(QCoreApplication.translate("AlterarCadastro", u"Descri\u00e7\u00e3o de fechamento", None))
        self.pushButton.setText(QCoreApplication.translate("AlterarCadastro", u"Confirmar", None))
    # retranslateUi

