dectxt = "434891Gh*00l0fkjdklvoir000"#input("What is the text to decrypt:\n>") #text to decrypt
nums= {} #dictionary to store index of numbers before any letter
for idx, i in enumerate(dectxt): #for loop to run against getting number forindex
    if i in list(f"{i}" for i in range(10)):
        nums[idx] = i
    else:
        break
dectxt_s = dectxt[max([i for i in nums.keys()])+1:] #assigning a new list for characters after all number have been gotten
#rint(dectxt_s) #prints the new list


def decrypt(s, n): #function for decrypting the rest of the characters after the first three characters of the new string
    d = max(j for j in n) #gets the max of the dictionary keys in nums
    #print(d)  #prints the maximum of the dictionary keys
    for i in s:
        if i == "0":
            reformat.append(nums[d])
            d -=1
        else:
            reformat.append(i)

#time to rearrange the rest of the function
reformat = [] #empty list to store all the new remade strings
i = 0 #counter constant
if dectxt_s[i].isupper() and dectxt_s[i+1].islower() and dectxt_s[i+2] == "*": #if statement to run through the first 3 characters of  the new string list
    reformat.append(dectxt_s[i+1])
    reformat.append(dectxt_s[i])
    i += 2
    decrypt(dectxt_s[i+1:], nums.keys()) #run the decrypt function
else: #else statement to append as it is, the arrangement assuming the condition results to false
    reformat.append(dectxt_s[i])
    reformat.append(dectxt_s[i+1])
    i += 1
    decrypt(dectxt_s[i+1:], nums.keys())
print("Decrypted text: ","".join(reformat))

