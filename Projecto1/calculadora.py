user_input = input('Please enter your age:')
age = int(user_input)
resultado = age // 10
if resultado > 1:
    print ('Usted tiene ', resultado ,'decadas')
else:
   print ('Usted tiene una ', resultado ,'decada') 