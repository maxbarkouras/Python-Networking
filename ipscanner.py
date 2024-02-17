try:
    import socket
    print('''\033[1;35m                _                                                            
               | |                                                           
   ___ __ _  __| | ___ _ __  _   _ ___   ___  ___ __ _ _ __  _ __   ___ _ __ 
  / __/ _` |/ _` |/ _ \ '_ \| | | / __| / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
 | (_| (_| | (_| |  __/ | | | |_| \__ \ \__ \ (_| (_| | | | | | | |  __/ |   
  \___\__,_|\__,_|\___|_| |_|\__,_|___/ |___/\___\__,_|_| |_|_| |_|\___|_|                                                                                                                                                    
\033[0m''')
    y = int(input('what port would you like to scan? '))
    with open('ips.txt', 'r') as files:
        for file in files:
            new = file.split('\n')[0]
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.03)
                raw = s.connect_ex((new,y))
                if raw == 0:
                    print(f'\033[1;35m{new} is open on y\033[0m')
                    pass
                else:
                    pass
        print('\033[1;34mscan is complete\033[0m')
except KeyboardInterrupt:
    print('\033[1;31mclosing scanner\033[0m')