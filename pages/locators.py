CSS_SELECTORS = {
    # here we will add selectors used for the project
    # eg:
    # 'example_button' : 'div[class = 'sl-button-wrapper']'

    # this is the css selector used for the header "Back" button
    "header_back": "button[class='button button--back header__back']",

    # this is the css selector used for the "Next" button in the card pages footer
    "footer_cards_next": "button[class='button button--arrow footer-cards__button']",

    # this is the css selector used for the "Next" button in non card pages
    "footer_next": "button[class='button button--arrow footer-purple__btn']",

    # this is the css selector used for the Month DOB input field
    "month_input": "input[placeholder='MM']",

    # this is the css selector used for the Year DOB input field
    "year_input": "input[placeholder='YYYY']",

    # this is the css selector used for the Day DOB input field
    "day_input": "input[placeholder='DD']",

    # this is the css selector used for the "take a Survey" wrapper
    "take_a_survey": "div[class='wrapper canvas__survey__wrapper']",

    # this is the css selector used for the text input field
    "text_input": "textarea[class='inline-input']",

    # this is the css selector used for the phone number input field
    "phone_input": "input[type='tel']",

    # this is the css selector used for the radio buttons options
    "radio_option": "div[class='activity__button']",

    # this is the css selector used for checkboxes
    "checkbox": "div[class='checkbox__box']",

    # this is the css selector used for the "Create My Profile" button
    "create_my_profile_button": "button[type='submit']",

    # this is the css selector used for the "Save and exit" header button
    "header_save": "button[class='button header__save']",

    # this is the css selector used for the SMS tool header
    'sms_tool_header': "h2[class='heading-section']",

    # this is the css selector used for the SMS reply input field
    'sms_reply': "input[type='text']"
}
CSS_SELECTORS_LIFEMAP_CARDS = {
    # these are the  css selectors used for activity cards
    "activity_card_1": "[aria-labelledby='name__1']",
    "activity_card_2": "[aria-labelledby='name__2']",
    "activity_card_3": "[aria-labelledby='name__3']",
    "activity_card_4": "[aria-labelledby='name__4']",
    "activity_card_5": "[aria-labelledby='name__5']",
    "activity_card_6": "[aria-labelledby='name__6']",
    "activity_card_7": "[aria-labelledby='name__7']",
    "activity_card_8": "[aria-labelledby='name__8']",
    "activity_card_9": "[aria-labelledby='name__9']",
    "activity_card_10": "[aria-labelledby='name__10']",
    "activity_card_11": "[aria-labelledby='name__11']",
    "activity_card_12": "[aria-labelledby='name__12']",
    "activity_card_13": "[aria-labelledby='name__13']",
    "activity_card_14": "[aria-labelledby='name__14']",
    "activity_card_15": "[aria-labelledby='name__15']",
    "activity_card_16": "[aria-labelledby='name__16']",
    "activity_card_17": "[aria-labelledby='name__17']",
    "activity_card_18": "[aria-labelledby='name__18']",
    "activity_card_19": "[aria-labelledby='name__19']",
    "activity_card_20": "[aria-labelledby='name__20']",
    "activity_card_21": "[aria-labelledby='name__21']",
    "activity_card_22": "[aria-labelledby='name__22']",
    "activity_card_23": "[aria-labelledby='name__23']",
    "activity_card_24": "[aria-labelledby='name__24']",
    "activity_card_25": "[aria-labelledby='name__25']",
    "activity_card_26": "[aria-labelledby='name__26']",
    "activity_card_27": "[aria-labelledby='name__27']",
    "activity_card_28": "[aria-labelledby='name__28']",
    "activity_card_29": "[aria-labelledby='name__29']",
    "activity_card_30": "[aria-labelledby='name__30']",
    "activity_card_31": "[aria-labelledby='name__31']",
    "activity_card_32": "[aria-labelledby='name__32']"
}

