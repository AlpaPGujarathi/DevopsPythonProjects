def reverseStr(string1):
    revstring = ""
    for i in string1:
        revstring = i + revstring
    return revstring




str = "My name is Alpa"

print(reverseStr(str))
