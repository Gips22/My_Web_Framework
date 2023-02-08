class Response:
    def __init__(self, status_code=200, headers=None, body=''):
        self.status_code = status_code
        self.headers = {}
        self.body = b''
        self.set_headers()
        if headers:
            self.update_headers(headers)
        self.set_body(body)


    def set_headers(self):
        self.headers = {
            ('Content-Type', 'text/plain; charset=utf-8'),
            ('Content-Length', 0),
        }

    def set_body(self, body):
        self.body = body.encode('utf-8')  # строки не читаются, нужно передавать байты с кодировкой
        self.update_headers(
            {'Content-Length': str(len(self.body))}
        )

    def update_headers(self, headers: dict):
        self.headers.update(headers)  # когда будут пересекаться заголовки-не будет ошибки, а просто произойдет замена