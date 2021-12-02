# Caesar Cypher

You are in war with an enemy and your soldiers are on the battlefield. You want to send them a message, but you
realize your message could be intercepted because the person who delivers it is not trustable.

Well, so why not encrypt the message? The Caesar Cypher is a classical cryptography method, it is symmetric and damn
simple! Here are the rules:

You have a message you want to encrypt, let's suppose it is 'potato'.
To encrypt this message, both you and the person who will get this message must know a password in common, this password
is a number.

Then to decrypt the message, they will need to sum all the characters with the password they know.
As example, if the password is number 4, the result would be:

p + 4 = t
o + 4 = s
t + 4 = x
a + 4 = e
t + 4 = x
o + 4 = s

So the encrypted message would be 'tsxexs'!

## Requirements
- Python 3+

## Running

To run this program, run the following line inside of a terminal:

`python3 src/script.py`

## Inputs

- O: an integer number meant as the operation. 0 for encrypting and 1 for decrypting.
- W: an string meant as the word which will be encrypted
- P: an integer number meant as the password which will be used to encrypt the message.

### Requirements
- -1 < O < 2
- -1 < C < 27
- W cannot have special characters

## Outputs

- R: an string meant as the word encrypted or decrypted.

## Example

### Input
0
potato
4

### Output
utxext

## Credits

This program was developed by students from TINFEM 2018:
Adriano Pereira Junior, Giovanna Duarte Evaristo, Guilherme Farrel Garcia Calixto Tobias de Souza, Matheus Dolci and Mikael Pedro Sonoda Gomes.