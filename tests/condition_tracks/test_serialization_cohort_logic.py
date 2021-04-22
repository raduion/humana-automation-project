from pages.cohort_utils.cohort_methods import CohortLogic
from pages.cohort_utils.lifemap_utils import MAX_SCORE_VALUES
from pages.cohort_utils.wellness_utils import WELLNESS_ANSWERS_0002, WELLNESS_ANSWERS_0006

COHORT_LOGIC_PARAMS_002 = {
    'track_0002-01': {
        'memberpersonalgeneratedkey': "1000000000022",
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'phone_number': '9049446547',
        'wait_time': 240,
        'first_track_id_value': '0002-01'
    },
    'track_0002-02': {
        'memberpersonalgeneratedkey': "1000000000028",
        'phone_number': '8173813339',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02'
    },
    'track_0002-03': {
        'memberpersonalgeneratedkey': "1000000000025",
        'phone_number': '8643514182',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03'
    },
    'track_0002-04': {
        'memberpersonalgeneratedkey': "1000000000023",
        'phone_number': '5863152106',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04'
    }
}

COHORT_LOGIC_PARAMS_002_003 = {
    'track_0003-01': {
        'memberpersonalgeneratedkey': "1000000000021",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01'
    },
    'track_0003-02': {
        'memberpersonalgeneratedkey': "1000000000026",  # this needs a user with F gender
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 4'],
        'second_track_id_value': '0003-02'
    },
    'track_0003-03': {
        'memberpersonalgeneratedkey': "1000000000025",  # this needs a user with M or null gender
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 4'],
        'second_track_id_value': '0003-03'
    },
    'track_0003-04_a': {
        'memberpersonalgeneratedkey': "1000000000022",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 3'],
        'second_track_id_value': '0003-04'
    },
    'track_0003-04_b': {
        'memberpersonalgeneratedkey': "1000000000023",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 5'],
        'second_track_id_value': '0003-04'
    },
    'track_0003-05_a': {
        'memberpersonalgeneratedkey': "1000000000024",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 1'],
        'second_track_id_value': '0003-05'
    },
    'track_0003-05_b': {
        'memberpersonalgeneratedkey': "1000000000027",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 7'],
        'second_track_id_value': '0003-05'
    },
    'track_0003-06': {
        'memberpersonalgeneratedkey': "1000000000028",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 6'],
        'second_track_id_value': '0003-06'
    },
    'track_0003-01_2': {
        'memberpersonalgeneratedkey': "1000000000021",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01'
    },
    'track_0003-02_2': {
        'memberpersonalgeneratedkey': "1000000000026",  # this needs a user with F gender
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 4'],
        'second_track_id_value': '0003-02'
    },
    'track_0003-03_2': {
        'memberpersonalgeneratedkey': "1000000000025",  # this needs a user with M or null gender
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 4'],
        'second_track_id_value': '0003-03'
    },
    'track_0003-04_a2': {
        'memberpersonalgeneratedkey': "1000000000022",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 3'],
        'second_track_id_value': '0003-04'
    },
    'track_0003-04_b2': {
        'memberpersonalgeneratedkey': "1000000000023",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 5'],
        'second_track_id_value': '0003-04'
    },
    'track_0003-05_a2': {
        'memberpersonalgeneratedkey': "1000000000024",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 1'],
        'second_track_id_value': '0003-05'
    },
    'track_0003-05_b2': {
        'memberpersonalgeneratedkey': "1000000000027",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 7'],
        'second_track_id_value': '0003-05'
    },
    'track_0003-06_2': {
        'memberpersonalgeneratedkey': "1000000000028",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_2'],
        'wait_time': 240,
        'first_track_id_value': '0002-02',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 6'],
        'second_track_id_value': '0003-06'
    },
    'track_0003-01_3': {
        'memberpersonalgeneratedkey': "1000000000021",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01'
    },
    'track_0003-02_3': {
        'memberpersonalgeneratedkey': "1000000000026",  # this needs a user with F gender
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 4'],
        'second_track_id_value': '0003-02'
    },
    'track_0003-03_3': {
        'memberpersonalgeneratedkey': "1000000000025",  # this needs a user with M or null gender
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 4'],
        'second_track_id_value': '0003-03'
    },
    'track_0003-04_a3': {
        'memberpersonalgeneratedkey': "1000000000022",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 3'],
        'second_track_id_value': '0003-04'
    },
    'track_0003-04_b3': {
        'memberpersonalgeneratedkey': "1000000000023",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 5'],
        'second_track_id_value': '0003-04'
    },
    'track_0003-05_a3': {
        'memberpersonalgeneratedkey': "1000000000024",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 1'],
        'second_track_id_value': '0003-05'
    },
    'track_0003-05_b3': {
        'memberpersonalgeneratedkey': "1000000000027",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 7'],
        'second_track_id_value': '0003-05'
    },
    'track_0003-06_3': {
        'memberpersonalgeneratedkey': "1000000000028",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_3'],
        'wait_time': 240,
        'first_track_id_value': '0002-03',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 6'],
        'second_track_id_value': '0003-06'
    },
    'track_0003-01_4': {
        'memberpersonalgeneratedkey': "1000000000011",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01'
    },
    'track_0003-02_4': {
        'memberpersonalgeneratedkey': "1000000000026",  # this needs a user with F gender
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 4'],
        'second_track_id_value': '0003-02'
    },
    'track_0003-03_4': {
        'memberpersonalgeneratedkey': "1000000000025",  # this needs a user with M or null gender
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 4'],
        'second_track_id_value': '0003-03'
    },
    'track_0003-04_a4': {
        'memberpersonalgeneratedkey': "1000000000022",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 3'],
        'second_track_id_value': '0003-04'
    },
    'track_0003-04_b4': {
        'memberpersonalgeneratedkey': "1000000000023",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 5'],
        'second_track_id_value': '0003-04'
    },
    'track_0003-05_a4': {
        'memberpersonalgeneratedkey': "1000000000024",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 1'],
        'second_track_id_value': '0003-05'
    },
    'track_0003-05_b4': {
        'memberpersonalgeneratedkey': "1000000000027",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 7'],
        'second_track_id_value': '0003-05'
    },
    'track_0003-06_4': {
        'memberpersonalgeneratedkey': "1000000000028",
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_4'],
        'wait_time': 240,
        'first_track_id_value': '0002-04',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 6'],
        'second_track_id_value': '0003-06'
    }

}

