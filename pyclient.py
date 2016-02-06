import json

from authpy.auth import AuthenticationService
from authpy.auth.ttypes import TokenNotValidException
from authpy.auth.ttypes import UserAlreadyExistException
from thrift import Thrift
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport


class AuthClient():

    def connect(self):
        try:
            self.transport = TSocket.TSocket('127.0.0.1', 1818)
            self.transport = TTransport.TBufferedTransport(self.transport)
            self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
            self.client = AuthenticationService.Client(self.protocol)
            self.transport.open()
        except Thrift.TException, tx:
            print '%s' % (tx.message)

    def close(self):
        self.transport.close()

    def authenticate(self, access_token):
        try:
            client = self.client.authenticate(access_token)
            return json.loads(client)
        except TokenNotValidException, e:
            print e

    def register_client(self, name, email):
        try:
            client = self.client.register_client(name, email)
            return client
        except UserAlreadyExistException, e:
            print e
