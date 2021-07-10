import sys
import socket

portasAbertas = []
portasFechadas = []
portasFiltradas = []

try:
    servidor = socket.gethostbyname(sys.argv[1]) 
    min = int(sys.argv[2])
    max = int(sys.argv[3])

    print("Escaneando o servidor {} no intervalo [{}, {}].".format(servidor, min, max))

    print()
    # O programa irá escanear portas de min até max+1
    for porta in range(min, max + 1):
        print("Verificando a porta {}".format(porta))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
          
        resultado = s.connect_ex((servidor, porta))
        
        if resultado == 0:
            portasAbertas.append(porta)
        
        elif resultado == 10035:  
            portasFechadas.append(porta)

        elif resultado == 10061 or resultado == 10060:
            portasFiltradas.append(porta)
        
        s.close()

 
    
    print("\n       Portas abertas: {}".format(len(portasAbertas)))
    
    print("-" * 34)
    for porta in portasAbertas:
        print("| O status porta {} é aberta. |".format(porta))
    print("-" * 34)
    
    print("\n       Portas fechadas: {}".format(len(portasFechadas)))
    
    print("-" * 34)
    for porta in portasFechadas:
        print("| O status da porta {} é fechada. |".format(porta))
    print("-" * 34)
    
    print("\n       Portas filtradas: {}".format(len(portasFiltradas)))
    
    print("-" * 34)
    for porta in portasFiltradas:
        print("| O status da porta {} é filtrada. |".format(porta))
    print("-" * 34)

except KeyboardInterrupt:
    print("\n Programa finalizado.")
    exit()
except socket.gaierror:
    print("\n Entrada inválida para o nome do host.")
    exit()