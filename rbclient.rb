$:.push('authrb')

require 'thrift'
require 'authentication_service'

class AuthClient

  def authenticate(access_token)
    begin
      transport = Thrift::BufferedTransport.new(Thrift::Socket.new('127.0.0.1', 1818))
      protocol = Thrift::BinaryProtocol.new(transport)
      client = Auth::AuthenticationService::Client.new(protocol)
      transport.open()
      access = client.authenticate(access_token)
      transport.close()
      return access
    rescue Thrift::Exception => tx
      print 'Thrift::Exception: ', tx.message, "\n"
    end
  end

  def register_client(name, email)
    begin
      transport = Thrift::BufferedTransport.new(Thrift::Socket.new('127.0.0.1', 1818))
      protocol = Thrift::BinaryProtocol.new(transport)
      client = Auth::AuthenticationService::Client.new(protocol)
      transport.open()
      register = client.register_client(name, email)
      transport.close()
      return register
    rescue Thrift::Exception => tx
      print 'Thrift::Exception: ', tx.message, "\n"
    end
  end
end