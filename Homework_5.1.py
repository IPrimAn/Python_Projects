import keyword
import string
string_punctuation = ""
print (string.punctuation)
string_punctuation = string.punctuation.replace("_"," ")
print(string_punctuation)

test_data=["__","___"]

while True:

    your_variable = input('Input your symbols for variable and we will check it: ')

    for i in your_variable:
        if i in string_punctuation:
            print("False")
            break
    for i in your_variable:
        if your_variable in keyword.kwlist:
            print("False")
            break
    for i in your_variable:
        if your_variable in test_data:
            print("False")
            break
    for i in your_variable:
        if your_variable.isnumeric :
            print("False")
            break

    # if your_variable.islower() != True:
    #     print("False")
    #     break
    # if your_variable[0].isnumeric == True:
    #     print("False")
    #     continue
