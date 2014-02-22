import socket
import re
import sys

# Main IRC connection class
class IrcConnection:
    # Constructor
    def __init__(self):
        # Set up some defaults
        self.bufsize = 4096
        self.nick = 'dzbot'
        self.user = 'dzbot'

    def init_socket(self):
        # standard socket code
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # want it to be blocking
        self.sock.setblocking(1)

    def connect(self, servername):
        self.servername = servername;
        # start the connection
        self.sock.connect((servername,6667))
        # need to send initial IRC commands
        # first we get sent 4 messages + 1 pong request
        msg_count = 0
        while msg_count < 4:
            msg_count += len(self.recv())
        # send the required fields
        self.send('NICK ' + self.nick)
        # now the pong request will come
        self.recv()
        # send the rest
        self.send('USER dzbot 8 *  : dzbot dzbot')
        self.send('JOIN #ua')

    # sends data to the irc server, '\r\n' is automatically
    # added on the end
    def send(self,msg):
        msg = msg + '\r\n'
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(bytes(msg[totalsent:],"utf-8"))
            if sent == 0:
                raise RuntimeError("socket broken")
            totalsent += sent
        sys.stdout.write("<<  " + msg)
        
    # checks for ping/pong events and handles them using regular
    # expressions
    def ping_pong_check(self, msg):
        reply = re.search('^PING :(\w+)', msg)
        if reply:
            reply = 'PONG :' + reply.group(1)
            self.send(reply)
            return 1
        return 0

    def recv(self):
        self.recv_buffer = self.sock.recv(self.bufsize)
        self.recv_buffer = self.recv_buffer.decode("utf-8")
        return_lines = []
        while self.recv_buffer:
            pos = self.recv_buffer.find('\n') + 2
            if pos > 0:
                msg = self.recv_buffer[:pos]
                self.recv_buffer = self.recv_buffer[pos:]
                # suppress the ping pong messages
                if self.ping_pong_check(msg) == 0:
                    sys.stdout.write(">>  " + msg)
                    return_lines.append(msg)
        return return_lines
    
    def send_privmsg(self, msg, channel):
        msg = 'PRIVMSG ' + channel + ' :' + msg
        self.send(msg)
