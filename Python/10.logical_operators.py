# Logical operators

temp = int(input("what is temp outside: "))

if not(temp >= 0 and temp <=30):
    print('Cool temp.')
elif not(temp < 0 or temp > 30):
    print('Horrible temp.')



