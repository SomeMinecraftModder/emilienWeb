class Request:

    def __init__(self, raw_data, headers, method, url, data):
        self._raw_data: bytes = raw_data
        self.headers: dict = headers
        self.method: str = method
        self.data: str = data
        self.url: str = url
