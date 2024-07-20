Mary_string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

def count_words(substring, Mary_string):
    """ This function takes in a string and substring, makes both strings lower case, then counts the number of substrings in the string. """
    substring_lower = substring.lower()
    Mary_string_lower = Mary_string.lower()
    # print(Mary_string_lower) added to return string during debugging
    # print(substring_lower) added to return string during debugging
    
    str_count = Mary_string_lower.count(substring_lower) # counting the substring in the givenstring
    # print(substring) added to return string during debugging
    # print(str_count) added to return string during debugging
    return(str_count)

substring = "little"
current_string_count = count_words(substring, Mary_string)
print(current_string_count)
