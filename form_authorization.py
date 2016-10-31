from base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AuthorizationForm(BaseComponent):
    id = {'login': 'input_auth_email',
          'pass': 'input_auth_pas',
          'email':'input_remind_email',
          'login_facebook':'email',
          'pass_facebook':'pass',
          'button_login_facebook':'loginbutton'
          }
    class_name = {
        'but_login':'pos_but',
        'but_get_new_pass':'getNewPas',
        'but_auth':'enter',
        'error_message_incorrect_login': 'Error',
        'message_sending_new_pass': 'smallText'
                  }
    selectors = {
        'button_facebook':'.sLinks_inside > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)',
        'button_forgot_pass':'table.layout:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > button:nth-child(1)',
        'error_message_incorrect_email': '#RemindAuth > div:nth-child(3)'
    }
    def authorization(self, login, password):
        self.driver.find_element_by_id(self.id['login']).send_keys(login)
        self.driver.find_element_by_id(self.id['pass']).send_keys(password)
        self.driver.find_element_by_class_name(self.class_name['but_login']).click()

    def forgot_password(self, email):
        self.driver.find_element_by_class_name(self.class_name['but_get_new_pass']).click()
        self.driver.find_element_by_id(self.id['email']).send_keys(email)
        self.driver.find_element_by_css_selector(self.selectors['button_forgot_pass']).click()

    def auth_facebook(self, login, password):
        self.driver.find_element_by_css_selector(self.selectors['button_facebook']).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_id(self.id['login_facebook']).send_keys(login)
        self.driver.find_element_by_id(self.id['pass_facebook']).send_keys(password)
        self.driver.find_element_by_id(self.id['button_login_facebook']).click()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_error_message_incorrect_login(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.class_name['error_message_incorrect_login'])))
        return self.driver.find_element_by_class_name(self.class_name['error_message_incorrect_login']).text

    def get_error_message_incorrect_email(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors['error_message_incorrect_email'])))
        return self.driver.find_element_by_css_selector(self.selectors['error_message_incorrect_email']).text

    def message_sending_new_pass_is_displayed(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.class_name['message_sending_new_pass'])))
        return self.driver.find_element_by_class_name(self.class_name['message_sending_new_pass']).is_displayed


