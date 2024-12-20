username = input("Digite seu username: ")
password = input("Digite sua senha: ")
passwordlenght = 0
criptografia = []

for caracteres in password:
    passwordlenght += 1

criptografia = passwordlenght * '*'

print(f"{username}'s password {criptografia} is {passwordlenght} characters long")

