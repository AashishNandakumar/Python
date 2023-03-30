import time
# for loops  --> iterates only for a limited time, unlike while loop

# for i in range(10):
#     print(i+1)

# for i in range(50, 100+1):
#     print(i)

# for i in range(50, 100+1, 2):
#     print(i)

# for i in 'Aashish nk':
#     print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(2)   # Put the thread to sleep

print('happy new year')