CARDS_XPATHS = {
    # category: talents
    "Adding Humor": "//figcaption[normalize-space(span)='Adding Humor']/../..",
    "Advancing Ideas": "//figcaption[normalize-space(span)='Advancing Ideas']/../..",
    "Analyzing Information": "//figcaption[normalize-space(span)='Analyzing Information']/../..",
    "Breaking Molds": "//figcaption[normalize-space(span)='Breaking Molds']/../..",
    "Bringing Joy": "//figcaption[normalize-space(span)='Bringing Joy']/../..",
    "Building Friendships": "//figcaption[normalize-space(span)='Building Friendships']/../..",
    "Building Things": "//figcaption[normalize-space(span)='Building Things']/../..",
    "Caring for Others": "//figcaption[normalize-space(span)='Caring for Others']/../..",
    "Creating Things": "//figcaption[normalize-space(span)='Creating Things']/../..",
    "Empowering Others": "//figcaption[normalize-space(span)='Empowering Others']/../..",
    "Exploring the Way": "//figcaption[normalize-space(span)='Exploring the Way']/../..",
    "Fixing Things": "//figcaption[normalize-space(span)='Fixing Things']/../..",
    "Getting Participation": "//figcaption[normalize-space(span)='Getting Participation']/../..",
    "Growing Things": "//figcaption[normalize-space(span)='Growing Things']/../..",
    "Healing Others": "//figcaption[normalize-space(span)='Healing Others']/../..",
    "Instructing People": "//figcaption[normalize-space(span)='Instructing People']/../..",
    "Making Connections": "//figcaption[normalize-space(span)='Making Connections']/../..",
    "Making Sense of Numbers": "//figcaption[normalize-space(span)='Making Sense of Numbers']/../..",
    "Motivating People": "//figcaption[normalize-space(span)='Motivating People']/../..",
    "Organizing Things": "//figcaption[normalize-space(span)='Organizing Things']/../..",
    "Overcoming Obstacles": "//figcaption[normalize-space(span)='Overcoming Obstacles']/../..",
    "Researching Things": "//figcaption[normalize-space(span)='Researching Things']/../..",
    "Resolving Disputes": "//figcaption[normalize-space(span)='Resolving Disputes']/../..",
    "Seeing the Big Picture": "//figcaption[normalize-space(span)='Seeing the Big Picture']/../..",
    "Solving Problems": "//figcaption[normalize-space(span)='Solving Problems']/../..",
    "Speaking to People": "//figcaption[normalize-space(span)='Speaking to People']/../..",
    "Staying Active": "//figcaption[normalize-space(span)='Staying Active']/../..",
    "Staying Current": "//figcaption[normalize-space(span)='Staying Current']/../..",
    "Translating Things": "//figcaption[normalize-space(span)='Translating Things']/../..",

    # category: talents
    "Animals": "//figcaption[normalize-space(span)='Animals']/../..",
    "Art": "//figcaption[normalize-space(span)='Art']/../..",
    "Crafts": "//figcaption[normalize-space(span)='Crafts']/../..",
    "Culture": "//figcaption[normalize-space(span)='Culture']/../..",
    "Dance": "//figcaption[normalize-space(span)='Dance']/../..",
    "Education": "//figcaption[normalize-space(span)='Education']/../..",
    "Entertaining": "//figcaption[normalize-space(span)='Entertaining']/../..",
    "Fashion": "//figcaption[normalize-space(span)='Fashion']/../..",
    "Finance": "//figcaption[normalize-space(span)='Finance']/../..",
    "Fitness": "//figcaption[normalize-space(span)='Fitness']/../..",
    "Food": "//figcaption[normalize-space(span)='Food']/../..",
    "Gardening": "//figcaption[normalize-space(span)='Gardening']/../..",
    "Homemaking": "//figcaption[normalize-space(span)='Homemaking']/../..",
    "Literature": "//figcaption[normalize-space(span)='Literature']/../..",
    "Music": "//figcaption[normalize-space(span)='Music']/../..",
    "Outdoors": "//figcaption[normalize-space(span)='Outdoors']/../..",
    "Photography": "//figcaption[normalize-space(span)='Photography']/../..",
    "Politics": "//figcaption[normalize-space(span)='Politics']/../..",
    "Social Media": "//figcaption[normalize-space(span)='Social Media']/../..",
    "Socializing": "//figcaption[normalize-space(span)='Socializing']/../..",
    "Spirituality": "//figcaption[normalize-space(span)='Spirituality']/../..",
    "Sports": "//figcaption[normalize-space(span)='Sports']/../..",
    "Traveling": "//figcaption[normalize-space(span)='Traveling']/../..",
    "Volunteering": "//figcaption[normalize-space(span)='Volunteering']/../..",
    "Well-Being": "//figcaption[normalize-space(span)='Well-Being']/../..",
    "Work": "//figcaption[normalize-space(span)='Work']/../..",
    "Writing": "//figcaption[normalize-space(span)='Writing']/../..",

    # category: impacts
    "Children": "//figcaption[normalize-space(span)='Children']/../..",
    "My Clients": "//figcaption[normalize-space(span)='My Clients']/../..",
    "My Community": "//figcaption[normalize-space(span)='My Community']/../..",
    "My Country": "//figcaption[normalize-space(span)='My Country']/../..",
    "My Family": "//figcaption[normalize-space(span)='My Family']/../..",
    "My Friends": "//figcaption[normalize-space(span)='My Friends']/../..",
    "My Personal Growth": "//figcaption[normalize-space(span)='My Personal Growth']/../..",
    "My Spiritual Group": "//figcaption[normalize-space(span)='My Spiritual Group']/../..",
    "My Team": "//figcaption[normalize-space(span)='My Team']/../..",
    "My Work": "//figcaption[normalize-space(span)='My Work']/../..",
    "The Environment": "//figcaption[normalize-space(span)='The Environment']/../..",
    "The Less Fortunate": "//figcaption[normalize-space(span)='The Less Fortunate']/../..",

    # category: values
    "Belonging": "//figcaption[normalize-space(span)='Belonging']/../..",
    "Commitment": "//figcaption[normalize-space(span)='Commitment']/../..",
    "Compassion": "//figcaption[normalize-space(span)='Compassion']/../..",
    "Consistency": "//figcaption[normalize-space(span)='Consistency']/../..",
    "Curiosity": "//figcaption[normalize-space(span)='Curiosity']/../..",
    "Empathy": "//figcaption[normalize-space(span)='Empathy']/../..",
    "Equality": "//figcaption[normalize-space(span)='Equality']/../..",
    "Excellence": "//figcaption[normalize-space(span)='Excellence']/../..",
    "Excitement": "//figcaption[normalize-space(span)='Excitement']/../..",
    "Faith": "//figcaption[normalize-space(span)='Faith']/../..",
    "Freedom": "//figcaption[normalize-space(span)='Freedom']/../..",
    "Generosity": "//figcaption[normalize-space(span)='Generosity']/../..",
    "Health": "//figcaption[normalize-space(span)='Health']/../..",
    "Honesty": "//figcaption[normalize-space(span)='Honesty']/../..",
    "Independence": "//figcaption[normalize-space(span)='Independence']/../..",
    "Leadership": "//figcaption[normalize-space(span)='Leadership']/../..",
    "Loyalty": "//figcaption[normalize-space(span)='Loyalty']/../..",
    "Peace": "//figcaption[normalize-space(span)='Peace']/../..",
    "Relationships": "//figcaption[normalize-space(span)='Relationships']/../..",
    "Risk-Taking": "//figcaption[normalize-space(span)='Risk-Taking']/../..",
    "Security": "//figcaption[normalize-space(span)='Security']/../..",
    "Self-Discipline": "//figcaption[normalize-space(span)='Self-Discipline']/../..",
    "Tolerance": "//figcaption[normalize-space(span)='Tolerance']/../..",
    "Tradition": "//figcaption[normalize-space(span)='Tradition']/../..",
    "Trust": "//figcaption[normalize-space(span)='Trust']/../..",
    "Wisdom": "//figcaption[normalize-space(span)='Wisdom']/../..",

    # category: goals
    "I Want to Be Active": "//figcaption[normalize-space(span)='I Want to Be Active']/../..",
    "I Want to Be Appreciated": "//figcaption[normalize-space(span)='I Want to Be Appreciated']/../..",
    "I Want to Be Calm": "//figcaption[normalize-space(span)='I Want to Be Calm']/../..",
    "I Want to Be Challenged": "//figcaption[normalize-space(span)='I Want to Be Challenged']/../..",
    "I Want to Be Connected": "//figcaption[normalize-space(span)='I Want to Be Connected']/../..",
    "I Want to Be Creative": "//figcaption[normalize-space(span)='I Want to Be Creative']/../..",
    "I Want to Be Fulfilled": "//figcaption[normalize-space(span)='I Want to Be Fulfilled']/../..",
    "I Want to Be Happy": "//figcaption[normalize-space(span)='I Want to Be Happy']/../..",
    "I Want to Be Healthy": "//figcaption[normalize-space(span)='I Want to Be Healthy']/../..",
    "I Want to Be Independent": "//figcaption[normalize-space(span)='I Want to Be Independent']/../..",
    "I Want to Be Inventive": "//figcaption[normalize-space(span)='I Want to Be Inventive']/../..",
    "I Want to Be Loved": "//figcaption[normalize-space(span)='I Want to Be Loved']/../..",
    "I Want to Be Purpose-Driven": "//figcaption[normalize-space(span)='I Want to Be Purpose-Driven']/../..",
    "I Want to Be Successful": "//figcaption[normalize-space(span)='I Want to Be Successful']/../..",
    "I Want to Be Supported": "//figcaption[normalize-space(span)='I Want to Be Supported']/../..",
    "I Want to Feel Excited": "//figcaption[normalize-space(span)='I Want to Feel Excited']/../..",
    "I Want to Feel in Control": "//figcaption[normalize-space(span)='I Want to Feel in Control']/../..",
    "I Want to Feel More Capable": "//figcaption[normalize-space(span)='I Want to Feel More Capable']/../..",
    "I Want to Feel More Confident": "//figcaption[normalize-space(span)='I Want to Feel More Confident']/../..",
    "I Want to Feel More Energetic": "//figcaption[normalize-space(span)='I Want to Feel More Energetic']/../..",
    "I Want to Feel More Joyful": "//figcaption[normalize-space(span)='I Want to Feel More Joyful']/../..",
    "I Want to Feel Safe": "//figcaption[normalize-space(span)='I Want to Feel Safe']/../..",
    "I Want to Have More Time for Me": "//figcaption[normalize-space(span)='I Want to Have More Time for Me']/../..",
    "I Want to Have More Time with My Family": "//figcaption[normalize-space(span)='I Want to Have More Time with My "
                                               "Family']/../..",
    "I Want to Have Stronger Friendships": "//figcaption[normalize-space(span)='I Want to Have Stronger "
                                           "Friendships']/../.."
}

