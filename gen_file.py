fi = open("data/level.txt", mode="wt", encoding="UTF-8")

for i in range(100):
    for j in range(100):
        fi.write("0")
    fi.write("\n")
