ANO_ANUAL = 2025

print("Olá! Bem-vindo(a) ào App  pra descobrir seu sexo? .")

nome = input("Por favor, digite seu nome: ")
peso = input("Por favor, digite seu peso (em kg): ")
altura = input("Por favor, digite sua altura (em metros): ")
sexo = input("Por favor, digite seu sexo: ")
time = input("Por favor, digite seu time do coração: ")
cor = input("Por favor, digite sua cor favorita: ")
cidade = input("Por favor, digite sua cidade: ")

ano_nascimento_str = input(f"Que legal, {nome}! Em que ano você nasceu? ")

try:
    ano_nascimento = int(ano_nascimento_str)
    idade = ANO_ANUAL - ano_nascimento

    print("\n--- Processando ---\n")
    print(f"Olá, {nome}!")
    print(f"Você nasceu em {ano_nascimento} e tem (ou fará) {idade} anos em {ANO_ANUAL}.")
    print(f"Sexo: {sexo}")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"Time do coração: {time}")
    print(f"Cor favorita: {cor}")
    print(f"Cidade: {cidade}")
    print("\nMuito obrigado voce é Menina!")

except ValueError:
    print(f"\nOops! Parece que '{ano_nascimento_str}' não é um ano válido. "
          "Por favor, rode o programa novamente e digite apenas números.")
