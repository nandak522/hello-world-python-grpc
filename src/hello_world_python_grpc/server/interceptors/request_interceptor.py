import grpc


class RequestInterceptor(grpc.ServerInterceptor):
    def __init__(self, greeting):
        self.greeting = "Tampered " + str(greeting)

    def intercept_service(self, continuation, handler_call_details):
        # Before response computation
        response = continuation(handler_call_details)
        return response
