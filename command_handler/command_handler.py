import commands.sysinfo as si

def h(input):
    if input == 'info':
        si.System_information()
        returnvar = si.System_information()
    else:
        returnvar = 'Command not found'
    return returnvar