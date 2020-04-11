import csv

from terminaltables import AsciiTable

from app.entities.constants import ConsoleColor


class PrettyPrint:
    """Static utility class to handle console output related functions"""

    @classmethod
    def print_colorful(cls, message, foreground_color=ConsoleColor.OFF, background_color=ConsoleColor.BG_BLACK):
        """
        Utility function to print a message to console screen.
        :param message: message to output
        :param foreground_color: font color
        :param background_color: console background color
        :return: nothing
        """
        print("{bg_color}{fg_color}{msg}{color_reset}".format(bg_color=background_color, fg_color=foreground_color,
                                                              msg=message, color_reset=ConsoleColor.OFF))

    @staticmethod
    def info(msg):
        """
        Prints information message to console
        :param msg: string message
        :return: nothing
        """
        PrettyPrint.print_colorful(msg)

    @staticmethod
    def error(msg):
        """
        Prints error message to console
        :param msg: string message
        :return: nothing
        """
        PrettyPrint.print_colorful("\n{msg}\n".format(msg=msg), foreground_color=ConsoleColor.BOLD_RED,
                                   background_color=ConsoleColor.INTENSE_BLACK)

    @staticmethod
    def success(msg):
        """
        Prints success message to console
        :param msg: string message
        :return: nothing
        """
        PrettyPrint.print_colorful("\n{msg}\n".format(msg=msg), foreground_color=ConsoleColor.BOLD_GREEN,
                                   background_color=ConsoleColor.INTENSE_BLACK)

    @staticmethod
    def warn(msg):
        """
        Prints success message to console
        :param msg: string message
        :return: nothing
        """
        PrettyPrint.print_colorful("WARNING: {msg}".format(msg=msg), foreground_color=ConsoleColor.BOLD_YELLOW,
                                   background_color=ConsoleColor.BG_WHITE)

    @staticmethod
    def tabular(heading, table_array):
        """
        Prints table in console.
        :param heading: list of heading title
        :param table_array: 2 dims array representing table.
        :return:
        """
        data = [heading, ]
        data.extend(table_array)

        table = AsciiTable(data)

        print(table.table)


def read_csv_file(file_path):
    """
    Function to read a file
    :param file_path: path to file
    :return:
    """
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        lines = []
        for line in csv_reader:
            lines.append(line)

        return lines[1:]


def get_values_of_dict(dictionary):
    """
    Utility function that convert dictionary to list of values present in it.
    :param dictionary: dictionary
    :return: list of values in dict
    """

    values = []
    for i in dictionary:
        values.append(dictionary[i])

    return values
