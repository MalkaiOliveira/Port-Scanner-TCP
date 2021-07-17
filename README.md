# Port-Scanner-TCP
 Protótipo Port Scanner TCP

[![forthebadge made-with-python](https://forthebadge.com/images/badges/works-on-my-machine.svg)](#)

*Euller Macena*
*Hiaggo Bezerra*
*Malkai Oliveira*
*Ciência da Computação*
*UFF*
*Niteroi, 2020*

Projeto desenvolvido para a disciplina de **Redes de Computadores I**, **UFF**.
### Stack
  * **Python**
  * **Visual Code**

### App
O objetivo do trabalho é desenvolver um Port Scanner simplificado que consiga categorizar as portas de um host alvo nessas três classes: "aberta", "filtrada" e "fechada". O programa desenvolvido deverá receber como argumentos da linha de comando o endereço do host alvo (seja um hostname, seja diretamente o endereço IP) e uma faixa de números de porta a serem analisados. O programa deverá, então, varrer essas portas tentando estabelecer conexões e, com base no resultado dessa tentativa, classificar cada porta da faixa. Ao final da execução, o programa deverá listar todas as portas abertas, todas as portas filtradas e todas as portas fechadas.

Exemplo de entrada: **127.0.0.1 1 10**<br>
Output:
<p align="center">
        
        Portas abertas: 0
    ------------------------------------
    ------------------------------------

        Portas filtradas: 0
    ------------------------------------
    ------------------------------------

        Portas fechadas: 10
    ------------------------------------
    | O status da porta 1 é fechada. |
    | O status da porta 2 é fechada. |
    | O status da porta 3 é fechada. |
    | O status da porta 4 é fechada. |
    | O status da porta 5 é fechada. |
    | O status da porta 6 é fechada. |
    | O status da porta 7 é fechada. |
    | O status da porta 8 é fechada. |
    | O status da porta 9 é fechada. |
    | O status da porta 10 é fechada. |
    ------------------------------------
</p>

Listas são geradas, dividindo as portas em um desses 3 estados: aberta, filtrada ou fechada, mostrando também a quantidade de portas em cada estado. O resultado desse processo é mostrado no próprio terminal.

### Como executar

Para executar, execute o seguinte comando dentro da pasta do projeto:
```sh
$ python scanner.py hostname min max threadNumber
```

Onde hostname é o nome ou endereço IP do host alvo, min e max são os valores da faixa de portas desejadas para serem analisadas, e threadNumber é o número de threads a ser usado no processo.


#### OBS
Usamos threads para acelerar a análise das portas, atribuindo para cada thread uma porta da faixa a ser avaliada.

Créditos
----

[@eullerm](https://github.com/eullerm)
[@Hiaggo](https://github.com/Hiaggo/)
[@MalkaiOliveira](https://github.com/MalkaiOliveira)
