def mockText(original, handle):
    newtext = handle + " "
    i = newtext.len()
    for character in original:
        if i == 160:
            return newtext
        else if i % 2 == 0:
            newtext += character.upper()
        else:
            newtext += character.lower()
        i+=1
    return newtext
