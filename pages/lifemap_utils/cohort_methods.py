import time
from pages.lifemap_utils.lifemap_utils import LifeMapUtils, MAX_SCORE_VALUES


class LifeMapCohortLogic:

    def __init__(self, browser):
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
