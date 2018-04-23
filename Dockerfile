FROM python:3.6-slim-stretch
WORKDIR /apps
COPY ./ .
RUN pip install -r requirements.txt
EXPOSE 8888
CMD [ "python3", "/apps/src/hello_world_python_grpc/server/main.py" ]
