def morsify(text):
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
    output = []
    text = text.lower()
    for letter in text:
        print(morsemap[letter], " / ", end="")


morsify("hello")

