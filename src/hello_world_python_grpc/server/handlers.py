from hello_world_pb2_grpc import HelloWorldGreeterServicer
from hello_world_pb2 import HelloWorldResponse
import time
import socket

START = time.time()


def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


class Greeter(HelloWorldGreeterServicer):
    def SayHello(self, request, context):
        response = HelloWorldResponse(
            text=
            "[HOST:%s] Hello World (Python gRPC)! (up %s)\n Request.greeting:%s"
            % (socket.gethostname(), elapsed(),
               getattr(request, 'greeting', '')))
        return response
