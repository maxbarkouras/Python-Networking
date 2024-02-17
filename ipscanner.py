import socket
import argparse

print('''\033[1;35m                _                                                            
               | |                                                           
   ___ __ _  __| | ___ _ __  _   _ ___   ___  ___ __ _ _ __  _ __   ___ _ __ 
  / __/ _` |/ _` |/ _ \ '_ \| | | / __| / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
 | (_| (_| | (_| |  __/ | | | |_| \__ \ \__ \ (_| (_| | | | | | | |  __/ |   
  \___\__,_|\__,_|\___|_| |_|\__,_|___/ |___/\___\__,_|_| |_|_| |_|\___|_|                                                                                                                                                    
\033[0m''')

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", help="IP address or host to scan", required = True)
    args = parser.parse_args()

    #loop for all possible ports
    for i in range(65536):
        #define variable for sending tcp packets
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.03)
        #send a tcp connection to ip and port
        outputCode = s.connect_ex((args.ip,i))
        #check if request was sent successfully, meaning port is open
        if outputCode == 0:
            print(f'\033[1;35m{args.ip} is open on {i}\033[0m')
            pass
        else:
            pass
        
    print('\033[1;34mscan is complete\033[0m')
except KeyboardInterrupt:
    print('\033[1;31mclosing scanner\033[0m')
