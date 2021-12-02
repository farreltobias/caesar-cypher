# Cifra de César

Você está em guerra com um inimigo e seus soldados estão no campo de batalha. Você quer enviar uma mensagem a eles, mas
você percebe que sua mensagem poderia ser interceptada, já que a pessoa que faz a entrega dela não é confiável.

Bem, então por que não criptografar a mensagem? A Cifra de César um método clássico de criptografia, é simétrico e simples
para caramba! Aqui vão as regras:

Você tem uma mensagem para criptografar, então vamos supor que é 'batata'.
Para criptografar essa mensagem, tanto você quanto a pessoa que vai recebê-la, precisam conhecer uma senha, e essa senha
é um número.

Então para descriptografar a mensagem, essa pessoa precisará somar todos os caracteres dela com a senha que você sabe.
Como exemplo, se a senha fosse o número 4, o resultado seria:

b + 4 = f
a + 4 = e
t + 4 = x
a + 4 = e
t + 4 = x
a + 4 = e

Então a mensagem criptograda seria 'fexexe'!

## Requisitos
- Python 3+

## Rodando

Para rodar esse programa, execute a seguinte linha em um terminal:

`python3 src/script.py`

## Entrada

- O: um número inteiro (integer) para indicar a operação. 0 para criptografar e 1 para descriptografar.
- W: um texto (string) para indicar a palavra a ser criptografada
- P: um número inteiro (integer) para indicar a senha que vai ser usada para criptografar a mensagem.

### Requisitos
- -1 < O < 2
- -1 < C < 27
- W não pode ter caracteres especiais

## Saída

- R: um texto (string) para indicar a palavra criptografada ou descriptografada.

## Exemplo

### Entrada
0
batata
4

### Saída
fexexe

## Créditos

Este programa foi desenvolvido por discentes do TINFEM 2018:
Adriano Pereira Junior, Giovanna Duarte Evaristo, Guilherme Farrel Garcia Calixto Tobias de Souza, Matheus Dolci e Mikael Pedro Sonoda Gomes.