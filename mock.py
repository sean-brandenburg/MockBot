def mockText(original, handle):
    newtext = handle + " "
    i = len(newtext)
    for character in original:
        if(i == 160):
            return newtext
        elif(i % 2 == 0):
            newtext += character.upper()
        else:
            newtext += character.lower()
        i+=1
    return newtext
