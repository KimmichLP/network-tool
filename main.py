import socket           #Hente socket biblotek

HOST = "127.0.0.1"

def port_skanning():    #Funksjon for port skanning
    start_port = int(input("Startport (0-65535): "))
    ende_port = int(input("Endeport (0-65535): "))
    
    if start_port < 0 or start_port > ende_port or ende_port > 65535:
        print("Ugyldig portområde! Velg port mellom 0-65535")
        return
    
    print(f"Sjekker porter fra {start_port} til {ende_port}...")

    for port in range(start_port, ende_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #Setter AF._INET for IPv4 og SOCK_STREAM for TCP 
            sock.settimeout(1)  #Delay på 1 sekund
            result = sock.connect_ex((HOST, port))                      #Kobler til og returnerer feilkode uten å kræsje

            if result == 0:
                 print(f"[ÅPEN] port {port} på {HOST}")
            else:
                 print(f"[STENGT] port {port} på {HOST}")

            sock.close()
    
    sock.close()

def ping_test():        #Funksjon for å pinge en server/port
    #TO DO:
    # - Gjøre mer research på Socket Lib
    print("Nice 2")
    
def dos_monitor():      #Funksjon for DoS monitorering
    #TO DO:
    # - Gjøre mer research på Socket Lib
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
