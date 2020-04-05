PAGE_SIZE = 20

CSV_FILE_PATH = './covid_19_data.csv'


class ConsoleColor:
    """
    Constant class to hold commonly used console colors include normal bold and background colors
    """
    RED = '\033[91m {}\033[00m'
    GREEN = '\033[92m {}\033[00m'

    OFF = '\033[0m'

    BOLD_RED = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    BOLD_YELLOW = '\033[1;33m'

    BG_BLACK = '\033[40m'
    BG_GREEN = '\033[42m'
    BG_WHITE = '\033[47m'

    INTENSE_BLACK = '\033[0;90m'
