class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cstr(msg, color):
	return "{}{}{}".format(color, msg, bcolors.ENDC)

def green(msg):
	return cstr(msg, bcolors.OKGREEN)

def red(msg):
	return cstr(msg, bcolors.FAIL)

def yellow(msg):
	return cstr(msg, bcolors.WARNING)

def blue(msg):
	return cstr(msg, bcolors.OKBLUE)
	