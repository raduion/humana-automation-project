import time
from pages.cohort_utils.lifemap_utils import LifeMapUtils
from pages.cohort_utils.wellness_utils import WellnessUtils


class CohortLogic:

    def __init__(self, browser):
        self.browser = browser
        self.lifemap_utils = LifeMapUtils(browser)
        self.wellness_utils = WellnessUtils(browser)

    def track_002(self, memberpersonalgeneratedkey, max_score, wait_time, first_track_id_value):
        self.lifemap_utils.lifemap_url_loader(memberpersonalgeneratedkey)
        self.lifemap_utils.lifemap_phone_inputter(phone_number='1234567890')
        self.lifemap_utils.custom_score(**max_score)
        self.lifemap_utils.lifemap_dob_inputter(month='04',
                                                day='11',
                                                year='1949')
        time.sleep(wait_time)

        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey=memberpersonalgeneratedkey,
                                            expected_track_id_value=first_track_id_value)

        self.browser.execute_script('window.localStorage.clear();')
        self.browser.delete_all_cookies()

        time.sleep(5)

    def track_003(self, memberpersonalgeneratedkey, first_track_id_value, wait_time, wellness_answer,
                  second_track_id_value):
        self.wellness_utils.wellness_url_loader(memberpersonalgeneratedkey, first_track_id_value)
        self.wellness_utils.wellness_intro_passer()
        self.wellness_utils.welness_activity_passer(welness_activity_answer=wellness_answer)

        time.sleep(wait_time)

        self.wellness_utils.track_id_checker(memberpersonalgeneratedkey=memberpersonalgeneratedkey,
                                             expected_track_id_value=second_track_id_value)

        self.browser.execute_script('window.localStorage.clear();')
        self.browser.delete_all_cookies()

        time.sleep(5)

    def track_002_003(self, memberpersonalgeneratedkey, max_score, wait_time, first_track_id_value, wellness_answer,
                      second_track_id_value):
        self.track_002(memberpersonalgeneratedkey, max_score, wait_time, first_track_id_value)
        time.sleep(240)
        self.track_003(memberpersonalgeneratedkey, first_track_id_value, wait_time, wellness_answer,
                       second_track_id_value)
