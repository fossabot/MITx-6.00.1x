test = 'abcdefgaaaaabbb'
quad = 'ab'
for i in quad:
    if i in test:
        test = test.replace(i,'',1)

print("This is test  " + test)
print("This is test  " + quad)