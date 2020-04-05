from app.entities.option import ConsoleOption
from app.services.dispatching import BaseConsoleDispatcher


class AnalysisService(BaseConsoleDispatcher):

    def print_test(self, args):
        print('test func', args)

    def get_options(self):
        return [ConsoleOption(
            title='test func', invoke_key=0, action=self.print_test)
        ]
