# Define a word as a sequence of consecutive English letters. Find the longest 
# word from the given string.

def solution(text):

    words = ['']

    for char in text:
        if char.isalpha():
            words[-1] += char
        elif words[-1] != '':
            words.append('')
        else:
            pass

    lengths = [len(word) for word in words]
    k = lengths.index(max(lengths))

    return words[k]

# passed all tests