TYPE_0_TALENTS = [CARDS_XPATHS["Breaking Molds"]]
TYPE_0_PASSIONS = []
TYPE_0_IMPACTS = []
TYPE_0_VALUES = [CARDS_XPATHS["Excitement"], CARDS_XPATHS["Independence"]]
TYPE_0_GOALS = [CARDS_XPATHS["I Want to Be Challenged"], CARDS_XPATHS["I Want to Be Happy"],
                CARDS_XPATHS["I Want to Be Healthy"], CARDS_XPATHS["I Want to Be Independent"],
                CARDS_XPATHS["I Want to Feel Excited"]]

TYPE_1_TALENTS = [CARDS_XPATHS["Adding Humor"], CARDS_XPATHS["Bringing Joy"], CARDS_XPATHS["Building Friendships"],
                  CARDS_XPATHS["Empowering Others"], CARDS_XPATHS["Getting Participation"],
                  CARDS_XPATHS["Making Connections"], CARDS_XPATHS["Motivating People"],
                  CARDS_XPATHS["Resolving Disputes"], CARDS_XPATHS["Speaking to People"]]
TYPE_1_PASSIONS = [CARDS_XPATHS["Entertaining"], CARDS_XPATHS["Social Media"], CARDS_XPATHS["Socializing"]]
TYPE_1_IMPACTS = [CARDS_XPATHS["Children"], CARDS_XPATHS["My Community"], CARDS_XPATHS["My Country"],
                  CARDS_XPATHS["My Family"], CARDS_XPATHS["My Friends"], CARDS_XPATHS["My Team"]]
