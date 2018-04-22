FROM python:3-alpine
WORKDIR /service
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 8888
CMD [ "python3", "-m", "hello_world_python_grpc.service.main" ]
