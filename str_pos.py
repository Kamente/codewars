def encode(i):
    result = ""
    for char in i:
        if char.isalpha():
            position = ord(char.lower()) - ord('a') + 1
            result += str(position)
        else:
            result += char
    return result

# example:
print(encode("adi"))
print(encode("ab@c"))