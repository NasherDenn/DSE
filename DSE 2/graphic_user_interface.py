# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os


# создаём приложение
app = QApplication(sys.argv)
# создаём окно приложения
window = QWidget()
# название приложения
window.setWindowTitle('Data Search Engine')
# задаём стиль приложения Fusion
app.setStyle('Fusion')
# размер окна приложения
window.setFixedSize(1521, 965)

# устанавливаем favicon в окне приложения
icon = QIcon()
icon.addFile(os.path.abspath(os.getcwd()) + '\\Pictures\\' + 'icon.ico', QSize(), QIcon.Normal, QIcon.Off)
icon.addFile(os.path.abspath(os.getcwd()) + '\\Pictures\\' + 'icon.ico', QSize(), QIcon.Active, QIcon.On)
app.setWindowIcon(icon)

# создаём стиль кнопок приложения
style_fon = QFont()
# стиль шрифта
style_fon.setFamily(u"Arial")
# размер шрифта
style_fon.setPointSize(14)
# не наклонный
style_fon.setItalic(False)

# создаём однострочное поле - поиска, для ввода номер линии, чертежа, номера репорта, номера work order
line_search = QLineEdit(window)
# устанавливаем положение окна ввода и его размеры в окне приложения
line_search.setGeometry(QRect(20, 20, 561, 41))
# устанавливаем стиль поля для поиска
line_search.setFont(style_fon)
# дополнительные параметры
line_search.setMouseTracking(False)
line_search.setContextMenuPolicy(Qt.NoContextMenu)
line_search.setAcceptDrops(True)
line_search.setStyleSheet(u"")
line_search.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
line_search.setEchoMode(QLineEdit.Normal)
line_search.setCursorPosition(0)
line_search.setCursorMoveStyle(Qt.LogicalMoveStyle)
line_search.setClearButtonEnabled(True)
# сразу вставляем значение для поиска
line_search.setText('28278087')
# устанавливаем курсор на поле поиска
line_search.setFocus()

# создаём кнопку "Поиск"
button_search = QPushButton('Поиск', window)
# устанавливаем положение и размер кнопки для поиска в окне приложения
button_search.setGeometry(600, 20, 161, 41)
# задаём параметры стиля и оформления кнопки "Поиск"
button_search.setFont(style_fon)

# создаём кнопку "Закрыть" для закрытия программы
button_exit = QPushButton('Закрыть', window)
# устанавливаем положение и размер кнопки "Закрыть"
button_exit.setGeometry(QRect(1340, 904, 161, 41))
# задаём параметры стиля и оформления кнопки "Закрыть"
button_exit.setFont(style_fon)
# Закрытие программы при нажатии на кнопку "Закрыть"
button_exit.clicked.connect(qApp.exit)

# создаём стиль для полей ввода логина и пароля
style_fon_login_password = QFont()
style_fon_login_password.setFamily(u"Arial")
style_fon_login_password.setPointSize(11)
style_fon_login_password.setItalic(True)

# создаём однострочное поле для ввода логина
line_login = QLineEdit(window)
# устанавливаем положение и размер поля для ввода логина в родительском окне (window)
line_login.setGeometry(QRect(1270, 20, 111, 31))
# задаём параметры стиля и оформления поля для ввода логина
line_login.setFont(style_fon_login_password)
# дополнительные параметры
line_login.setEchoMode(QLineEdit.Normal)
# устанавливаем исчезающий текст
line_login.setPlaceholderText('login')
# устанавливаем по умолчанию логин
line_login.setText('admin')

# создаём однострочное поле для ввода пароля
line_password = QLineEdit(window)
# устанавливаем положение и размер поля для ввода пароля в родительском окне (window)
line_password.setGeometry(QRect(1270, 60, 111, 31))
# задаём параметры стиля и оформления поля для ввода пароля
line_password.setFont(style_fon_login_password)
# дополнительные параметры
line_password.setEchoMode(QLineEdit.Password)
# устанавливаем исчезающий текст
line_password.setPlaceholderText('password')
# устанавливаем по умолчанию пароль
line_password.setText('admin')

