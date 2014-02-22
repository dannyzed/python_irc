import irc_bot
import ircconn
import pug_handler

def run():
    globalgamers = ircconn.IrcConnection()
    globalgamers.init_socket()
    globalgamers.connect('irc.globalgamers.net')
    
    pughandler = pug_handler.PugHandler()
    testbot = irc_bot.IrcBot(globalgamers)
    testbot.add_handler(pughandler)
    testbot.listen()


