'''Another way to hide a message is to include the letters that make it up within
 seemingly random text. The letters of the message might be every fi h character,
 for example. Write and test a function that does such encryption. It should
 randomly generate an interval (between 2 and 20), space the message out
 accordingly, and should fill the gaps with random letters. The function should
 return the encrypted message and the interval used.
 For example, if the message is "send cheese", the random interval is 2, and for
 clarity the random letters are not random:
 send cheese
 s  e  n  d   c  h  e  e  s  e
 sxyexynxydxy cxyhxyexyexysxye'''

import random
import string

def encrypt_message(message):
    
    interval = random.randint(2, 20)
    
    encrypted_message = []
    
    for i in range(len(message)):
        if i % interval == 0:
            encrypted_message.append(message[i])
        else:
           
            random_letter = random.choice(string.ascii_lowercase)
            encrypted_message.append(random_letter)
    
    encrypted_message_str = ''.join(encrypted_message)
    
    return encrypted_message_str, interval

message = "send cheese"
encrypted, interval = encrypt_message(message)
print(f"Original message: {message}")
print(f"Encrypted message: {encrypted}")
print(f"Interval used: {interval}")