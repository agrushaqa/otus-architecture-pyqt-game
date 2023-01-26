import sys
from PyQt5.QtWidgets import  QApplication, QWidget, \
    QTableWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

imagePath = "warship6.jpg"

class ImgWidget1(QtWidgets.QLabel):

    def __init__(self, parent=None):
        super(ImgWidget1, self).__init__(parent)
        pic = QtGui.QPixmap(imagePath)
        self.setPixmap(pic)

class ImgWidget2(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ImgWidget2, self).__init__(parent)
        self.pic = QtGui.QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pic)


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Морской бой'
        self.left = 0
        self.top = 0
        self.width = 413
        self.height = 413
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(45)
        self.tableWidget.verticalHeader().setDefaultSectionSize(45)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 377, 385))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(
            QtCore.Qt.CrossCursor))
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(8)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(45)
        self.tableWidget.verticalHeader().setDefaultSectionSize(45)
        for i_row in range(8):
            for j_column in range(8):
                item = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(0, 180, 255))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setBackground(brush)
                self.tableWidget.setItem(i_row, j_column, item)
        self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        self.tableWidget.setIconSize(QtCore.QSize(45, 45))
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            currentQTableWidgetItem.setIcon(QIcon(QtGui.QPixmap(imagePath)))
            print(currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())