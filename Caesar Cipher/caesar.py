

a = str(print(input('Enter the string to be Ciphered ::::')))
encrypted = []

for i in range(0, len(a)) :
    a[i] = a[i + 3] % 26
    
        

