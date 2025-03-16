import keyword
import string
string_punctuation = ""
print (string.punctuation)
string_punctuation = string.punctuation.replace("_"," ")
print(string_punctuation)
string.ascii_uppercase

test_data=["__","___"]

while True:

    your_variable = input('Input your symbols for variable and we will check it: ')

    for i in your_variable:
        if i in string_punctuation:
            print("False")
            exit()
    for i in your_variable:
        if your_variable in keyword.kwlist:
            print("False")
            exit()
    for i in your_variable:
        if your_variable in test_data:
            print("False")
            break

    first_value=your_variable[0]

    if first_value.isnumeric()== True:
        print("False")
        continue

    for i in your_variable:
        if i in string.ascii_uppercase:
            print("False")
            break
    else:
        print("True")
