

class Handler(object):
    def execute(self, command):
        print('ERROR SHOULD NOT BE CALLED')
    def set_irc_connection(self, irc_connection):
        self.irc_connection = irc_connection

