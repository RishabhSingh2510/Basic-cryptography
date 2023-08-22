import fileinput

file_path = 'file.txt'

def encryption():
    shift = 2
    finput = fileinput.input(files=file_path)
    for line in finput:
        shift +=1
        text = line
        encrypted = " "
        for i in text:
            if i.isupper():
                unicode = ord(i)
                index = ord(i)-ord('A')
                new_index = (index + shift)%26
                new_unicode = ord('A')+new_index
                new_charcter = chr(new_unicode)
                encrypted = encrypted + new_charcter
            elif i.islower():
                unicode = ord(i)
                index = unicode - ord('a')
                new_index = (index +shift)%26
                new_unicode = new_index + ord('a')
                new_character = chr(new_unicode)
                encrypted = encrypted + new_character
            elif i.isdigit():
                new_character = (int(i)+shift)%10
                encrypted += str(new_character)
            else:
                encrypted += i
    finput.close()
    return encrypted

def decryption():
    shift = 2
    finput = fileinput.input(files=file_path)
    for line in finput:
        shift +=1
        text = line
        decrypted = " "
        for i in text:
            if i.isupper():
                unicode = ord(i)
                index = unicode - ord('A')
                new_index = (index - shift)%26
                new_unicode = new_index + ord('A')
                new_character = chr(new_unicode)
                decrypted = decrypted + new_character
            elif i.islower():
                unicode = ord(i)
                index  = unicode - ord('a')
                new_index = (index - shift)%26
                new_unicode  = ord('a') + new_index
                new_character = chr(new_unicode)
                decrypted += new_character
            elif i.isdigit():
                org_digit = (int(i) - shift)%10
                decrypted += str(org_digit)
            else:
                decrypted += i
    finput.close()
    return decrypted
