from typing import Any

from common.Response_codes import Response_codes

class Response:
    def __init__(self, status: Response_codes, content:Any = None, error:Any = None):
        self.status = status
        self.content = content
        self.error = error

    @property
    def value(self):
        response_data = {'status': self.status.message()}

        if self.content:
            response_data['content'] = self.content

        if self.error:
            response_data['error'] = self.error

        return response_data

    def __bool__(self):
        return False



