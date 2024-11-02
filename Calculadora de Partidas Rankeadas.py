
## inicio 
Nome_do_jogador = input("Informe seu nome de usuário: ")
print(f"Bem-vindo(a), {Nome_do_jogador}!")

## entrada
while True:
    try:
        Vitorias = int(input("\nDigite suas vitórias atuais: "))
        Derrotas = int(input("\nDigite suas derrotas atuais: "))
        saida = int(input("Digite 0 para continuar: "))
        if saida == 0:
            print("Continuando...")
            break
    except ValueError:
        print("Por favor, insira um número válido.")

# Soma de vitórias e derrotas
soma = Vitorias - Derrotas
print(f"\n=== Sua soma de vitórias e derrotas é: {soma} ===")

# Determinação do rank

if Vitorias <=10:
    print("Seu rank atual é Ferro")
elif Vitorias >=21:
    print("Seu rank atual é Bronze")
elif Vitorias >= 51:
    print("Seu rank atual é Prata")
elif Vitorias >= 81:
    print("Seu rank atual é Ouro")
elif Vitorias >= 91:
    print("Seu rank atual é Diamante")
elif Vitorias >= 101:
    print("Seu rank atual é Lendário")
else: 
    print("")