from pages.lifemap_utils.cohort_methods import LifeMapCohortLogic
from pages.lifemap_utils.lifemap_utils import MAX_SCORE_VALUES

COHORT_LOGIC = {
    'track_0002-01': {
        'memberpersonalgeneratedkey': "1000000000023",
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 180,
        'track_id_value': '0002-01'
    }
}


def test_cohort_logic(browser, track=None):
    if track is None:
        track = COHORT_LOGIC
    cohort = LifeMapCohortLogic(browser)

    for x in COHORT_LOGIC:
        cohort.track_002(**track[x])
