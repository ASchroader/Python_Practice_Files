# TextAnalyzer - analyzes a string of text to look for frequency of words and look for a specific word
# Python class project - I admit I had to peek and look up some things to complete this. However, this looks useful for future project and worth building upon, so keeping. 

class TextAnalyzer(object):
    # The __init__ method initializes the class with a 'text' parameter.
    # You will store the provided 'text' as an instance variable.
    def __init__(self, text):
        self.text = text
        # convert text to lowercase
        lower_text = text.lower()
        # remove punctuation
        formatted_text = lower_text.replace('.','').replace('!','').replace('?','').replace(',','')
        self.fmtText = formatted_text

    def freqAll(self):
        # split string into a dictionary (as key) and then get a count of each word
        word_list = self.fmtText.split(' ')
        word_map = {}
        for word in set(word_list):
            word_map[word] = word_list.count(word)
        return(word_map)

    def freqOf(self,word):
      # using the dictionary in freqAll, see if a word is in it and return the count
        freqDict = self.freqAll()
        if word in freqDict:
            return(freqDict[word])
        else:
            return 0

# Now instansiate the object and call functions and methods
given_string="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
Analyze = TextAnalyzer(given_string)

# Make sure the string looks lower case and has the punctuation removed
print("formatted text: ", Analyze.fmtText)

# This is calling the method to count the words
List_of_Words_Count = Analyze.freqAll()
print(List_of_Words_Count)

# and lastly, looking for a specific word
word = "lorem"
Specific_Word_Count = Analyze.freqOf(word)
print(Specific_Word_Count)

# Ideas for expansion: let the user input the string and the word they are looking for, add error handling, eventually use this on a data stream w/ 100's to 1000's of strings

        
