import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import sys

class MainWindow(QtGui.QDialog):
        def __init__(self):
                QtGui.QDialog.__init__(self)

                dial = QtGui.QDial()
                dial.setNotchesVisible(True)
                self.spinbox = QtGui.QSpinBox()

                layout = QtGui.QHBoxLayout()
                layout.addWidget(dial)
                layout.addWidget(self.spinbox)
                self.setLayout(layout)

                #connect this event to the given method.
                dial.valueChanged.connect(self.changeSpinbox)

        def changeSpinbox(self, value):
                #do some operation on this value. In this case half it.
                self.spinbox.setValue(value / 2)

app = QtGui.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()