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
        LOGIN = "1"
        POSTS = '2'
        ADDR = '3'

        TEST_MENU = {
            TYPE: MENU,
            TITLE: MAIN_MENU,
            DEFAULT: CONTINUE,
            CHOICES: {
                CONTINUE: {
                    URL: 'api/main_menu',
                    METHOD: 'get',
                    TEXT: "Continue displaying menu"
                },
                LOGIN: {
                    URL: 'api/loggedin',
                    METHOD: 'get',
                    TEXT: "Login with google"
                },
                POSTS: {
                    URL: 'api/posts',
                    METHOD: 'get',
                    TEXT: "Get all posts"
                },
                ADDR: {
                    URL: 'api/addr',
                    METHOD: 'get',
                    TEXT: "Get all addresses"
                },
                EXIT: {
                    METHOD: 'get',
                    TEXT: "Exit"
                }
            }
        }
