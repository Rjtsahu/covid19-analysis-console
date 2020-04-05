class ConsoleOption(object):

    def __init__(self, title='', invoke_key=None, action=None):
        self.title = title
        self.description = None
        self.invoke_key = str(invoke_key)
        self.action = action

    def get_usage_description(self):

        if self.description is None:
            description = "No details provided."
        else:
            description = self.description

        return "{key} : {title} \n     {description} \n".format(key=self.invoke_key, title=self.title,
                                                                description=description)
