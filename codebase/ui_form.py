# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1000, 600))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLockScreen))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 981, 561))
        self.gridLayoutWidget.setMinimumSize(QSize(981, 561))
        self.gridLayoutWidget.setMaximumSize(QSize(981, 561))
        font = QFont()
        font.setPointSize(13)
        self.gridLayoutWidget.setFont(font)
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(979, 559))
        self.tabWidget.setMaximumSize(QSize(979, 559))
        self.tabWidget.setFont(font)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.tab_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(473, 500))
        self.frame.setMaximumSize(QSize(473, 500))
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(449, 235))
        self.widget_2.setMaximumSize(QSize(449, 235))
        self.widget_2.setFont(font)
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(427, 39))
        self.pushButton.setMaximumSize(QSize(427, 39))
        self.pushButton.setFont(font)

        self.gridLayout_5.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(427, 39))
        self.pushButton_2.setMaximumSize(QSize(427, 39))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)

        self.gridLayout_5.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(427, 121))
        self.label.setMaximumSize(QSize(427, 121))
        font1 = QFont()
        font1.setFamilies([u"Lucida Sans Typewriter"])
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(449, 234))
        self.widget_3.setMaximumSize(QSize(449, 234))
        self.widget_3.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(427, 39))
        self.pushButton_4.setMaximumSize(QSize(427, 39))
        self.pushButton_4.setFont(font)

        self.verticalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_5.addWidget(self.widget_3)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.tab_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(473, 500))
        self.frame_2.setMaximumSize(QSize(473, 500))
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(449, 200))
        self.frame_3.setMaximumSize(QSize(449, 235))
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_5 = QWidget(self.frame_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(425, 102))
        self.widget_5.setMaximumSize(QSize(425, 102))
        self.widget_5.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(198, 80))
        self.label_2.setMaximumSize(QSize(198, 80))
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(198, 38))
        self.comboBox.setMaximumSize(QSize(198, 38))
        self.comboBox.setFont(font)

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout_9.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.frame_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(425, 102))
        self.widget_6.setMaximumSize(QSize(425, 102))
        self.widget_6.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(198, 80))
        self.label_4.setMaximumSize(QSize(198, 80))
        self.label_4.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(198, 38))
        self.lineEdit.setMaximumSize(QSize(198, 38))
        self.lineEdit.setFont(font)

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_9.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.frame_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(425, 102))
        self.widget_7.setMaximumSize(QSize(425, 102))
        self.widget_7.setFont(font)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_5 = QPushButton(self.widget_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)

        self.horizontalLayout_7.addWidget(self.pushButton_5)


        self.verticalLayout_9.addWidget(self.widget_7)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(449, 234))
        self.widget_4.setMaximumSize(QSize(449, 234))
        self.widget_4.setFont(font)
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_3 = QPushButton(self.widget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(427, 39))
        self.pushButton_3.setMaximumSize(QSize(427, 39))
        self.pushButton_3.setFont(font)

        self.verticalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_7.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(self.tab_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logsView = QPlainTextEdit(self.widget)
        self.logsView.setObjectName(u"logsView")
        self.logsView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.logsView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.logsView.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.logsView)

        self.logViewDesc = QTextEdit(self.widget)
        self.logViewDesc.setObjectName(u"logViewDesc")
        self.logViewDesc.setMaximumSize(QSize(16777215, 130))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(10)
        self.logViewDesc.setFont(font2)
        self.logViewDesc.setMouseTracking(True)
        self.logViewDesc.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.logViewDesc.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.logViewDesc.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.logViewDesc.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.logViewDesc)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout_3 = QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.tab_5)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(800, 400))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.textBrowser.setFont(font3)

        self.gridLayout_3.addWidget(self.textBrowser, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyShield", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start Firewall", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Stop Firewall", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PyShield", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Clear Logs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add Firewall Rule :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"src_ip", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"dst_port", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter Value : ", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Add Rule", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Show Firewall Rules", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Options", None))
        self.logsView.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logs will show here...", None))
        self.logViewDesc.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Above are the logs generated as of the current Boot of the program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Default Location of generated logs file is - </span><span style=\" font-size:11pt; font-style:italic; color:#00ff7f;\">ApplicationFolder</span><span style=\" font-size:11pt; color:#00ff7f;\">/logs.txt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">[Location Format : </span><span style=\" font-size:11pt; font-style:italic;\">ApplicationFolder</span><span style=\" font-size:11pt;\">/PyShield.py]</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Logs", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:16pt; font-weight:700;\"><br /></span><span style=\" font-family:'Lucida Calligraphy'; font-size:26pt; font-weight:700;\">Welcome to </span><span style=\" font-family:'Courier New'; font-size:26pt; font-weight:700; color:#00aa00;\">PyShield</span><span style=\" font-family:'Courier New'; font-size:26pt; font-weight:700;\"> !</span><"
                        "span style=\" font-family:'Courier New'; font-size:16pt;\"><br /></span><span style=\" font-family:'Courier New'; font-size:18pt;\">(An intuitive way to protect yourself</span><span style=\" font-family:'Calibri'; font-size:18pt;\">)</span><span style=\" font-family:'Calibri'; font-size:16pt;\"><br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Calibri'; font-size:16pt;\"><br /></span><span style=\" font-family:'Calibri'; font-size:14pt;\">Designed and Developed using :</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Calibri'; font-size:14pt;\">~</span><span style=\" font-size:14pt; color:#000000;\"> </span><span style=\" font-size:14pt; color:#00ff7f;\">PyQt6</span><span style=\" font-family:'Calibri'; font-size:14pt;\"> and </span><span style="
                        "\" font-family:'Calibri'; font-size:14pt; color:#00ff7f;\">Qt Creator.</span><span style=\" font-family:'Calibri'; font-size:14pt; color:#ffffff;\"> </span><span style=\" font-family:'Calibri'; font-size:14pt;\">[for GUI purpose]</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Calibri'; font-size:14pt;\">~</span><span style=\" font-size:14pt; color:#000000;\"> </span><span style=\" font-size:14pt; color:#00ff7f;\">PyShark </span><span style=\" font-family:'Calibri'; font-size:14pt;\">[Working with Network]</span><span style=\" font-family:'Calibri'; font-size:14pt; color:#00ff7f;\"><br /></span><span style=\" font-family:'Calibri'; font-size:14pt;\">~</span><span style=\" font-size:14pt; color:#000000;\"> </span><span style=\" font-size:14pt; color:#00ff7f;\">Python </span><span style=\" font-family:'Calibri'; font-size:14pt;\">[Base Programming Language]</span></p>\n"
"<p align="
                        "\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:14pt;\"><br /></span><span style=\" font-family:'Courier New'; font-size:14pt; color:#728d02;\">Team Members : Abhinav Negi, Ankit Kumar, Abhay Rawat,</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:14pt; color:#728d02;\"> Akshat Bisht</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Credits", None))
    # retranslateUi