# создаём стиль для названий полей ввода логина и пароля
style_fon_label_login_password = QFont()
style_fon_label_login_password.setFamily(u"Arial")
style_fon_label_login_password.setPointSize(12)
style_fon_label_login_password.setItalic(True)

# устанавливаем надпись "Логин"
label_login = QLabel('Логин', window)
# устанавливаем положение и размер поля для надписи "Логин" в родительском окне (window)
label_login.setGeometry(QRect(1200, 30, 61, 21))
# задаём параметры стиля и оформления поля для надписи "Логин"
label_login.setFont(style_fon_label_login_password)

# устанавливаем надпись "Пароль"
label_password = QLabel('Пароль', window)
# устанавливаем положение и размер поля для надписи "Пароль" в родительском окне (window)
label_password.setGeometry(QRect(1190, 70, 81, 21))
# задаём параметры стиля и оформления поля для надписи "Пароль"
label_password.setFont(style_fon_label_login_password)

# создаём кнопку печати
button_print = QPushButton('Печать', window)
# устанавливаем положение и размер кнопки печати в родительском окне (window)
button_print.setGeometry(QRect(20, 155, 161, 41))
# задаём параметры стиля и оформления кнопки печати
button_print.setFont(style_fon)

# создаём кнопку "Войти"
button_log_in = QPushButton('Войти', window)
# устанавливаем положение и размер кнопки "Войти" в родительском окне (window)
button_log_in.setGeometry(QRect(1390, 20, 111, 31))
# задаём параметры стиля и оформления кнопки "Войти"
button_log_in.setFont(style_fon)

# создаём кнопку "Выйти"
button_log_out = QPushButton('Выйти', window)
# устанавливаем положение и размер кнопки "Выйти" в родительском окне (window)
button_log_out.setGeometry(QRect(1390, 60, 111, 31))
# задаём параметры стиля и оформления кнопки "Выйти"
button_log_out.setFont(style_fon)
# делаем неактивной кнопку "Выйти" до авторизации
button_log_out.setDisabled(True)

# создаём кнопку "Добавить"
button_add = QPushButton('Добавить', window)
# устанавливаем положение и размер кнопки "Добавить" в родительском окне (window)
button_add.setGeometry(QRect(200, 155, 161, 41))
# задаём параметры стиля и оформления кнопки "Добавить"
button_add.setFont(style_fon)
# делаем неактивной кнопку "Добавить" до авторизации
button_add.setDisabled(True)

# создаём кнопку "Удалить"
button_delete = QPushButton('Удалить', window)
# устанавливаем положение и размер кнопки "Удалить" в родительском окне (window)
button_delete.setGeometry(QRect(20, 904, 171, 41))
# задаём параметры стиля и оформления кнопки "Удалить"
button_delete.setFont(style_fon)
# делаем неактивной кнопку "Удалить" до авторизации
button_delete.setDisabled(True)

# создаём кнопку "Сводные данные"
button_statistic_master = QPushButton('Сводные данные', window)
# устанавливаем положение и размер кнопки "Сводные данные" в родительском окне (window)
button_statistic_master.setGeometry(QRect(659, 904, 201, 41))
# задаём параметры стиля и оформления кнопки "Сводные данные"
button_statistic_master.setFont(style_fon)
# делаем неактивной кнопку "Сводные данные" до авторизации
button_statistic_master.setDisabled(True)

# вставляем картинку YKR
label_ykr = QLabel(window)
# устанавливаем положение и размер картинки YKR в родительском окне (window)
label_ykr.setGeometry(QRect(790, 20, 111, 116))
label_ykr.setPixmap(QPixmap(os.path.abspath(os.getcwd()) + '\\Pictures\\' + 'logo_ykr.png'))

