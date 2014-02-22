import ircconn
import raw_string_parser as sp
import handler

# class to control the irc connection and send messages to various
# handlers which act on the received commands
class IrcBot:
    def __init__(self, irc_connection):
        # all variables are references in python
        # so we hook an irc connection to the IrcBot
        self.irc_connection = irc_connection
        self.handlers = []

    # adds a handler to receive commands
    def add_handler(self,handler):
        handler.set_irc_connection(self.irc_connection)
        self.handlers.append(handler)

    # main loop, listens for new messages then has the handlers
    # act on the received info
    def listen(self):
        while 1:
            msg_list = self.irc_connection.recv()
            for msg in msg_list:
                command = sp.parse_raw_string(msg)
                for h in self.handlers:
                    h.execute(command)
