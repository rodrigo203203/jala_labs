user_input = input('Ingrese la temperatura: ')
temp = int(user_input)
if temp > 80:
    print('Its too hot!','stay in home!')
elif temp < 60:
    print('Its too cold!','stay in home!')
else:
    print('enjoy the outdoor')

# Demo Logical Operator
temps = 95
if temps > 80 or temps < 60:
    print('stay inside the home!')
else:
    print('enjoy the outdoor')