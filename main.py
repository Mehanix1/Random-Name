class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._should_draw = False
        self.setupUi(self)
        self._init_ui()
        self._should_draw = False

    def _init_ui(self) -> None:
        self.pushButton.clicked.connect(self._create)

    def _create(self):
        self._should_draw = True
        self.update()

    def paintEvent(self, event) -> None:
        if not self._should_draw:
            return

        qr = QPainter()
        qr.begin(self)
        self.draw_circle(qr)
        qr.end()

    def draw_circle(self, qr):
        qr.setBrush(QColor.fromHsv(randint(0, 359), 255, 255, 255))
        diameter = randint(70, 200)
        start = 60
        qr.drawEllipse(start, start, start + diameter, start + diameter)