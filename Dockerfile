#FROM mwaaas/grpc_compiler
FROM python:2.7
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 50051

CMD python helloworld_server.py