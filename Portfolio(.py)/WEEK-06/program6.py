'''Write a program that decrypts messages encoded as above.'''

def decrypt_message(encrypted_message, interval):
    original_message = []
    
    for i in range(len(encrypted_message)):
        if i % interval == 0:
            original_message.append(encrypted_message[i])
    
   
    decrypted_message = ''.join(original_message)
    return decrypted_message

encrypted_message = "sxyexynxydxycxyhxyexyexysxye"  
interval = 2  

decrypted = decrypt_message(encrypted_message, interval)
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted}")