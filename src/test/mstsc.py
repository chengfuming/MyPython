#!/usr/bin/env python

def telnetdo(HOST=None, USER=None, PASS=None, COMMAND=None): #define a function
    import telnetlib, sys
    if not HOST:
        try:
            HOST = sys.argv[1]
            USER = sys.argv[2]
            PASS = sys.argv[3]
            COMMAND = sys.argv[4]
        except:
            print ("Usage: telnetdo.py host user pass command")
            return
    msg = ['Debug messages:\n'] #
    tn = telnetlib.Telnet() #
    try:
        tn.open(HOST)
    except:
        print ("Cannot open host")
        return
    #tn.write(b'y\n')
    #msg.append(tn.expect(['login:'], 5)) #
    tn.read_until(b"login:")
    tn.write(USER.encode('ascii') + b'\n')
    if PASS:
        #msg.append(tn.expect(['Password:'], 5))
        tn.read_until(b"Password:")
        tn.write(PASS.encode('ascii') + b'\n')
    #msg.append(tn.expect([USER], 5))
    tn.write(COMMAND.encode('ascii') + b'\n')
    tn.write(b"exit\n")
    #msg.append(tn.expect(['#'], 5))
    tmp = tn.read_all()
    tn.close()
    del tn
    return tmp
    
if __name__ == '__main__':
    print (telnetdo('192.168.1.103','gg','gg','java -version'))