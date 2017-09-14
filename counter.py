f = open("count.txt", "r")
try:
    x = int(f.read())
except ValueError:
    x = 0
x += 1
f.close()
f = open("count.txt", "w")
f.write(str(x))
f.close()
