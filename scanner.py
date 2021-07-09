import sys
import socket

servidor = socket.gethostbyname(sys.argv[1]) 
min = int(sys.argv[2])
max = int(sys.argv[3])

print("+" * 50)
print("Escaneando Servidor: " + servidor)
print("+" * 50)

try:
      
    # O programa irá escanear portas de min até max+1
    for porta in range(min,max+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
          
        resultado = s.connect_ex((servidor,porta))
        if resultado == 0:
            print("Porta {} está aberta".format(porta))
        elif resultado == 10061:  
            print('Porta {} está filtrada, connect_ex retornou: '.format(porta)+str(resultado)) 
        elif resultado == 10035:  
            print('Porta {} está fechada, connect_ex retornou: '.format(porta)+str(resultado)) 
        else: print('Erro desconhecido'+str(resultado)) 
        s.close()
          
except KeyboardInterrupt:
    print("\n Saindo do programa")
    exit()
except socket.gaierror:
    print("\n Hostname não pode ser resolvido")
    exit()
except socket.error:
    print("\n Servidor não está respondendo")
    exit()