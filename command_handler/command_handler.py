import commands.sysinfo as si
import sys
def h(input):
    if input == 'stop':
        sys.exit(0)
    elif input == 'info':
        si.System_information()
        returnvar = si.System_information()
    else:
        returnvar = 'Command not found'
    return returnvar