# вставляем картинку NCA
label_nca = QLabel(window)
# устанавливаем положение и размер картинки NCA в родительском окне (window)
label_nca.setGeometry(QRect(920, 20, 111, 116))
label_nca.setPixmap(QPixmap(os.path.abspath(os.getcwd()) + '\\Pictures\\' + 'logo_nca.png'))

# вставляем картинку NCOC
label_ncoc = QLabel(window)
# устанавливаем положение и размер картинки NCOC в родительском окне (window)
label_ncoc.setGeometry(QRect(1050, 20, 111, 116))
label_ncoc.setPixmap(QPixmap(os.path.abspath(os.getcwd()) + '\\Pictures\\' + 'logo_ncoc.png'))

# общая область с боковой полосой прокрутки
scroll_area = QScrollArea(window)
# полоса прокрутки появляется, только если таблицы больше самой области прокрутки
scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
# задаём размер области с полосой прокрутки
scroll_area.setGeometry(20, 215, 1481, 670)

# создаём группу из радио-кнопок 'ON', 'OF', 'OS'
groupBox_location = QGroupBox(window)
# устанавливаем размер группы радио-кнопок
groupBox_location.setGeometry(QRect(20, 80, 161, 56))
# устанавливаем название группы радио-кнопок
groupBox_location.setTitle('Локация')
# устанавливаем стиль группы радио-кнопок 'ON', 'OF', 'OS'
groupBox_location.setStyleSheet('''QGroupBox {border: 0.5px solid grey;};
                                   QGroupBox:title{
                                   subcontrol-origin: margin;
                                   subcontrol-position: top center;
                                   padding: 0 3px 0 3px;
                                }''')

# создаём радио-кнопку локации 'ON'
radioButton_on = QRadioButton(groupBox_location)
# устанавливаем положение внутри группы
radioButton_on.setGeometry(QRect(10, 25, 42, 20))
# указываем текст радио-кнопки
radioButton_on.setText('ON')
# делаем радио-кнопку 'ON' активной по умолчанию
radioButton_on.setChecked(True)

# создаём радио-кнопку локации 'OF'
radioButton_of = QRadioButton(groupBox_location)
# устанавливаем положение внутри группы
radioButton_of.setGeometry(QRect(60, 25, 42, 20))
# указываем текст радио-кнопки
radioButton_of.setText('OF')

# создаём радио-кнопку локации 'OS'
radioButton_os = QRadioButton(groupBox_location)
# устанавливаем положение внутри группы
radioButton_os.setGeometry(QRect(110, 25, 42, 20))
# указываем текст радио-кнопки
radioButton_os.setText('OS')

# создаём группу из чек-боксов методов контроля
groupBox_ndt = QGroupBox(window)
groupBox_ndt.setGeometry(QRect(200, 80, 161, 56))
# устанавливаем название группы чек-боксов
groupBox_ndt.setTitle('Метод контроля')
# устанавливаем стиль группы чек-боксов методов контроля
groupBox_ndt.setStyleSheet('''QGroupBox {border: 0.5px solid grey;};
                              QGroupBox:title{
                              subcontrol-origin: margin;
                              subcontrol-position: top center;
                              padding: 0 3px 0 3px;
                           }''')

# создаём чек-бокс метода контроля 'UTT'
checkBox_utt = QCheckBox(groupBox_ndt)
# устанавливаем положение внутри группы
checkBox_utt.setGeometry(QRect(10, 25, 61, 20))
# указываем текст чек-бокса
checkBox_utt.setText('UTT')
# делаем чек-бокс 'UTT' активным по умолчанию
checkBox_utt.setChecked(True)

# создаём чек-бокс метода контроля 'PAUT'
checkBox_paut = QCheckBox(groupBox_ndt)
# устанавливаем положение внутри группы
checkBox_paut.setGeometry(QRect(80, 25, 61, 20))
# указываем текст чек-бокса
checkBox_paut.setText('PAUT')

