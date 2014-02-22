import re

def parse_raw_string(msg):
    # first search for a generic irc string, could be a PART of a PRIVMSG
    m1 = re.search('^:(\w+)!(\w+).(\S+)\s(\S+)\s(\S+)', msg)
    command = []        # null out our return list
    rawmsg = ''         # 
    cmd = ''            # 
    arg = ''            #
    m2 = []
    m3 = []
    # if there is a generic irc command
    if m1:
        # check if it is a full PRIVMSG
        m = re.search('^:(\w+)!(\w+).(\S+)\s(\S+)\s(\S+)\s:(.+)', msg)
        if m:
            # if it is set the rawmsg and check to see if its a pugbot command
            rawmsg = m.group(6)
            m2 = re.search('^[@!\.](\S+)', rawmsg)
            m3 = re.search('^[@!\.](\S+)\s(\S+)', rawmsg)
        if m2:
            #if there was a pugbot command store it
            cmd = m2.group(1)
            if m3:
                #if there was an argument to this command store it
                arg = m3.group(2)
        command = {'name': m1.group(1), 'uname': m1.group(2), 'hostmask': m1.group(3), 'irccmd': m1.group(4), 'channel': m1.group(5), 'rawmsg': rawmsg, 'cmd': cmd, 'arg': arg}
    return command

