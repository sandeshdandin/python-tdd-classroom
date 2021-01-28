class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        return character.lower() in 'aeiou'

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        text_list=sentence.split()        
        maxx=0
        ind=0
        i=0
        for item in text_list:
            if maxx<len(item):
                maxx=len(item)
                ind=i
            i=i+1
        return text_list[ind]

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        text_list=text.split()
        len_list=list()
        for item in text_list:
            len_list.append(len(item))        
        return len_list