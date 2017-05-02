import helloworld_pb2_grpc
import helloworld_pb2
import grpc
from concurrent import futures
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class HelloWorldServer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("request:", request)
        print("context:", dir(context))
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
  print("starting")
  # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  # helloworld_pb2_grpc.add_GreeterServicer_to_server(HelloWorldServer(), server)

  server = helloworld_pb2.beta_create_Greeter_server(HelloWorldServer())
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt as e:
    server.stop(0)

if __name__ == '__main__':
  print('here')
  serve()
