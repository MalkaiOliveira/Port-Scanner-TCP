import sys
import socket
import threading
from queue import Queue

portasAbertas = []
portasFechadas = []
portasFiltradas = []
resultadoDasPortas = []
filaDePortas = Queue()

def threader(servidor, tid):
    while True:
        porta = filaDePortas.get()
        verificaPorta(servidor, porta, tid)
        filaDePortas.task_done()

def verificaPorta(servidor, porta, tid):
    
    # O programa irá escanear portas de min até max+1
    print("Verificando a porta {} com a thread {}".format(porta, tid))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.setdefaulttimeout(1)
    
    resultado = s.connect_ex((servidor, porta))
    
    print("RESULTADO {}".format(resultado))
    if resultado not in resultadoDasPortas:
        resultadoDasPortas.append(resultado)

    if resultado == 0:
        portasAbertas.append(porta)
    
    elif resultado == 10035:  
        portasFechadas.append(porta)

    elif resultado == 10060 or resultado == 10061:
        portasFiltradas.append(porta)
    
    s.close()


def main():
    try:
        servidor = socket.gethostbyname(sys.argv[1]) 
        min = int(sys.argv[2])
        max = int(sys.argv[3])

        print("Escaneando o servidor {} no intervalo [{}, {}].".format(servidor, min, max))
        
        for x in range(8):
            thread = threading.Thread(target=threader, args=(servidor, x,), daemon=True)
            thread.start()
        
        for porta in range(min, max + 1):
            
            filaDePortas.put(porta)
        
        filaDePortas.join()

        print("\n       Portas abertas: {}".format(len(portasAbertas)))
        
        print("-" * (34 + len(str(max))))
        portasAbertas.sort()
        for porta in portasAbertas:
            print("| O status porta {} é aberta. |".format(porta))
        print("-" * (34 + len(str(max))))
        
        print("\n       Portas fechadas: {}".format(len(portasFechadas)))
        
        print("-" * (34 + len(str(max))))
        portasFechadas.sort()
        for porta in portasFechadas:
            print("| O status da porta {} é fechada. {} |".format(porta))
        print("-" * (34 + len(str(max))))
        
        print("\n       Portas filtradas: {}".format(len(portasFiltradas)))
        
        print("-" * (34 + len(str(max))))
        portasFiltradas.sort()
        for porta in portasFiltradas:
            print("| O status da porta {} é filtrada. |".format(porta))
        print("-" * (34 + len(str(max))))

        print("Erros recebidos: {}".format(resultadoDasPortas))

    except KeyboardInterrupt:
        print("\n Programa finalizado.")
        exit()
    except socket.gaierror:
        print("\n Entrada inválida para o nome do host.")
        exit()

main()