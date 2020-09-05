def vanda_om(text):
    return "".join(reversed(text))

hej = input("Vilken värld du avkoda? ")
nummer = input("Vilket viddnummer? ")
hnum = input("Vilket hnummer? ")

fil = open(".worlds/" + hej + "/iysfb134vx06732w8is88bvjx" + str(nummer) + "wibf23s" + str(hnum), "r")

text = fil.read()
fil.close()

bokstaver = "abPcdefghQijklmnowxyzåäABCDEFGHIJpqrstuvKLM4NORSTö(UVWXYZÅÄÖ :\n!?123567890.),"
f2 = open(".worlds/" + hej + "/nyckel", "r")
nyckel = f2.read()
f2.close()
stringen = ""
num = 0
while True:
    try:
        plats = nyckel.find(text[num])
    except IndexError:
        fil3 = open(input("Vad ska filen heta? "), "w")
        fil3.write(vanda_om(stringen))
        fil3.close()
        print(vanda_om(stringen))
        break
    stringen += bokstaver[plats]
    num += 1
