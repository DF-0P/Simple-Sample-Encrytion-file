text = "hG19l8fkjdklvoir434" #input("what is the text to encrypt:\n>")

text_2 = text[0:2] #get the first two character of the text
rest = text[2:] #get the rest of the characters of the text

encryption =[] #new list to store  the arrangement of  the first two characters and arrangement of the other digits  
if text_2[0].islower() and text_2[1].isupper(): #conditions tocheck the first two characters
    encryption.append(text_2[1])
    encryption.append(text_2[0])
    encryption.append("*") #salt added to the arrangement
else: #else statement 
    encryption.append(text_2[0])
    encryption.append(text_2[1])
#print(encryption) #to print the initial encryption wihtout the nnumbers first

rest_c =[] #list to hold the rest of the characters
for i in rest: #forloop to iterate each character in the string
    if i in [f"{j}" for j in range(10)]: #condition to check if the variable exist
        rest_c.append("0") #appends the character "0" to the list rest_c
        encryption.insert(0, i) #fucntion to insert the variable to the zero index to the encryption list
    else:
        rest_c.append(i) #append i if the condition above is false
#print(rest_c+"\n") #prints the rest_c list
#print(encryption+"\n") #prints the new encryption list
print("Encrypted text : ","".join(encryption+rest_c)) #prints the joined string of the lists