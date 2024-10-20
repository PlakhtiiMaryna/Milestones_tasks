Enter_key = int(input('Enter key: '))
Enter_message = input('Enter message: ')

encrypt_massage = []
for i in Enter_message:
    if i.isalpha():
        if i.isupper():
            encrypt_massage.append(chr((ord(i) - ord('A') + Enter_key) % 26 + ord('A')))
        else: 
            i.islower()
            encrypt_massage.append(chr((ord(i) - ord('a') + Enter_key) % 26 + ord('a')))
    else: 
        encrypt_massage.append(i)
encrypt_massage = ' '.join(encrypt_massage)    

print (encrypt_massage) 