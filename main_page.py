class MainPage():
    def __init__(self, driver):
        self.driver = driver
        self._top_panel = None

    @property
    def top_panel(self):
        from top_panel import TopPanel
        if self._top_panel is None:
            self._top_panel = TopPanel(self.driver)
        return self._top_panel

    def open(self, url):
        self.driver.get(url)
