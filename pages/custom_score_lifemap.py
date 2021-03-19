from pages.base_element import BaseElement
from pages.base_page import BasePage
from pages.locators import CSS_SELECTORS, CARDS_XPATHS, TYPE_1, TYPE_0, TYPE_1_TALENTS, TYPE_0_TALENTS, \
    CSS_SELECTORS_LIFEMAP_CARDS, TYPE_0_PASSIONS, TYPE_1_PASSIONS, TYPE_0_IMPACTS, TYPE_1_IMPACTS, TYPE_1_VALUES, \
    TYPE_0_VALUES, TYPE_2_PASSIONS, TYPE_0_GOALS, TYPE_1_GOALS
from pages.mongo_db import Connect, DATABASE_CONNECTION_STRINGS, DATABASE_KEYS


class CustomLifemapScore:

    def __init__(self, browser, base_element):
        self.browser = browser
        self.base_element = BaseElement(browser)

    def custom_score(self, main_talents, secondary_talents, main_passions, secondary_passions,
                     main_impacts, secondary_impacts, main_values, secondary_values, main_goals, secondary_goals):
        # talents
        self.base_element.custom_card_selector(main_card_type=main_talents,
                                               secondary_card_type=secondary_talents,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS['header_save'])

        self.base_element.custom_card_selector(main_card_type=main_talents,
                                               secondary_card_type=secondary_talents,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        # passions
        self.base_element.custom_card_selector(main_card_type=main_passions,
                                               secondary_card_type=secondary_passions,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        self.base_element.custom_card_selector(main_card_type=main_passions,
                                               secondary_card_type=secondary_passions,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_2'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        # impacts
        self.base_element.custom_card_selector(main_card_type=main_impacts,
                                               secondary_card_type=secondary_impacts,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        self.base_element.custom_card_selector(main_card_type=main_impacts,
                                               secondary_card_type=secondary_impacts,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        # values
        self.base_element.custom_card_selector(main_card_type=main_values,
                                               secondary_card_type=secondary_values,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        self.base_element.custom_card_selector(main_card_type=main_values,
                                               secondary_card_type=secondary_values,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        # goals
        self.base_element.custom_card_selector(main_card_type=main_goals,
                                               secondary_card_type=secondary_goals,
                                               minimum_selection_number=5,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS_LIFEMAP_CARDS['activity_card_1'])

        self.base_element.custom_card_selector(main_card_type=main_goals,
                                               secondary_card_type=secondary_goals,
                                               minimum_selection_number=3,
                                               wait_element=CSS_SELECTORS['header_save'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_cards_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])
        self.base_element.button_click(button_selector=CSS_SELECTORS['footer_next'],
                                       wait_element=CSS_SELECTORS['footer_next'])
