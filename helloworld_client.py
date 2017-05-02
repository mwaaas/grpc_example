import helloworld_pb2
import helloworld_pb2_grpc
import grpc


def run():
  channel = grpc.insecure_channel('localhost:7000')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  print("Greeter client received: " + response.message)


if __name__ == '__main__':
  run()
