from domHttpx.colors import Color

def tab():
    print('\n')

def info(text):
    print('[' + Color.CBLUE2 + 'INFO' + Color.ENDC + '] ' + text) 

def success(text):
    print('\n[' + Color.CGREEN2 + 'SUCCESS' + Color.ENDC + '] ' + text)

def error(text):
    print('[' + Color.CRED2 + 'ERROR' + Color.ENDC + '] ' + text)

def title(title):
    return f"[{Color.CCYAN2}{title}{Color.ENDC}]"

def sc_200(sc):
    return f"[{Color.CGREEN2}{sc}{Color.ENDC}]"

def sc_500(sc):
    return f"[{Color.CYELLOW2}{sc}{Color.ENDC}]"

def sc_other(sc):
    return f"[{Color.CRED2}{sc}{Color.ENDC}]"