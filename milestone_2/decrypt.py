Enter_key = int(input('Enter key: '))
Enter_message = input('Enter message: ')

decrypt_massage = []
for i in Enter_message:
    if i.isalpha():
        if i.isupper():
            decrypt_massage.append(chr((ord(i) - ord('A') - Enter_key) % 26 + ord('A')))
        else: 
            i.islower()
            decrypt_massage.append(chr((ord(i) - ord('a') - Enter_key) % 26 + ord('a')))
    else: 
        decrypt_massage.append(i)
decrypt_massage = ''.join(decrypt_massage)    

print (decrypt_massage) 