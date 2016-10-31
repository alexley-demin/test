class PageLogin():
    def __init__(self, driver):

        self.driver = driver
        self.authorization_form = None

    @property
    def auth_form(self):
        from form_authorization import AuthorizationForm

        if self.authorization_form is None:
            self.authorization_form = AuthorizationForm(self.driver)
        return self.authorization_form

    def open(self, url):
        self.driver.get(url)