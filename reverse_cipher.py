
#######################################################################################
#Reverse Cipher Program from the book "Cracking Codes with Python" by Al Sweigart

# This program simply reverses the text that was entered as a simply cipher. The 
# text can be deciphered by entering the cipher text instead of the message. 

########################################################################################

# Keep this to input message for encoding
message = input('Enter Message: ')


# Use field below to add cipher text for decoding (comment out unless decoding)
#message = ''

translated =''

i = len(message)  - 1
while i >0:
    translated = translated + message[i]
    print('i is', i , ', message[i] is' , message[i] , ', translated is' , translated)
    i = i - 1
    
print(translated)
