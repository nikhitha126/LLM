def Capitalize(string, letter):
    index = string.lower().find(letter.lower())
    if index == -1:
        return string.lower()
    return string[:index].lower() + string[index:].upper()
print(Capitalize("CAtCHa", "a"))
print(Capitalize("Preteen", "e"))
print(Capitalize("You've got this", "m"))
print(Capitalize("Keep trying", "k"))
