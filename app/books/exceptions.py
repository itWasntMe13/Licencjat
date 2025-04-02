class TooLongName(Exception):
    def __init__(self, message="Too long name"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{type(self).__name__}: {self.message}"


class HTMLResponse(Exception):
    def __init__(self, message="HTML response from API"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{type(self).__name__}: {self.message}"
