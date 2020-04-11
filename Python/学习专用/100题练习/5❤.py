a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
d = int(input('d:'))
e = int(input('e:'))
arr = [a,b,c,d,e]
words = []
for i in range (4,-1,-1):
    x = arr[0]
    for j in range(0,i):
        if x > arr[j+1]:
            x = arr[j+1]
    words.append(x)
    arr.remove(x)        
for word in words:
    print(word)
print(words)

