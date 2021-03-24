from pages.lifemap_utils.cohort_methods import CohortLogic
from pages.lifemap_utils.lifemap_utils import MAX_SCORE_VALUES

COHORT_LOGIC_PARAMS = {
    'track_0002-01': {
        'memberpersonalgeneratedkey': "1000000000006",
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'track_id_value': '0002-01'
    },
    'track_0002-02': {
        'memberpersonalgeneratedkey': "1000000000007",
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'track_id_value': '0002-02'
    },
    'track_0002-03': {
        'memberpersonalgeneratedkey': "1000000000003",
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'track_id_value': '0002-03'
    },
    'track_0002-04': {
        'memberpersonalgeneratedkey': "1000000000004",
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'track_id_value': '0002-04'
    }
}


def test_cohort_logic(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS
    cohort = CohortLogic(browser)

    for x in COHORT_LOGIC_PARAMS:
        cohort.track_002(**track[x])
