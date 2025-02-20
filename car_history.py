import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from car_history_page import Ui_CarHistory

import sqlite3
from sqlite3 import Error


class CarHistory(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_CarHistory()
        self. ui.setupUi(self)
        self.loadData()
    
    def loadData(self):
        try:
            sqliteConnection = sqlite3.connect("userHistory.db")
            print("Connected to SQLite")

            sqlite_select_query = "SELECT * from userHistory"
            result = sqliteConnection.execute(sqlite_select_query)
            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CarHistory()
    w.show()
    sys.exit(app.exec_())