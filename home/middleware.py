class HomeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        print('---------------------------------------------')
        pass

    def get_response(self, request, response):
        print('---------------------------------------------')
        self.get_response(request)
        return response

    def __call__(self, request):
        print('before---------------response')
        response = self.get_response(request)
        # response = self.process_request(request)
        print('after---------------response')
        return response
