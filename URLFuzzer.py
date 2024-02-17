import requests
import argparse

print('''\033[1;35m                _                         __               
               | |                       / _|              
   ___ __ _  __| | ___ _ __  _   _ ___  | |_ _   _ ________
  / __/ _` |/ _` |/ _ \ '_ \| | | / __| |  _| | | |_  /_  /
 | (_| (_| | (_| |  __/ | | | |_| \__ \ | | | |_| |/ / / / 
  \___\__,_|\__,_|\___|_| |_|\__,_|___/ |_|  \__,_/___/___|
\033[0m''')

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", help="Base URL to fuzz", required = True)
    parser.add_argument("-wl", help="Path to wordlist you would like to use", required = True)
    args = parser.parse_args()

    if "https" not in args.url or "http" not in args.url:
        print("Please include full URL, including https:// or http://")
        exit()

    try:
        with open(args.wl, 'r') as wordlist:
            wordlists = wordlist.readlines()
            print("\033[1;35mStarting Fuzz\033[0m")
            for words in wordlists:
                word = str(words).split('\n')[0]
                requestOutput = requests.get(f'{args.url}/{word}')
                if str(requestOutput) == '<Response [200]>':
                    print(f'/{word} exists')
                else:
                    pass
        print('Fuzzing Complete')
    except requests.exceptions.ConnectionError:
        print('URL is not valid')
    except FileNotFoundError:
        print('Wordlist not found')
except KeyboardInterrupt:
    print('\033[1;31mclosing fuzzer\033[0m')
