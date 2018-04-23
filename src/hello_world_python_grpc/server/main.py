import grpc
import time
from concurrent import futures
import hello_world_pb2_grpc
from handlers import Greeter

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    hello_world_pb2_grpc.add_HelloWorldGreeterServicer_to_server(
        Greeter(), server)
    server.add_insecure_port("[::]:8888")
    print("Greeter Server is up and running...")
    server.start()
    try:
        while 1:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()