TYPE_1_VALUES = [CARDS_XPATHS["Belonging"], CARDS_XPATHS["Generosity"], CARDS_XPATHS["Loyalty"],
                 CARDS_XPATHS["Relationships"], CARDS_XPATHS["Tolerance"], CARDS_XPATHS["Trust"]]
TYPE_1_GOALS = [CARDS_XPATHS["I Want to Be Appreciated"], CARDS_XPATHS["I Want to Be Connected"],
                CARDS_XPATHS["I Want to Be Loved"], CARDS_XPATHS["I Want to Be Supported"],
                CARDS_XPATHS["I Want to Feel Safe"], CARDS_XPATHS["I Want to Have More Time with My Family"],
                CARDS_XPATHS["I Want to Have Stronger Friendships"]]

TYPE_2_TALENTS = [CARDS_XPATHS["Caring for Others"], CARDS_XPATHS["Growing Things"], CARDS_XPATHS["Healing Others"],
                  CARDS_XPATHS["Overcoming Obstacles"], CARDS_XPATHS["Seeing the Big Picture"]]
TYPE_2_PASSIONS = [CARDS_XPATHS["Animals"], CARDS_XPATHS["Art"], CARDS_XPATHS["Food"], CARDS_XPATHS["Gardening"],
                   CARDS_XPATHS["Music"], CARDS_XPATHS["Photography"], CARDS_XPATHS["Spirituality"],
                   CARDS_XPATHS["Volunteering"], CARDS_XPATHS["Well-Being"]]
TYPE_2_IMPACTS = [CARDS_XPATHS["My Personal Growth"], CARDS_XPATHS["My Spiritual Group"],
                  CARDS_XPATHS["The Less Fortunate"]]
