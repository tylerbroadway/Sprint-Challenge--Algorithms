'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # check to see if the word has less than 2 characters. 
    if len(word) < 2:
        # If so, return 0, because an instance of "th" is not possible
        return 0
    elif word [:2] == "th":
        # If the first 2 characters in the word are "th", recursively return count_th + 1
        return 1 + count_th(word[1:])
    else:
        # Else, just call count_th, starting with the 2nd character in the word.
        return count_th(word[1:])