# создаём группу из чек-боксов годов
groupBox_year = QGroupBox(window)
# устанавливаем размер группы радио-кнопок
groupBox_year.setGeometry(QRect(380, 80, 381, 56))
# устанавливаем название группы чек-боксов
groupBox_year.setTitle('Год контроля')
# устанавливаем стиль группы чек-боксов годов
groupBox_year.setStyleSheet('''QGroupBox {border: 0.5px solid grey;};
                               QGroupBox:title{
                               subcontrol-origin: margin;
                               subcontrol-position: top center;
                               padding: 0 3px 0 3px;
                            }''')

# создаём чек-бокс года '2023'
checkBox_2023 = QCheckBox(groupBox_year)
# устанавливаем положение внутри группы
checkBox_2023.setGeometry(QRect(10, 25, 61, 20))
# указываем текст чек-бокса
checkBox_2023.setText('2023')

# создаём чек-бокс года '2022'
checkBox_2022 = QCheckBox(groupBox_year)
# устанавливаем положение внутри группы
checkBox_2022.setGeometry(QRect(80, 25, 61, 20))
# указываем текст чек-бокса
checkBox_2022.setText('2022')
# делаем чек-бокс '2022' активным по умолчанию
checkBox_2022.setChecked(True)

# создаём чек-бокс года '2021'
checkBox_2021 = QCheckBox(groupBox_year)
# устанавливаем положение внутри группы
checkBox_2021.setGeometry(QRect(150, 25, 61, 20))
# указываем текст чек-бокса
checkBox_2021.setText('2021')

# создаём чек-бокс года '2020'
checkBox_2020 = QCheckBox(groupBox_year)
# устанавливаем положение внутри группы
checkBox_2020.setGeometry(QRect(220, 25, 61, 20))
# указываем текст чек-бокса
checkBox_2020.setText('2020')

# создаём чек-бокс года '2019'
checkBox_2019 = QCheckBox(groupBox_year)
# устанавливаем положение внутри группы
checkBox_2019.setGeometry(QRect(290, 25, 61, 20))
# указываем текст чек-бокса
checkBox_2019.setText('2019')

# устанавливаем последовательность перехода по нажатию на клавишу 'Tab'
# поле логин - поле пароль
window.setTabOrder(line_login, line_password)
# поле пароль - кнопка 'Войти'
window.setTabOrder(line_password, button_log_in)
# поле для ввода - кнопка 'Поиск'
window.setTabOrder(line_search, button_search)
# кнопка 'Войти' - радио-кнопка 'ON'
window.setTabOrder(button_search, radioButton_on)

# нажатие кнопки "Войти"
# button_log_in.clicked.connect(log_in)
# нажатие на кнопку Enter когда фокус (каретка - мигающий символ "|") находится в поле для ввода логина
# line_login.returnPressed.connect(log_in)
# нажатие на кнопку Enter когда фокус (каретка - мигающий символ "|") находится в поле для ввода пароля
# line_password.returnPressed.connect(log_in)

# нажатие на кнопку "Печать"
# button_print.clicked.connect(print_table)

# нажатие на кнопку "Добавить"
# button_add.clicked.connect(add_tables)

# нажатие на кнопку "Поиск"
# button_search.clicked.connect(search)
# нажатие на кнопку Enter когда фокус (каретка - мигающий символ "|") находится в поле для ввода номера линии, чертежа,
# номера репорта или work order
# line_search.returnPressed.connect(search)

# нажатие на кнопку "Удалить"
# button_delete.clicked.connect(delete_report)

# нажатие на кнопку "Сформировать отчёт"
# button_create_report.clicked.connect(create_report)

# нажатие на кнопку "Сводные данные"
# button_statistic_master.clicked.connect(statistic_master)

# нажатие на кнопку "Выйти"
# button_log_out.clicked.connect(log_out)


def main():
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