COHORT_LOGIC_PARAMS_002_003_004 = {
    'track_0004-01': {
        'memberpersonalgeneratedkey': "1000000000011",  # this needs a user with CHRONIC_CONDITION_DESC = ["Diabetes",
        # or ["Diabetes", ...]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0004-01'

    },
    'track_0004-02_a': {
        'memberpersonalgeneratedkey': "1000000000012",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0004-02'
    },
    'track_0004-02_b': {
        'memberpersonalgeneratedkey': "1000000000013",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0004-02'
    },
    'track_0004-02_c': {
        'memberpersonalgeneratedkey': "1000000000014",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0004-02'
    },
    'track_0004-03': {
        'memberpersonalgeneratedkey': "1000000000015",  # this needs a user with CHRONIC_CONDITION_DESC =
        # [“Rheumatoid arthritis and inflammatory diseases"]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0004-03'
    },
    'track_0004-04': {
        'memberpersonalgeneratedkey': "1000000000017",  # this needs a user with CHRONIC_CONDITION_DESC =
        # [“Breast, Prostate, Colorectal and Other Cancers and Tumors”]"
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0004-04'
    },
    'track_0004-05': {
        'memberpersonalgeneratedkey': "1000000000019",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF”,
        # “Breast, Prostate, Colorectal and Other Cancers and Tumors”, ], or [“CHF”, “Rheumatoid Arthritis and
        # Inflammatory Connective Tissue Disease”], or [“CHF”, “Breast, Prostate, Colorectal and Other Cancers and
        # Tumors”, “Rheumatoid Arthritis and Inflammatory Connective Tissue Disease”], or [“COPD”, “Breast, Prostate,
        # Colorectal and Other Cancers and Tumors”, ], or [“COPD”, “Rheumatoid Arthritis and Inflammatory Connective
        # Tissue Disease”], or [“COPD”, “Breast, Prostate, Colorectal and Other Cancers and Tumors”, “Rheumatoid
        # Arthritis and Inflammatory Connective Tissue Disease”], or [“Breast, Prostate, Colorectal and Other Cancers
        # and Tumors”, “Rheumatoid Arthritis and Inflammatory Connective Tissue Disease”]"
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0004-05'
    },
    'track_0004-06': {
        'memberpersonalgeneratedkey': "1000000000018",  # this needs a user with CHRONIC_CONDITION_DESC = [null],
        # or all other members not in HCC table"
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0004-06'
    },

}

