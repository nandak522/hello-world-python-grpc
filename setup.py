#!/usr/bin/env python

from distutils.core import setup

setup(
    name='hello_world_python_grpc',
    version='0.1.0',
    description='hello_world_python_grpc',
    author='Nanda Kishore B',
    author_email='madhav.bnk@gmail.com',
    package_dir={'': 'src'},
    packages=['hello_world_python_grpc'],
    install_requires=[
        'grpcio == 1.11.0',
        'grpcio-tools == 1.11.0',
        'protobuf == 3.5.2.post1',
        'six == 1.11.0',
    ])