TYPE_2_VALUES = [CARDS_XPATHS["Compassion"], CARDS_XPATHS["Empathy"], CARDS_XPATHS["Equality"], CARDS_XPATHS["Faith"],
                 CARDS_XPATHS["Health"], CARDS_XPATHS["Honesty"], CARDS_XPATHS["Peace"], CARDS_XPATHS["Security"],
                 CARDS_XPATHS["Self-Discipline"]]
TYPE_2_GOALS = [CARDS_XPATHS["I Want to Be Calm"], CARDS_XPATHS["I Want to Be Purpose-Driven"],
                CARDS_XPATHS["I Want to Feel in Control"], CARDS_XPATHS["I Want to Feel More Confident"],
                CARDS_XPATHS["I Want to Feel More Joyful"], CARDS_XPATHS["I Want to Have More Time for Me"]]

TYPE_3_TALENTS = [CARDS_XPATHS["Advancing Ideas"], CARDS_XPATHS["Analyzing Information"],
                  CARDS_XPATHS["Creating Things"], CARDS_XPATHS["Exploring the Way"],
                  CARDS_XPATHS["Instructing People"], CARDS_XPATHS["Making Sense of Numbers"],
                  CARDS_XPATHS["Researching Things"], CARDS_XPATHS["Solving Problems"],
                  CARDS_XPATHS["Translating Things"]]
TYPE_3_PASSIONS = [CARDS_XPATHS["Culture"], CARDS_XPATHS["Education"], CARDS_XPATHS["Fashion"], CARDS_XPATHS["Finance"],
                   CARDS_XPATHS["Literature"], CARDS_XPATHS["Politics"], CARDS_XPATHS["Writing"]]
TYPE_3_IMPACTS = []
TYPE_3_VALUES = [CARDS_XPATHS["Curiosity"], CARDS_XPATHS["Excellence"], CARDS_XPATHS["Tradition"],
                 CARDS_XPATHS["Wisdom"]]
TYPE_3_GOALS = [CARDS_XPATHS["I Want to Be Creative"], CARDS_XPATHS["I Want to Be Inventive"]]

TYPE_4_TALENTS = [CARDS_XPATHS["Building Things"], CARDS_XPATHS["Fixing Things"], CARDS_XPATHS["Organizing Things"],
                  CARDS_XPATHS["Staying Active"], CARDS_XPATHS["Staying Current"]]
TYPE_4_PASSIONS = [CARDS_XPATHS["Crafts"], CARDS_XPATHS["Dance"], CARDS_XPATHS["Fitness"], CARDS_XPATHS["Homemaking"],
                   CARDS_XPATHS["Outdoors"], CARDS_XPATHS["Sports"], CARDS_XPATHS["Traveling"], CARDS_XPATHS["Work"]]
TYPE_4_IMPACTS = [CARDS_XPATHS["My Clients"], CARDS_XPATHS["My Work"], CARDS_XPATHS["The Environment"]]
TYPE_4_VALUES = [CARDS_XPATHS["Commitment"], CARDS_XPATHS["Consistency"], CARDS_XPATHS["Freedom"],
                 CARDS_XPATHS["Leadership"], CARDS_XPATHS["Risk-Taking"]]
TYPE_4_GOALS = [CARDS_XPATHS["I Want to Be Active"], CARDS_XPATHS["I Want to Be Fulfilled"],
                CARDS_XPATHS["I Want to Be Successful"], CARDS_XPATHS["I Want to Feel More Capable"],
                CARDS_XPATHS["I Want to Feel More Energetic"]]

WELLNESS_CATEGORIES_CSS_SELECTORS_0002 = {
    'Mental Health': "div[tabindex='2']",
    'Healthy eating': "div[tabindex='3']",
    'Social well-being': "div[tabindex='4']",
    'Exercise': "div[tabindex='5']",
    'Putting my talents to work': "div[tabindex='6']",
    'I don"t have a goal yet': "div[tabindex='7']",
    'None of these': "div[tabindex='8']"
}

WELLNESS_CATEGORIES_CSS_SELECTORS_0006 = {
    'Not enough time': "div[tabindex='2']",
    'Lack of support': "div[tabindex='3']",
    'Can’t find the energy': "div[tabindex='4']",
    'I’m not confident I can do it': "div[tabindex='5']",
    'Need more information': "div[tabindex='6']",
    'Cost is too much': "div[tabindex='7']",
    'My barrier is not on this list': "div[tabindex='8']",
    'I don’t have any barriers right now': "div[tabindex='9']"
}