COHORT_LOGIC_PARAMS_002_003_005 = {
    'track_0005-01': {
        'memberpersonalgeneratedkey': "1000000000001",  # this needs a user with CHRONIC_CONDITION_DESC = ["Diabetes",
        # or ["Diabetes", ...]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-01'

    },
    'track_0005-02_a': {
        'memberpersonalgeneratedkey': "1000000000012",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-02'
    },
    'track_0005-02_b': {
        'memberpersonalgeneratedkey': "1000000000013",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-02'
    },
    'track_0005-02_c': {
        'memberpersonalgeneratedkey': "1000000000014",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-02'
    },
    'track_0005-03': {
        'memberpersonalgeneratedkey': "1000000000015",  # this needs a user with CHRONIC_CONDITION_DESC =
        # [“Rheumatoid arthritis and inflammatory diseases"]
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-03'
    },
    'track_0005-04': {
        'memberpersonalgeneratedkey': "1000000000017",  # this needs a user with CHRONIC_CONDITION_DESC =
        # [“Breast, Prostate, Colorectal and Other Cancers and Tumors”]"
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-04'
    },
    'track_0005-05': {
        'memberpersonalgeneratedkey': "1000000000019",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF”,
        # “Breast, Prostate, Colorectal and Other Cancers and Tumors”, ], or [“CHF”, “Rheumatoid Arthritis and
        # Inflammatory Connective Tissue Disease”], or [“CHF”, “Breast, Prostate, Colorectal and Other Cancers and
        # Tumors”, “Rheumatoid Arthritis and Inflammatory Connective Tissue Disease”], or [“COPD”, “Breast, Prostate,
        # Colorectal and Other Cancers and Tumors”, ], or [“COPD”, “Rheumatoid Arthritis and Inflammatory Connective
        # Tissue Disease”], or [“COPD”, “Breast, Prostate, Colorectal and Other Cancers and Tumors”, “Rheumatoid
        # Arthritis and Inflammatory Connective Tissue Disease”], or [“Breast, Prostate, Colorectal and Other Cancers
        # and Tumors”, “Rheumatoid Arthritis and Inflammatory Connective Tissue Disease”]"
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-05'
    },
    'track_0005-06': {
        'memberpersonalgeneratedkey': "1000000000018",  # this needs a user with CHRONIC_CONDITION_DESC = [null],
        # or all other members not in HCC table"
        'phone_number': '2028997316',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-06'
    },

}

