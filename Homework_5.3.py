import string

user_input = str(input("Enter your value:"))

title = user_input.title()
strip = title.strip()

count=strip.count(" ")


for symbol in strip:
    strip = strip.replace(" ", "")

prohibited_symbols = string.punctuation

for symbol in strip:
    if symbol in prohibited_symbols:
        strip=strip.replace(symbol,"")

print (f"#{strip[0:140]}")