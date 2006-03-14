from comar.service import *

serviceType = "server"
serviceDesc = "CUPSD"

def start():
    call("System.Service.start", "hplip")
    run("/sbin/start-stop-daemon --start -q --exec /usr/sbin/cupsd")

def stop():
    run("/sbin/start-stop-daemon --stop -q --exec /usr/sbin/cupsd")
