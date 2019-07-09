f = open('names.txt', 'r')
d = f.read()
f.close
d = d.replace('"', '')
names = d.split(',')
names.sort()

def point(names):
    sigma = 0
    for i in range(len(names)):
        s = 0
        names[i] = names[i].lower()
        for a in names[i]:
            s += int(ord(a) - 96)
        sigma += s * (i + 1) 
    return sigma

print(point(names))