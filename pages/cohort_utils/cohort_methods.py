import time
from random import randint
from pages.cohort_utils.lifemap_utils import LifeMapUtils
from pages.cohort_utils.sms_utils import SMSUtils
from pages.cohort_utils.wellness_utils import WellnessUtils


class CohortLogic:

    def __init__(self, browser):
        self.browser = browser
        self.lifemap_utils = LifeMapUtils(browser)
        self.wellness_utils = WellnessUtils(browser)
        self.sms_utlis = SMSUtils(browser)

    def track_002(self, memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value):
        self.lifemap_utils.lifemap_url_loader(memberpersonalgeneratedkey)
        self.lifemap_utils.lifemap_phone_inputter(phone_number)
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

    def track_003(self, memberpersonalgeneratedkey, first_track_id_value, wait_time, wellness_answer_0002,
                  second_track_id_value):
        self.wellness_utils.wellness_url_loader(memberpersonalgeneratedkey, first_track_id_value)
        self.wellness_utils.wellness_intro_passer()
        self.wellness_utils.wellness_activity_passer_0002(wellness_activity_answer=wellness_answer_0002)

        time.sleep(wait_time)

        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey=memberpersonalgeneratedkey,
                                            expected_track_id_value=second_track_id_value)

        self.browser.execute_script('window.localStorage.clear();')
        self.browser.delete_all_cookies()

        time.sleep(5)

    def track_002_003(self, memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value,
                      wellness_answer_0002, second_track_id_value):
        self.track_002(memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value)
        self.track_003(memberpersonalgeneratedkey, first_track_id_value, wait_time, wellness_answer_0002,
                       second_track_id_value)

    def track_002_003_004(self, memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value,
                          wellness_answer_0002, second_track_id_value, third_track_id_value):
        self.track_002(memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value)
        self.track_003(memberpersonalgeneratedkey, first_track_id_value, wait_time, wellness_answer_0002,
                       second_track_id_value)
        time.sleep(600)
        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey, third_track_id_value)

    def track_002_003_005(self, memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value,
                          wellness_answer_0002, second_track_id_value, third_track_id_value):
        self.track_002(memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value)
        self.track_003(memberpersonalgeneratedkey, first_track_id_value, wait_time, wellness_answer_0002,
                       second_track_id_value)
        time.sleep(1200)
        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey, third_track_id_value)

    def track_002_003_005_006(self, memberpersonalgeneratedkey, phone_number, max_score, wait_time,
                              first_track_id_value, wellness_answer_0002, second_track_id_value, third_track_id_value,
                              reply_1, reply_2, fourth_track_id_value):
        self.track_002(memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value)
        self.track_003(memberpersonalgeneratedkey, first_track_id_value, wait_time, wellness_answer_0002,
                       second_track_id_value)
        time.sleep(1200)
        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey, third_track_id_value)
        self.sms_utlis.sms_tool_url_loader(phone_number)
        time.sleep(3)
        self.sms_utlis.sms_reply(reply=reply_1)
        time.sleep(5)
        self.browser.refresh()
        time.sleep(5)
        self.sms_utlis.sms_reply(reply=reply_2)
        time.sleep(wait_time)
        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey, fourth_track_id_value)

    def track_006(self, memberpersonalgeneratedkey, fourth_track_id_value, wait_time, wellness_answer_0006,
                  fifth_track_id_value):
        self.wellness_utils.wellness_url_loader(memberpersonalgeneratedkey, fourth_track_id_value)
        self.wellness_utils.wellness_activity_passer_0006(wellness_activity_answer=wellness_answer_0006)

        time.sleep(wait_time)

        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey=memberpersonalgeneratedkey,
                                            expected_track_id_value=fifth_track_id_value)

        self.browser.execute_script('window.localStorage.clear();')
        self.browser.delete_all_cookies()

        time.sleep(5)

    def track_002_003_005_006_007(self, memberpersonalgeneratedkey, phone_number, max_score, wait_time,
                                  first_track_id_value, wellness_answer_0002, second_track_id_value,
                                  third_track_id_value, reply_1, reply_2, fourth_track_id_value, wellness_answer_0006,
                                  fifth_track_id_value):
        self.track_002(memberpersonalgeneratedkey, phone_number, max_score, wait_time, first_track_id_value)
        self.track_003(memberpersonalgeneratedkey, first_track_id_value, wait_time, wellness_answer_0002,
                       second_track_id_value)
        time.sleep(1200)
        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey, third_track_id_value)
        self.sms_utlis.sms_tool_url_loader(phone_number)
        time.sleep(3)
        self.sms_utlis.sms_reply(reply=reply_1)
        time.sleep(5)
        self.browser.refresh()
        time.sleep(5)
        self.sms_utlis.sms_reply(reply=reply_2)
        time.sleep(wait_time)
        self.lifemap_utils.track_id_checker(memberpersonalgeneratedkey, fourth_track_id_value)
        self.track_006(memberpersonalgeneratedkey, fourth_track_id_value, wait_time, wellness_answer_0006,
                       fifth_track_id_value)

