#lost in translation

E2I = {'bread':'pane', 'wine':'vino',  'with': 'con', 'I':'io', 
        'eat':'mangio', 'drink':'bevo', 'John':"Giovanni",
        'friends':'amici', 'and':'e', 'of':'di', 'red':'rosso'}

def translator(s, d):
    '''
    transliterates each word from english to italian using the dictionary d
    '''
    result = ""
    s = s.split()
    for w in s:
        if w in d:
            result = result + d[w] + " "
        else:
            result = result + "\"" + w +"\" "
    return result

s = input("insert a simple englis sentence: ")
print(f"that in italian is: {translator(s,E2I)}")