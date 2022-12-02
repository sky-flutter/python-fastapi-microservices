class Error(Exception):
    pass

class UnknownError(Error):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    

class UserNotFoundException(Error):
    pass

class UserExistsException(Error):
    pass