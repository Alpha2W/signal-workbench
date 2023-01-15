from PyQt5.QtWidgets import QWidget
from Ui_signal_panel import Ui_signalPanel

class SignalPanel(QWidget):
    """
    Class Description: SignalPanel
    """
    def __init__(self, *args):
        super(SignalPanel, self).__init__(*args)
        self.ui = Ui_signalPanel()
        self.ui.setupUi(self)
        
        pass
    
    pass
