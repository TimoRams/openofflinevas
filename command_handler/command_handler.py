import commands.sysinfo as si
import commands.utility as util

import sys


def h(input):
    if input == 'stop':
        sys.exit(0)
    elif input == 'info':
        si.System_information()
        returnvar = si.System_information()
    elif input == 'time':
        util.time()
        returnvar = util.time()
    else:
        returnvar = 'Command not found'
    return returnvar
