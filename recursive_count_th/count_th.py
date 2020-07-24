'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #counter starting at 0
    count = 0
    #base case
    #if length of word is 0
    if len(word) == 0:
        #return 0
        return 0
    #recursive case
    #elif word[0] == 't'
    elif word[0] == 't' and len(word) > 1:
        #if next letter is 'h':
        if word[1] == 'h':
            #count += 1 and recurse again, word[1:]
            return count+1 + count_th(word[1:])
        else:
            return count_th(word[1:])
    #otherwise move on
    else:
        #just recurse again word[1:]
        return count_th(word[1:])
    #return count
    return count

word = "abcthefthghith"
count_th(word)