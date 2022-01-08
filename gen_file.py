from random import randint

fi = open("data/level.txt", mode="wt", encoding="UTF-8")

for i in range(100):
    for j in range(100):
        if (i >= 100 - 15 or i <= 15 or j >= 100 - 15 or j <= 15) and i % 2 != 0 and j % 2 != 0:
            fi.write("I")
        else:
            ran = randint(0, 150)
            print(ran)
            if ran == 2:
                fi.write("m")
            elif ran == 1:
                fi.write("M")
            else:
                fi.write('0')

            # else:
            #     fi.write("M")

    fi.write("\n")


# for i in range(100):
#     for j in range(100):
#         fi.write("0")
#
#     fi.write("\n")
