def f(word):
    nearby_keys = {'a': ['q', 'w', 's', 'x', 'z'],
                   'b': ['g', 'h', 'v', 'n'],
                   'c': ['d', 'f', 'x', 'v'],
                   'd': ['e', 'r', 's', 'f', 'x', 'c'],
                   'e': ['w', 'r', 's', 'd'],
                   'f': ['r', 't', 'd', 'g', 'c', 'v'],
                   'g': ['t', 'y', 'f', 'h', 'v', 'b'],
                   'h': ['y', 'u', 'g', 'j', 'b', 'n'],
                   'i': ['u', 'o', 'j', 'k'],
                   'j': ['u', 'i', 'h', 'k', 'n', 'm'],
                   'k': ['i', 'o', 'j', 'l', 'm', ','],
                   'l': ['o', 'p', 'k', ';', ',', '.'],        
                   'm': ['j', 'k', 'n', ','],
                   'n': ['h', 'j', 'b', 'm'],
                   'o': ['i', 'p', 'k', 'l'],
                   'p': ['o', '[', 'l', ';'],
                   'q': ['w', 'a', 's'],
                   'r': ['e', 't', 'd', 'f'],
                   's': ['w', 'e', 'a', 'd', 'z', 'x'],
                   't': ['r', 'y', 'f', 'g'],
                   'u': ['y', 'i', 'h', 'j'],
                   'v': ['f', 'g', 'c', 'b'],
                   'w': ['q', 'e', 'a', 's'],
                   'x': ['s', 'd', 'z', 'c'],
                   'y': ['t', 'u', 'g', 'h'],
                   'z': ['a', 's', 'x']}
    words = []
    for i in range(len(word)):   
        #Function that take a word and generate a list of adjacent transposed letters
        if i < len(word) - 1:
            word_temp = list(word)
            word_temp[i], word_temp[i + 1] = word_temp[i + 1], word_temp[i]
            words.append(''.join(word_temp))
            
        #Function that take a word and generate a list of adjacent double letters    
        word_temp = list(word)
        word_temp.insert(i, word_temp[i])
        words.append(''.join(word_temp))    
        
        #Function that take a word and generate a list of missed letters 
        # TODO
        
        #Function that take a word and generate a list of adjacent incorrect letters
        word_temp = list(word)
        for j in range(len(nearby_keys[word_temp[i]])):
            word_temp = list(word)
            word_temp[i] = nearby_keys[word_temp[i]][j]
            words.append(''.join(word_temp))
    return words


suggestion_words = dict()
with open('English Words.txt', 'r') as words:
    for word_to_learn in words:
        word_to_learn = word_to_learn.rstrip()
        suggestion_words[word_to_learn] = f(word_to_learn)

        
import json
with open('Dictionary of words and suggestion words.json', 'w') as s_words:
    json.dump(suggestion_words, s_words, indent=4)
    
    
import json
with open('Dictionary of words and suggestion words.json', 'r') as s_words:
    s_words = json.load(s_words)
    
    
word_to_test = 'helo'
suggestions = []
for k, v in s_words.items():
    if word_to_test in v:
        suggestions.append(k)  
if suggestions:         
    print(f'Did you mean {suggestions}?')     
