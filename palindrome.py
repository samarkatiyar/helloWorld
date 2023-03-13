word = input("Enter a word that you want to know if it's palindrome or not --->")
#if word[0:len(word)] == word[int(len(word)/2):len(word)]:
#    print ('IT IS')
#else:
#    print('IT IS NOT')
reverse_word=''
for letter in word:
    reverse_word = letter + reverse_word
    #print("===> " + reverse_word)

if word == reverse_word:
    print("Bingo!!! Its a palindrome")
else:
    print("it is not")
