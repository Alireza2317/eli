#translating using dictionaries


E2I = {'bread':'pane', 'wine':'vino',  'with': 'con', 'I':'io', 
        'eat':'mangio', 'drink':'bevo', 'John':"Giovanni",
        'friends':'amici', 'and':'e', 'of':'di', 'red':'rosso'}
    
def translateW(w, d):
    if w in d.keys():
        return d[w]
    elif w != "":
        return '"' + w + '"'
    return w

def translate(f):
    #recognize words
    UCletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LCletters = "abcdefghijklmnopqrstuvxwyz"
    letters = UCletters + LCletters
    dictionary  = E2I
    word = ""
    translation = ""
    for c in f:
        if c in letters:
            word = word + c
        else:
            translation = translation + translateW(word, dictionary) +c 
            word = ""
    return translation + " " + translateW(word, dictionary)
    
    #substitute with the corresponding one
    
    
        
frase = input("what to translate?")

print(translate(frase))