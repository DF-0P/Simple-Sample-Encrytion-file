# Simple-Sample-Encrytion-file
This is a  simple encryption and decryption file to a question i came across on facebook... i found the question and decided to make the files according to the question


Facebook post i saw the question at : https://www.facebook.com/groups/pythonprogrammingbeginners/permalink/1609213246095494/?app=fbl

my own Facebook Post about it : https://www.facebook.com/D.F.0P.1694/posts/pfbid0xfnardGDDwbbVpm3ez3vuJ4gtxd4qmkcQ9ZG2msgvkB58kixUa84bWzDzCUzmKenl


the main post text:
Complement of the season to all Programmers in the house .
  Kindly rough out an algorithm for this problem below.(any help would be appreciated 🙏)
===========================
1. Password Decryption
In a computer security course, you just learned about password decryption. Your fellow student has created their own password encryption method, and they've asked you to test how secure it is. Your task is to recover the original password given the encrypted password provided to you by your classmate.
At first, it seems impossible. But one day after class, you catch a peek of your classmate's notebook where the encryption process is noted. You snap a quick picture of it to reference later. It says this:
Given string s, let s[i] represent the ith character in the string s, using 0-based indexing.
Initially i = 0.
If s[i] is lowercase and the next character s[i+1] is uppercase, swap them, add a '*' after them, and move to i+2.
If s[i] is a number, replace it with 0, place the original number at the start, and move to i+1.
Else, move to i+1.
Stop if i is more than or equal to the string length. Otherwise, go to step 2.
There's even an example mentioned in the notebook. When encrypted, the string "hAck3rr4nk" becomes "43Ah*ck0rr0nk". (Note: the original string, "hAck3rr4nk", does not contain the character 0.)
Note:
The original string always contains digits from 1 to 9 and does not contain 0.
The original string always contains only alpha-numeric characters.
Using this information, your task is to determine the original password (before encryption) when given the encrypted password from your classmate.
Function Description
Complete the function decryptPassword in the editor below. decryptPassword must return the original password string before it was encrypted by your classmate.
decryptPassword has the following parameter:
    s:  the password string after it was encrypted by your classmate
Constraints
1 ≤ length of s ≤ 105
