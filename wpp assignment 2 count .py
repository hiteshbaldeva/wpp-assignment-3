
text = input("Enter your text: ")
value = input("Enter value to find: ")
count = 0

for i in range(len(text)):
    if text[i:i+len(value)] == value:
        if i + len(value) == len(text) or text[i+len(value)] == ' ':
            count += 1

print("Occurrence:", count)