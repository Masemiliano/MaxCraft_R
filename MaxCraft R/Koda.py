def vanda_om(text):
    return "".join(reversed(text))

hej = input("Vilken fil du koda? ")
nummer = input("Vilket viddnummer? ")
hnum = input("Vilket hnummer? ")

v = input("Vad heter världen? ")

fil = open(hej)

text = fil.read()
fil.close()

bokstaver = "abPcdefghQijklmnowxyzåäABCDEFGHIJpqrstuvKLM4NORSTö(UVWXYZÅÄÖ :\n!?123567890.),"
f2 = open(".worlds/" + v + "/nyckel", "r")
nyckel = f2.read()
f2.close()
stringen = ""
num = 0
while True:
    try:
        plats = bokstaver.find(text[num])
    except IndexError:
        fil3 = open(".worlds/" + v + "/iysfb134vx06732w8is88bvjx" + str(nummer) + "wibf23s" + str(hnum), "w")
        fil3.write(vanda_om(stringen))
        fil3.close()
        print(vanda_om(stringen))
        break
    stringen += nyckel[plats]
    num += 1
