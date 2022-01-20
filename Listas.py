import base64

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


for x in range(1,1000):
    y = str(x)
    y = y.encode()
    y = base64.b64encode(y)
    print(x, end='[')
    print(y,end=']')
    print(" ", end = '')
    if (x/10) == (int(x/10)): 
       print(" ")





