import re
a = "aibohphobia"
b = 8
print (re.compile(r"[^ ].{0," + str(b-2) + r"}[^ ](?= |\Z)").findall(a))
print (a==a[::-1])

key = "zabcdefghijklmnopqrstuvwxy"
table = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', key.encode('ascii'))

print(b'runoob'.translate(table, b'o'))