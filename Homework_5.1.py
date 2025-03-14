import keyword
import string
string_punctuation = ""
print (string.punctuation)
string_punctuation = string.punctuation.replace("_"," ")
print(string_punctuation)

test_data=["__","___"]

while True:

    your_variable = input('Input your symbols for variable and we will check it: ')

    if your_variable.islower() != True:
        print("False")
        continue

    if your_variable[0].isnumeric == True:
        print("False")
        continue

    for i in your_variable:
        if i in string_punctuation:
            print("False")
            break
        elif i in keyword.kwlist:
            print("False")
            continue
        elif i in test_data:
            print("False")
        else:
            break
    print("True")