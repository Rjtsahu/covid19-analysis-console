class AppBaseException(Exception):
    """
    Base class to handle all sort of known exception.
    Any custom exception must inherit this.
    """

    def __init__(self, message='unknown error'):
        super().__init__()
        self.message = message

    def __str__(self):
        return "error message : %s " % (self.message,)


class InvalidInputException(AppBaseException):
    """
    Exception class to handle all invalid inputs that are taken from console.
    """

    def __init__(self, message="Invalid input entered"):
        super().__init__()
        self.message = message
