#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
file = open('IntroductoryCS.txt') # This line of code will open the 'IntroductoryCS.txt' and store the content of the file in the variable named file. 
words = file.read().split()# This line of code will read the file and split the content of the file into seperate words. This information will be stored in the variable name words. 
word_freq = {} # This line of code creates an empty dictionary named word_freq. This will store the frequency of the words that occur in the file and the word itself.
new_word=[] # This line of code creates an empty list named new_word. it will be used to store words so that characters are removed.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#
for i in words: 
    if i.isalpha():  # this is will use a for loop that will go through each word in the file and check if it is a word or not. by checking whether the string consists of alphabetic characters only
        new_word.append(i) # if a word is made of alphabetic characters only then it is placed in the list called new_word. 
    else:
        word = [] # if the word contains non alphabetic characters then the code below is executed
        for char in i: # This part of the code will go through each character in the words that contains non alphabetic characters using a for loop.
            if char.isalpha() or char == "'": 
                word.append(char) # if the character is an alphabetic character or the character is an apostrophe then the word is put together and stored in the list named word
        temp_str = ''.join(word) # these words are added onto an empty string named temp
        new_word.append(temp_str) # they are then added to the list named new_word. 

for i in new_word: # this goes through all the words in the list new_word
    if i.isalpha(): # if the words contain alphabetic characters only then the code below is executed.
        if i in word_freq: # if the word is already in the dictionary named word_frequency then 1 is added to the value of the key for the word.
            word_freq[i] += 1
        else: # if it is not already in the dictionary then the word is added to the dictionary and 1 is placed as it's value.
            word_freq[i] = 1
    else: # if it is not a word that doesn't contain alphabetic characters only then the code below is executed.
        for char in i: # the for loop will go through each character.
            if char == "'": # if it contains an apostrophe then the word is added to the dictionary and 1 is placed in the value of the word. 
                word_freq[i] = 1
                
            else:
                pass # else the word is passed and nothing is done to the word.
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

for word, frequency in sorted(word_freq.items(), reverse=True, key=lambda  item: item[1]): 
    print("'"+word+"' occurs",frequency,"times.")
# this for loop will go through the dictionary and saves the key (word) and the value as (frequency) from the word.freq dictionary.
# (reverse=True, key=lambda  item: item[1]) This section of the for loop will order the items in numerical order. Reverse=True will make the list go in reverse so the order will be the most frequent words first to the least frequent words.

# print("'"+word+"' occurs",frequency,"times.") this will print the key with quotations around the word. followed by the word 'occurs' and the value and then the word 'times'.
# I've done this so that the user can read the most frequent words more easily and the program is more user friendly. 
