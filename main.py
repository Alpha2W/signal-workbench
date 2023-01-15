from PyQt5 import QtWidgets		#Official Library
from PyQt5.QtGui import QPalette, QColor
from qt_main_window import OscMainWindow		#Custom Library
import sys		#Official Library

STYLE_MAIN_COLOR = "#303030"
STYLE_SECOND_COLOR = "#454545"
STYLE_EMPHASIS_COLOR = "#FF5555"
STYLE_EMPHASIS_SECOND_COLOR = "#FFFF00"
STYLE_TEXT_COLOR = "#EFEFEF"


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    # app.setStyle(MyProxyStyle("Fusion"))
    app.setStyle("Fusion")
    
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(STYLE_MAIN_COLOR))
    palette.setColor(QPalette.WindowText, QColor(STYLE_TEXT_COLOR))
    palette.setColor(QPalette.Base, QColor(STYLE_MAIN_COLOR))
    palette.setColor(QPalette.AlternateBase, QColor(STYLE_SECOND_COLOR))
    palette.setColor(QPalette.ToolTipBase, QColor(STYLE_MAIN_COLOR))
    palette.setColor(QPalette.ToolTipText, QColor(STYLE_EMPHASIS_SECOND_COLOR))
    palette.setColor(QPalette.Text, QColor(STYLE_TEXT_COLOR))
    # palette.setColor(QPalette.Button, QColor("#202020"))
    palette.setColor(QPalette.Button, QColor(STYLE_EMPHASIS_COLOR))
    palette.setColor(QPalette.ButtonText, QColor(STYLE_TEXT_COLOR))
    palette.setColor(QPalette.BrightText, QColor("#000000"))
    palette.setColor(QPalette.Link, QColor("#2a82da"))
    palette.setColor(QPalette.Highlight, QColor(STYLE_SECOND_COLOR))
    palette.setColor(QPalette.HighlightedText, QColor(STYLE_TEXT_COLOR))
    palette.setColor(QPalette.Shadow, QColor("#000000"))
    palette.setColor(QPalette.Dark, QColor("#101010"))
    palette.setColor(QPalette.Mid, QColor("#151515"))
    palette.setColor(QPalette.Button, QColor("#202020"))
    palette.setColor(QPalette.Midlight, QColor("#252525"))
    palette.setColor(QPalette.Light, QColor("#303030"))
    app.setPalette(palette)
    osc_main_window = OscMainWindow()		#Instanitate a OscMainWindow class
    sys.exit(app.exec_())
    pass

if __name__ == '__main__':
	main()
