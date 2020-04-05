import inspect
from types import FunctionType
from typing import List, Type

from app.entities.option import ConsoleOption
from app.services.analysis_service import AnalysisService
from app.services.dispatching import BaseConsoleDispatcher
from app.utils import Pretty


def dispatch_request(arguments):
    print('got arguments ', arguments)


class ConsoleRequest(object):
    executable_services: List[Type[BaseConsoleDispatcher]] = [AnalysisService]

    def __init__(self):
        self._action_mapping: dict[ConsoleOption] = {}
        self.__setup__()

    def __setup__(self):
        for service in self.executable_services:
            if inspect.isclass(service):
                for option in service().get_options():
                    self.register_option(option)

    def register_option(self, option: ConsoleOption):

        if isinstance(action, FunctionType):
            self._action_mapping[key] = action
        else:
            Pretty.warn('Cannot register action, not a function.')

    def register_action(self, action):

        if isinstance(action, FunctionType):
            self._action_mapping[key] = action
        else:
            Pretty.warn('Cannot register action, not a function.')
