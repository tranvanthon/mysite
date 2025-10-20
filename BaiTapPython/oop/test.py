str1 = "English = 78 Science = 83 Math = 68 History = 65"
# Find total in string
s = 0
count = 0
a = str1.split()
for i in a:
    if i.isdigit():
        s = s + int(i)
        count += 1
print(s)

print(f"Average of str1 is: {s/count}")
