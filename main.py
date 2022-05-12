#!/usr/bin/python3

import base64 as b64
from colorama import init, Fore, Style
import subprocess as sub
import sys

"""
russian-dev:
    Simple base encoder/decoder. Nothing special.
    
    Also, this code is pretty messy...
"""

asciiArt = f"""{Style.BRIGHT}{Fore.BLUE}
d8888b.         .o88b.  .d88b.  d8888b. d88888b d8888b. 
88  `8D        d8P  Y8 .8P  Y8. 88  `8D 88'     88  `8D 
88oooY'        8P      88    88 88   88 88ooooo 88oobY' 
88~~~b. C8888D 8b      88    88 88   88 88~~~~~ 88`8b   
88   8D        Y8b  d8 `8b  d8' 88  .8D 88.     88 `88. 
Y8888P'         `Y88P'  `Y88P'  Y8888D' Y88888P 88   YD {Style.RESET_ALL}
"""

def decode():
    sub.call('clear')
    print(f"""{Style.BRIGHT}{Fore.BLUE}
d8888b.         .o88b.  .d88b.  d8888b. d88888b d8888b. 
88  `8D        d8P  Y8 .8P  Y8. 88  `8D 88'     88  `8D 
88oooY'        8P      88    88 88   88 88ooooo 88oobY' 
88~~~b. C8888D 8b      88    88 88   88 88~~~~~ 88`8b   
88   8D        Y8b  d8 `8b  d8' 88  .8D 88.     88 `88. 
Y8888P'         `Y88P'  `Y88P'  Y8888D' Y88888P 88   YD 
{Style.RESET_ALL}
                      -PICK ONE-
                        Base16
                        Base32
                        Base64
                        Base85
""")
    
    selection = input(f"{Style.DIM}> {Style.RESET_ALL}").lower()
    
    if selection == 'base16':
        sub.call('clear')
        print(asciiArt)
        string = input(f"{Style.DIM}Decode (B16): {Style.RESET_ALL}")
        cstring = b64.b16decode(string.encode('ascii'))

        sub.call('clear')
        print(asciiArt)
        print(f"{Style.BRIGHT}\"{string}\" decoded in Base16:{Style.RESET_ALL}\n{cstring.decode('utf8')}")
        input("\nPress any key to exit...")
        sys.exit()
    elif selection == 'base32':
        sub.call('clear')
        print(asciiArt)
        string = input(f"{Style.DIM}Decode (B32): {Style.RESET_ALL}")
        cstring = b64.b32decode(string.encode('ascii'))

        sub.call('clear')
        print(asciiArt)
        print(f"{Style.BRIGHT}\"{string}\" decoded in Base32:{Style.RESET_ALL}\n{cstring.decode('utf8')}")
        input("\nPress any key to exit...")
        sys.exit()
    elif selection == 'base64':
        sub.call('clear')
        print(asciiArt)
        string = input(f"{Style.DIM}Decode (B64): {Style.RESET_ALL}")
        cstring = b64.b64decode(string.encode('ascii'))

        sub.call('clear')
        print(asciiArt)
        print(f"{Style.BRIGHT}\"{string}\" decoded in Base64:{Style.RESET_ALL}\n{cstring.decode('utf8')}")
        input("\nPress any key to exit...")
        sys.exit()
    elif selection == 'base85':
        pass
    elif selection == 'ascii85':
        pass
    else:
        sub.call('clear')
        print(asciiArt)
        print(f"{Style.DIM}Duh oh!.. I do not recognize that input!..")
        input("Press any key to restart...")
        decode()

    # for base85/ascii85
    sub.call('clear')
    print(asciiArt)
    string = input(f"{Style.DIM}Decode (A85): {Style.RESET_ALL}")
    cstring = b64.a85decode(string.encode('ascii'))

    sub.call('clear')
    print(asciiArt)
    print(f"{Style.BRIGHT}\"{string}\" decoded in Ascii85 (Base85):{Style.RESET_ALL}\n{cstring.decode('utf8')}")
    input("\nPress any key to exit...")
    sys.exit()

