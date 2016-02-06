from authpy.auth import AuthenticationService
from authhandler import AuthHandler
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport

handler = AuthHandler()
processor = AuthenticationService.Processor(handler)
host = '0.0.0.0'
port = 1818
transport = TSocket.TServerSocket(
                host=host,
                port=port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print "Authentication service is now serving on port %s..." % (port)
server.serve()
