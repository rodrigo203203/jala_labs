try:
    user_input = input("ingresar edad: ")
    user_age = int(user_input)
except:
    print("Tienes que ingresar un numero para continuar")

decada = user_age // 10
years = user_age % 10

display_text= f"age: {user_age}, decades: {decada}, years: {years}"
print(display_text)