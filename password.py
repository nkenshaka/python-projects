username = input("Digite seu username: ")
password = input("Digite sua senha: ")
passwordlenght = 0
criptografia = []

passwordlenght = len(password)

criptografia = passwordlenght * '*'

print(f"{username}'s password {criptografia} is {passwordlenght} characters long")
