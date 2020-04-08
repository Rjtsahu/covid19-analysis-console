import inspect
from types import FunctionType, MethodType
from typing import List, Type

from app.entities.constants import ConsoleColor
from app.entities.option import ConsoleOption
from app.exceptions.console_exceptions import AppBaseException
from app.services.analysis_service import AnalysisService
from app.services.dispatching import BaseConsoleDispatcher
from app.utils import PrettyPrint


def dispatch_request(arguments):
    """
    Entry function to look for incoming request on console and continues to execute request
    until a explicit terminated.
    :param arguments: list of arguments passed from console.
    :return: nothing
    """

    def proceed(request):
        """
        Internal function to dispatch a console-request after parsing argument's
        If operation key is not present then ignores to dispatch.
        At last prints usage summary.
        :param request: instance of console_request
        :return: nothing
        """

        key, args = request.parse_args(arguments)

        if key:
            request.dispatch_request(key, *args)

        request.print_usage_summary()

    console_request = ConsoleRequest()

    proceed(console_request)

    while True:

        try:
            arguments = input().split(' ')
        except KeyboardInterrupt:
            PrettyPrint.error(' Keyboard interrupt detected.')
            break

        proceed(console_request)


def exit_action():
    PrettyPrint.success('Exiting from app.')
    exit(0)


class ConsoleRequest(object):
    executable_services: List[Type[BaseConsoleDispatcher]] = [AnalysisService]
    exit_option = ConsoleOption(title='Exits from app.', invoke_key='exit',
                                action=exit_action)

    def __init__(self):
        self._action_mapping: dict[ConsoleOption] = {}
        self.usage_instructions = []
        self.__setup__()

    def __setup__(self):

        for service in self.executable_services:
            if inspect.isclass(service):
                for option in service().get_options():
                    self.register_option(option)

        self.register_option(self.exit_option)

    def get_usage_summary(self):
        return "            ***** COVID 19 POC ***** \n\n App Usage \n\n{data}".format(
            data="\n".join(self.usage_instructions))

    def print_usage_summary(self):
        PrettyPrint.print_colorful(self.get_usage_summary(), foreground_color=ConsoleColor.BOLD_YELLOW,
                                   background_color=ConsoleColor.BG_BLACK)

    def register_option(self, option: ConsoleOption):

        if self.register_action(option.invoke_key, option.action):
            self.usage_instructions.append(option.get_usage_description())

    def register_action(self, key, action):

        if not isinstance(action, (FunctionType, MethodType)):
            PrettyPrint.warn('Cannot register action, not a function.')
            return False
        if key in self._action_mapping:
            PrettyPrint.warn('Mapping of key: {key} already exists replacing with new action.'.format(key=key))

        self._action_mapping[key] = action

        return True

    def dispatch_request(self, key, *args):
        try:
            if key not in self._action_mapping:
                PrettyPrint.error("No action associated to operation key: {key}".format(key=key))
                return False

            self._action_mapping[key](*args)

            return True

        except TypeError as e:
            PrettyPrint.error("Input argument {error} key: {key}".format(error=e, key=key))
        except AppBaseException as e:
            PrettyPrint.error("Error {error} key: {key}".format(error=e, key=key))
        except Exception as e:
            PrettyPrint.error("Unhandled error {error} key: {key}".format(error=e, key=key))

        return False

    @classmethod
    def parse_args(cls, arguments):
        key, args = None, []

        if len(arguments) >= 1:
            key = arguments[0]

        if len(arguments) > 1:
            args = arguments[1:]

        return key, args
