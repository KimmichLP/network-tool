import socket           #Hente socket biblotek

HOST = "127.0.0.1"
PORT = 69696 


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    #Setter AF._INET for IPv4 og SOCK_STREAM for TCP 
    pass


def port_skanning():    #Funksjon for port skanning
    print("Nice 1")

def ping_test():        #Funksjon for å pinge en server/port
    print("Nice 2")

def dos_monitor():      #Funksjon for DoS monitorering
    print("Nice 3")

def main():  

    while True:         #Kjører en loop frem til bruker velger gyldig verdi
            VALG = input("\nHei, hva ønsker du å gjøre i dag?\nVelg en av disse tre alternativene:\n\n1. Port skanning?\n2. Kjøre ping-testing?\n3. DoS Monitor?\nTast inn valg her: ") #Henter inn verdi fra bruker

            if VALG == "1":
                port_skanning()
                break            
            elif VALG == "2":
                ping_test()
                break
            elif VALG == "3":
                dos_monitor()
                break
            else:
                print("Ugyldig verdi")


if __name__ == "__main__":
    main()
