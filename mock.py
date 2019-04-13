def mockText(original):
    newtext = ""
    i = 0
    for character in original:
        if i % 2 == 0:
            newtext += character.upper()
        else:
            newtext += character.lower()
        i+=1
    return newtext
