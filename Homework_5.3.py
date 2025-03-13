import string

user_input = str(input("Enter your value:"))

title = user_input.title()
strip = title.strip()

count=strip.count(" ")

i=0
for i in range(count):
    found_index = strip.find(" ")
    if found_index>0:
        strip = strip.replace(" ", "", found_index)
        i = i+1
    else:
        break

prohibited_symbols = string.punctuation

for symbol in strip:
    if symbol in prohibited_symbols:
        strip=strip.replace(symbol,"")

print (f"#{strip[0:140]}")