def encode():
    sub.call('clear')
    print(f"""{Style.BRIGHT}{Fore.BLUE}
d8888b.         .o88b.  .d88b.  d8888b. d88888b d8888b. 
88  `8D        d8P  Y8 .8P  Y8. 88  `8D 88'     88  `8D 
88oooY'        8P      88    88 88   88 88ooooo 88oobY' 
88~~~b. C8888D 8b      88    88 88   88 88~~~~~ 88`8b   
88   8D        Y8b  d8 `8b  d8' 88  .8D 88.     88 `88. 
Y8888P'         `Y88P'  `Y88P'  Y8888D' Y88888P 88   YD 
{Style.RESET_ALL}
                      -PICK ONE-
                        Base16
                        Base32
                        Base64
                        Base85
""")
    
    selection = input(f"{Style.DIM}> {Style.RESET_ALL}").lower()
    
    if selection == 'base16':
        sub.call('clear')
        print(asciiArt)
        string = input(f"{Style.DIM}Encode (B16): {Style.RESET_ALL}")
        cstring = b64.b16encode(string.encode('ascii'))

        sub.call('clear')
        print(asciiArt)
        print(f"{Style.BRIGHT}\"{string}\" encoded in Base16:{Style.RESET_ALL}\n{cstring.decode('utf8')}")
        input("\nPress any key to exit...")
        sys.exit()
    elif selection == 'base32':
        sub.call('clear')
        print(asciiArt)
        string = input(f"{Style.DIM}Encode (B32): {Style.RESET_ALL}")
        cstring = b64.b32encode(string.encode('ascii'))

        sub.call('clear')
        print(asciiArt)
        print(f"{Style.BRIGHT}\"{string}\" encoded in Base32:{Style.RESET_ALL}\n{cstring.decode('utf8')}")
        input("\nPress any key to exit...")
        sys.exit()
    elif selection == 'base64':
        sub.call('clear')
        print(asciiArt)
        string = input(f"{Style.DIM}Encode (B64): {Style.RESET_ALL}")
        cstring = b64.b64encode(string.encode('ascii'))

        sub.call('clear')
        print(asciiArt)
        print(f"{Style.BRIGHT}\"{string}\" encoded in Base64:{Style.RESET_ALL}\n{cstring.decode('utf-8')}")
        input("\nPress any key to exit...")
        sys.exit()
    elif selection == 'base85':
        pass
    elif selection == 'ascii85':
        pass
    else:
        sub.call('clear')
        print(asciiArt)
        print(f"{Style.DIM}Duh oh!.. I do not recognize that input!..")
        input("Press any key to restart...")
        encode()

    # for base85/ascii85
    sub.call('clear')
    print(asciiArt)
    string = input(f"{Style.DIM}Encode (A85): {Style.RESET_ALL}")
    cstring = b64.a85encode(string.encode('ascii'))

    sub.call('clear')
    print(asciiArt)
    print(f"{Style.BRIGHT}\"{string}\" encoded in Ascii85 (Base85):{Style.RESET_ALL}\n{cstring.decode('utf8')}")
    input("\nPress any key to exit...")
    sys.exit()

def main():
    sub.call('clear')
    print(f"""{Style.BRIGHT}{Fore.BLUE}
d8888b.         .o88b.  .d88b.  d8888b. d88888b d8888b. 
88  `8D        d8P  Y8 .8P  Y8. 88  `8D 88'     88  `8D 
88oooY'        8P      88    88 88   88 88ooooo 88oobY' 
88~~~b. C8888D 8b      88    88 88   88 88~~~~~ 88`8b   
88   8D        Y8b  d8 `8b  d8' 88  .8D 88.     88 `88. 
Y8888P'         `Y88P'  `Y88P'  Y8888D' Y88888P 88   YD 
                           {Style.RESET_ALL}                       
                      -PICK ONE-
                        Encode
                        Decode
""")
    selection = input(f"{Style.DIM}> {Style.RESET_ALL}").lower()

    if selection == "encode":
        encode()
    elif selection == "decode":
        decode()

"""
string = input("Encode (B64): ")

string = b64.b64encode(string.encode('ascii'))

print(string)

string = b64.b64decode(string)

print(string.decode('utf8'))
"""

if __name__ == "__main__":
    init(autoreset=True)
    main()