COHORT_LOGIC_PARAMS_002_003_005_006 = {
    'track_0006-01': {
        'memberpersonalgeneratedkey': "1000000000021",  # this needs a user with CHRONIC_CONDITION_DESC = ["Diabetes",
        # or ["Diabetes", ...]
        'phone_number': '4845020673',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-01',
        'reply_1': 'Y',
        'reply_2': '1',
        'fourth_track_id_value': '0006-01'

    },
    'track_0006-02': {
        'memberpersonalgeneratedkey': "1000000000022",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '4154170791',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-02',
        'reply_1': 'Y',
        'reply_2': '2',
        'fourth_track_id_value': '0006-02'
    },
    'track_0006-03': {
        'memberpersonalgeneratedkey': "1000000000025",  # this needs a user with CHRONIC_CONDITION_DESC =
        # [“Rheumatoid arthritis and inflammatory diseases"]
        'phone_number': '4159808528',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-03',
        'reply_1': 'Y',
        'reply_2': '3',
        'fourth_track_id_value': '0006-03'
    },
    'track_0006-04': {
        'memberpersonalgeneratedkey': "1000000000027",  # this needs a user with CHRONIC_CONDITION_DESC =
        # [“Breast, Prostate, Colorectal and Other Cancers and Tumors”]"
        'phone_number': '8177602161',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-04',
        'reply_1': 'Y',
        'reply_2': '4',
        'fourth_track_id_value': '0006-04'
    },
    'track_0006-05': {
        'memberpersonalgeneratedkey': "1000000000029",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF”,
        # “Breast, Prostate, Colorectal and Other Cancers and Tumors”, ], or [“CHF”, “Rheumatoid Arthritis and
        # Inflammatory Connective Tissue Disease”], or [“CHF”, “Breast, Prostate, Colorectal and Other Cancers and
        # Tumors”, “Rheumatoid Arthritis and Inflammatory Connective Tissue Disease”], or [“COPD”, “Breast, Prostate,
        # Colorectal and Other Cancers and Tumors”, ], or [“COPD”, “Rheumatoid Arthritis and Inflammatory Connective
        # Tissue Disease”], or [“COPD”, “Breast, Prostate, Colorectal and Other Cancers and Tumors”, “Rheumatoid
        # Arthritis and Inflammatory Connective Tissue Disease”], or [“Breast, Prostate, Colorectal and Other Cancers
        # and Tumors”, “Rheumatoid Arthritis and Inflammatory Connective Tissue Disease”]"
        'phone_number': '6124483552',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-05',
        'reply_1': 'Y',
        'reply_2': '5',
        'fourth_track_id_value': '0006-05'
    },
    'track_0006-06': {
        'memberpersonalgeneratedkey': "1000000000018",  # this needs a user with CHRONIC_CONDITION_DESC = [null],
        # or all other members not in HCC table"
        'phone_number': '6088889353',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-06',
        'reply_1': 'Y',
        'reply_2': '6',
        'fourth_track_id_value': '0006-06'
    },
    'track_0006-07': {
        'memberpersonalgeneratedkey': "1000000000023",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '4154170791',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-02',
        'reply_1': 'Y',
        'reply_2': '7',
        'fourth_track_id_value': '0006-07'
    },

}

COHORT_LOGIC_PARAMS_002_003_005_006_007 = {
    # 'track_0007-01': {
    #     'memberpersonalgeneratedkey': "1000000000021",  # this needs a user with CHRONIC_CONDITION_DESC = ["Diabetes",
    #     # or ["Diabetes", ...]
    #     'phone_number': '4152235628',
    #     'max_score': MAX_SCORE_VALUES['max_score_1'],
    #     'wait_time': 240,
    #     'first_track_id_value': '0002-01',
    #     'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
    #     'second_track_id_value': '0003-01',
    #     'third_track_id_value': '0005-01',
    #     'reply_1': 'Y',
    #     'reply_2': '1',
    #     'fourth_track_id_value': '0006-01',
    #     'wellness_answer_0006': WELLNESS_ANSWERS_0006['Answer 1'],
    #     'fifth_track_id_value': '0007-01'
    #
    # },
    'track_0007-02': {
        'memberpersonalgeneratedkey': "1000000000022",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '9049446547',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-02',
        'reply_1': 'Y',
        'reply_2': '2',
        'fourth_track_id_value': '0006-02',
        'wellness_answer_0006': WELLNESS_ANSWERS_0006['Answer 2'],
        'fifth_track_id_value': '0007-02'
    },
    'track_0007-03': {
        'memberpersonalgeneratedkey': "1000000000025",  # this needs a user with CHRONIC_CONDITION_DESC =
        # [“Rheumatoid arthritis and inflammatory diseases"]
        'phone_number': '8643514182',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-03',
        'reply_1': 'Y',
        'reply_2': '3',
        'fourth_track_id_value': '0006-03',
        'wellness_answer_0006': WELLNESS_ANSWERS_0006['Answer 3'],
        'fifth_track_id_value': '0007-03'
    },
    'track_0007-04': {
        'memberpersonalgeneratedkey': "1000000000027",  # this needs a user with CHRONIC_CONDITION_DESC =
        # [“Breast, Prostate, Colorectal and Other Cancers and Tumors”]"
        'phone_number': '2405585209',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-04',
        'reply_1': 'Y',
        'reply_2': '4',
        'fourth_track_id_value': '0006-04',
        'wellness_answer_0006': WELLNESS_ANSWERS_0006['Answer 4'],
        'fifth_track_id_value': '0007-04'
    },
    'track_0007-05': {
        'memberpersonalgeneratedkey': "1000000000029",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF”,
        # “Breast, Prostate, Colorectal and Other Cancers and Tumors”, ], or [“CHF”, “Rheumatoid Arthritis and
        # Inflammatory Connective Tissue Disease”], or [“CHF”, “Breast, Prostate, Colorectal and Other Cancers and
        # Tumors”, “Rheumatoid Arthritis and Inflammatory Connective Tissue Disease”], or [“COPD”, “Breast, Prostate,
        # Colorectal and Other Cancers and Tumors”, ], or [“COPD”, “Rheumatoid Arthritis and Inflammatory Connective
        # Tissue Disease”], or [“COPD”, “Breast, Prostate, Colorectal and Other Cancers and Tumors”, “Rheumatoid
        # Arthritis and Inflammatory Connective Tissue Disease”], or [“Breast, Prostate, Colorectal and Other Cancers
        # and Tumors”, “Rheumatoid Arthritis and Inflammatory Connective Tissue Disease”]"
        'phone_number': '4138893058',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-05',
        'reply_1': 'Y',
        'reply_2': '5',
        'fourth_track_id_value': '0006-05',
        'wellness_answer_0006': WELLNESS_ANSWERS_0006['Answer 5'],
        'fifth_track_id_value': '0007-05'
    },
    'track_0007-06': {
        'memberpersonalgeneratedkey': "1000000000028",  # this needs a user with CHRONIC_CONDITION_DESC = [null],
        # or all other members not in HCC table"
        'phone_number': '8173813339',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-06',
        'reply_1': 'Y',
        'reply_2': '6',
        'fourth_track_id_value': '0006-06',
        'wellness_answer_0006': WELLNESS_ANSWERS_0006['Answer 6'],
        'fifth_track_id_value': '0007-06'
    },

    'track_0007-07': {
        'memberpersonalgeneratedkey': "1000000000023",  # this needs a user with CHRONIC_CONDITION_DESC = [“CHF"] or
        # ["COPD”], or [ “CHF", "COPD”] or ["CHF", "COPD", ...]
        'phone_number': '5863152106',
        'max_score': MAX_SCORE_VALUES['max_score_1'],
        'wait_time': 240,
        'first_track_id_value': '0002-01',
        'wellness_answer_0002': WELLNESS_ANSWERS_0002['Answer 2'],
        'second_track_id_value': '0003-01',
        'third_track_id_value': '0005-02',
        'reply_1': 'Y',
        'reply_2': '7',
        'fourth_track_id_value': '0006-07',
        'wellness_answer_0006': WELLNESS_ANSWERS_0006['Answer 7'],
        'fifth_track_id_value': '0007-07'
    }

}


