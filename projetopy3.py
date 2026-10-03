import random
 
numero = random.randint(1, 100)
tentativas = 0
 
while True:
    palpite = int(input("Seu palpite (1-100): "))
    tentativas += 1
    if palpite < numero:
        print("Maior!")
    elif palpite > numero:
        print("Menor!")
    else:
        print(f"Acertou em {tentativas} tentativas!")
        break
 
