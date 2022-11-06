class Constants:
    STATIC_FOLDER = 'frontend/build'

    class Menu:
        FUNC = 'func'
        TEXT = 'text'
        URL = 'url'
        METHOD = 'method'
        TITLE = 'Title'
        TYPE = 'Type'
        MENU = 'Menu'
        FORM = 'Form'
        DATA = 'Data'
        MAIN_MENU = 'Main Menu'
        DEFAULT = 'Default'
        CHOICES = 'Choices'
        CONTINUE = '0'
        EXIT = 'X'

        TEST_MENU = {
            TYPE: MENU,
            TITLE: MAIN_MENU,
            DEFAULT: CONTINUE,
            CHOICES: {
                CONTINUE: {
                    URL: '/main_menu',
                    METHOD: 'GET',
                    TEXT: "Continue displaying menu"
                },
                EXIT: {
                    METHOD: 'GET',
                    TEXT: "Exit"
                }
            }
        }