def test_cohort_logic_002(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002
    cohort = CohortLogic(browser)

    i = 0
    for x in COHORT_LOGIC_PARAMS_002:
        i = i + 1
        print('Test {} started.'.format(i))
        cohort.track_002(**track[x])


def test_cohort_logic_002_003(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002_003
    cohort = CohortLogic(browser)

    i = 0
    for x in COHORT_LOGIC_PARAMS_002_003:
        i = i + 1
        print('Test {} started.'.format(i))
        cohort.track_002_003(**track[x])


def test_cohort_logic_002_003_004(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002_003_004
    cohort = CohortLogic(browser)

    i = 0
    for x in COHORT_LOGIC_PARAMS_002_003_004:
        i = i + 1
        print('Test {} started.'.format(i))
        cohort.track_002_003_004(**track[x])


def test_cohort_logic_002_003_005(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002_003_005
    cohort = CohortLogic(browser)

    i = 0
    for x in COHORT_LOGIC_PARAMS_002_003_005:
        i = i + 1
        print('Test {} started.'.format(i))
        cohort.track_002_003_005(**track[x])


def test_cohort_logic_002_003_005_006(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002_003_005_006
    cohort = CohortLogic(browser)

    i = 0
    for x in COHORT_LOGIC_PARAMS_002_003_005_006:
        i = i + 1
        print('Test {} started.'.format(i))
        cohort.track_002_003_005_006(**track[x])


def test_cohort_logic_002_003_005_006_007(browser, track=None):
    if track is None:
        track = COHORT_LOGIC_PARAMS_002_003_005_006_007
    cohort = CohortLogic(browser)

    i = 0
    for x in COHORT_LOGIC_PARAMS_002_003_005_006_007:
        i = i + 1
        print('Test {} started.'.format(i))
        cohort.track_002_003_005_006_007(**track[x])
