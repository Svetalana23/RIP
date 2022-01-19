from rectangle import Rectangle
from circle import Circle
from square import Square
import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)

    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(350,250)
    w.move(300,300)
    w.setWindowTitle('Window')
    w.show()

    sys.exit(app.exec_())
if __name__ == "__main__":
    main()