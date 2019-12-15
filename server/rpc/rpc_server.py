# -*- coding: utf-8 -*-
import grpc
import time
from concurrent import futures
import dashboard_pb2
import dashboard_pb2_grpc
from server import server

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8080'


class FormatData(dashboard_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        str = server.getServerInfo()
        return dashboard_pb2.Data(text=str.upper())


def serve():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    dashboard_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpc_server)
    grpc_server.add_insecure_port(_HOST + ':' + _PORT)
    grpc_server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpc_server.stop(0)

