from base_component import BaseComponent
from Page import PageLogin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TopPanel(BaseComponent):
    class_name = {
        'name_profile': 'myprofile',
        'button_personal_area': 'enter'
    }

    def click_button_personal_area(self):
        self.driver.find_element_by_class_name(self.class_name['button_personal_area']).click()

    def get_user_name(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.class_name['name_profile'])))
        return self.driver.find_element_by_class_name(self.class_name['name_profile']).text