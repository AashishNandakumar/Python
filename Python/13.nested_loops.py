

rows = int(input('enter no of rows: '))
columns = int(input('enter no of columns: '))
symbol = input('enter a symbol to use: ')

for i in range(rows):
    for j in range(columns):
        print(" "+symbol, end="")  # prevents the cursor from moving to next line
    print()                        # To generate new line

print('DONE')



