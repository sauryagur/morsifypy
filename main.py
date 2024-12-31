morsemap = {
    'a': '⋅-',
    'b': '-⋅⋅⋅',
    'c': '-⋅-⋅',
    'd': '-⋅⋅',
    'e': '⋅',
    'f': '⋅⋅-⋅',
    'g': '--⋅',
    'h': '⋅⋅⋅⋅',
    'i': '⋅⋅',
    'j': '⋅---',
    'k': '-⋅-',
    'l': '⋅-⋅⋅',
    'm': '--',
    'n': '-⋅',
    'o': '---',
    'p': '⋅--⋅',
    'q': '--⋅-',
    'r': '⋅-⋅',
    's': '⋅⋅⋅',
    't': '-',
    'u': '⋅⋅-',
    'v': '⋅⋅⋅-',
    'w': '⋅--',
    'x': '-⋅⋅-',
    'y': '-⋅--',
    'z': '--⋅⋅',
    '1': '⋅----',
    '2': '⋅⋅---',
    '3': '⋅⋅⋅--',
    '4': '⋅⋅⋅⋅-',
    '5': '⋅⋅⋅⋅⋅',
    '6': '-⋅⋅⋅⋅',
    '7': '--⋅⋅⋅',
    '8': '---⋅⋅',
    '9': '----⋅',
    '0': '-----',
}

stringmap = {v: k for k, v in morsemap.items()}
stringmap[''] = ''

def morsify(text):
    output = ""
    text = text.lower()
    for letter in text:
        output += morsemap[letter] + " / "
    return output

def demorsify(morse):
    output = ""
    morse = morse.split(" / ")
    for morseletter in morse:
        output += stringmap[morseletter]
    return output


print(demorsify(morsify("289398738798dhu")))

