from pages.cohort_utils.cohort_methods import CohortLogic
from pages.cohort_utils.lifemap_utils import MAX_SCORE_VALUES
from pages.cohort_utils.wellness_utils import WELLNESS_ANSWERS

COHORT_LOGIC_PARAMS_002 = {
    'track_0002-01': {
        'memberpersonalgeneratedkey': "1000000000022",
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01'
    },
    'track_0002-02': {
        'memberpersonalgeneratedkey': "1000000000007",
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02'
    },
    'track_0002-03': {
        'memberpersonalgeneratedkey': "1000000000003",
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03'
    },
    'track_0002-04': {
        'memberpersonalgeneratedkey': "1000000000004",
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04'
    }
}

COHORT_LOGIC_PARAMS_002_003 = {
    'track_0002-01_0003-05': {
        'memberpersonalgeneratedkey': "1000000000021",
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer': WELLNESS_ANSWERS['Answer 1'],
        'second_track_id_value': '0003-05',
    }

}

COHORT_LOGIC_PARAMS_002_003_004 = {
    'track_0002-01_0003-05': {
        'memberpersonalgeneratedkey': "1000000000021",
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer': WELLNESS_ANSWERS['Answer 1'],
        'second_track_id_value': '0003-05',
        'third_track_id_value': '0004-01'
    }

}


def test_cohort_logic_002(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002
    cohort = CohortLogic(browser)

    for x in COHORT_LOGIC_PARAMS_002:
        cohort.track_002(**track[x])


def test_cohort_logic_002_003(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002_003
    cohort = CohortLogic(browser)

    for x in COHORT_LOGIC_PARAMS_002_003:
        cohort.track_002_003(**track[x])


def test_cohort_logic_002_003_004(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002_003_004
    cohort = CohortLogic(browser)

    for x in COHORT_LOGIC_PARAMS_002_003_004:
        cohort.track_002_003_004(**track[x])
