from random import randint
iff = []
a = randint(3,20)
b = randint(1,a)
wiw = list(range(3,21))
for i in wiw :
    if a % i == 0:
        r = list(range(1, i))
        e = list(range(1, i))
        for w in r:
            for t in e:
                if (w + t) == i and w < t:
                        iff.append(w)
                        iff.append(t)
print(a)
print(iff)

