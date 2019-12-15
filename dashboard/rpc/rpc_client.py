# -*- coding: utf-8 -*-
import grpc
from rpc import dashboard_pb2_grpc, dashboard_pb2

_HOST = 'localhost'
_PORT = '8080'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = dashboard_pb2_grpc.FormatDataStub(channel=conn)
    response = client.DoFormat(dashboard_pb2.Data(text='hello,world!'))
    print("received: " + response.text)


def cpu():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = dashboard_pb2_grpc.FormatDataStub(channel=conn)
    response = client.DoFormat(dashboard_pb2.Data)
    print(response.text)


if __name__ == '__main__':
    cpu()
