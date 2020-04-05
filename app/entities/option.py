class ConsoleOption(object):

    def __init__(self, title='', invoke_key=None, action=None):
        self.title = title
        self.description = None
        self.invoke_key = str(invoke_key)
        self.action = action

    def get_usage_description(self):
        return "{key} : {title} \n {description}".format(key=self.invoke_key, title=self.title,
                                                         description=self.description)
