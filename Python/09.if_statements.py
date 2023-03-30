# if = will execute only if it is true

age = int(input('pls enter age: '))

if age == 100:
    print('u are too old to be alive')
elif age >= 18:
    print('u are an adult')
elif age < 0:
    print('u are not born')
else:
    print('u are a kid')
