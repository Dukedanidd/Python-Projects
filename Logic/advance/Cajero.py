# Programa que simula un cajero automático

def withdraw_money(amount):
    if amount > 0 and amount <= 1000:
        print(f"Retirando ${amount}...")
    else:
        print("Cantidad inválida. Debe ser un número positivo y menor o igual a 1000.")

def deposit(amount):
    if amount > 0:
        print(f'Depositando ${amount}...')
    else:
        print('Cantidad invalida para el deposito')
