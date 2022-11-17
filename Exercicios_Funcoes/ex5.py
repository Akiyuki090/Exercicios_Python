'''
Fibonacci
'''

def fibonacci():
    x = int(input('Quantas casas deseja ver: '))
    
    a, b = 0, 1

    for i in range(1, x + 1):
        a, b = b, a + b
        print(a)

fibonacci()
