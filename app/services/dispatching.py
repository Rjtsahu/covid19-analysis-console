from typing import List

from app.entities.option import ConsoleOption


class BaseConsoleDispatcher(object):

    def get_options(self) -> List[ConsoleOption]:
        """Abstract method need to override"""
        raise Exception('This needs to override.')
