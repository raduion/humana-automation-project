import time
from pages.lifemap_utils.lifemap_utils import LifeMapUtils


class CohortLogic:

    def __init__(self, browser):
        self.browser = browser
        self.lifemap_utils = LifeMapUtils(browser)

    def track_002(self, memberpersonalgeneratedkey, max_score, wait_time, track_id_value):

        self.lifemap_utils.lifemap_url_loader(memberpersonalgeneratedkey)
        self.lifemap_utils.lifemap_phone_inputter(phone_number='1234567890')
        self.lifemap_utils.custom_score(**max_score)
        self.lifemap_utils.lifemap_dob_inputter(month='04',
                                                day='11',
                                                year='1949')
        time.sleep(wait_time)

        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey=memberpersonalgeneratedkey,
                                            expected_track_id_value=track_id_value)

        self.browser.execute_script('window.localStorage.clear();')
        self.browser.delete_all_cookies()

        time.sleep(5)

    def track_003(self, memberpersonalgeneratedkey, max_score, wait_time, track_id_value):
        self.track_002(memberpersonalgeneratedkey, max_score, wait_time, track_id_value)


