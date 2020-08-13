# count up to 20 in 2s
for i in range(1, 21, 2):
    print(i, end=' ')
print("done 1")

# count up to 100 in 10s
for i in range(0, 101, 10):
    print(i, end=' ')
print("done 2")

# count down from 20
for i in range(20, 0, -1):
    print(i, end=' ')
print("done 3")

stars = int(input("how many stars? "))
star_prints = ""

# prints desired amount of stars
for i in range(stars):
    print("*", end='')
print(" done 4")

# prints desired amount of stars in "stair" pattern
for i in range(stars):
    star_prints = star_prints + "*"
    print(star_prints)
print("done 5")
