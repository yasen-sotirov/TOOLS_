from fastapi import Response


class BadRequest(Response):
    def __init__(self, content=''):
        super().__init__(status_code=400, content = content)


class NotFound(Response):
    def __init__(self, content=''):
        super().__init__(status_code=404, content=content)


class OK(Response):
    def __init__(self, content=''):
        super().__init__(status_code=200, content=content)


class NoContent(Response):
    def __init__(self):
        super().__init__(status_code=204)