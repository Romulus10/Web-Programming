f = open("count.txt", "r")
x = int(f.read())
x += 1
f.close()
f = open("count.txt", "w")
f.write(x)
f.close()
