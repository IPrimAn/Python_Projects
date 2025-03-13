user_input = str(input("Enter your value:"))

title = user_input.title()
strip = title.strip()
print(strip)

first_found_index=0
for first_found_index in range(len(strip)):

first_found_index = strip.find(" ")
print (first_found_index)
without_backspace = strip.replace(" ", "", first_found_index)
print (without_backspace)
first_found_index =+1