
class ERROR(Exception):
    def __init__(self, error_type, message) -> None:
        super().__init__(error_type, message)
        self.error_type = error_type
        self.message = message

    def getERROR(self):
        message = {self.error_type: self.message}

        return message