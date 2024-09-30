import random
import os

def validar(letra):
  if letra in letras_tentadas:
    return 0
  if letra.isalpha():
    return 1
  else:
    return 0


palavras = [
    "cachorro",
    "gato",
    "passaro",
    "elefante",
    "leao",
    "tigre",
    "zebra",
    "girafa",
    "hipopotamo",
    "crocodilo",
    "cobra",
    "lagarto",
    "sapo",
    "ra",
    "peixe",
    "tubarao",
    "baleia",
    "polvo",
    "caranguejo",
    "lagosta",
    "camarao",
    "lula",
    "arvore",
    "flor",
    "folha",
    "grama",
    "cacto",
    "bambu",
    "pinheiro",
    "carvalho",
    "pergaminho",
    "papel",
    "caneta",
    "lapis",
    "borracha",
    "caderno",
    "livro",
    "biblioteca",
    "escola",
    "universidade",
    "professor",
    "aluno",
    "ciencia",
    "matematica",
    "historia",
    "geografia",
    "arte",
    "musica",
    "danca"
]
homem_enforcado = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]
sorteada=random.choice(palavras)
sorteada1=[]
for i in sorteada:
  sorteada1.append(i)
ganhou=False
tentativas=1
certo=1
letras=[]
letras_tentadas=[]
underline=""
validada=0

print(sorteada)

for letra in sorteada:
  letras.append(' ')
  underline+="- "
  
while ganhou==False and tentativas<8 :
  _ = os.system('cls')
  print("Tentativa número: ",tentativas)
  print("Letras já usadas:",letras_tentadas)
  print(homem_enforcado[tentativas-1])
  for i in letras:
    print(i,end=" ")
  print(end="\n")
  print(underline)

  tentada=input("DIGITE UMA LETRA: ")
  validada=validar(tentada)
  while validada==0:
    tentada=input("DIGITE UMA LETRA: ")
    validada=validar(tentada)
  certo=0
  letras_tentadas.append(tentada)
  k=0
  for i in sorteada1:
    if i==tentada:
      certo=1
      letras[k]=tentada
    k+=1


  if letras==sorteada1:
    ganhou=True
    
  if certo==0:
    tentativas+=1
  
if ganhou==True:
  _ = os.system('clear')
  print("Tentativa número: ",tentativas)
  print("Letras já usadas:",letras_tentadas)
  print(homem_enforcado[tentativas-1])
  for i in letras:
    print(i,end=" ")
  print("",end="\n")
  print(underline)
  print("Você ganhou, a palavra era:",sorteada)
else:
  print("Você perdeu, a palavra era:",sorteada)