import pygame
import random
import os
import time

pygame.init()

vidd, hoejd = 1000, 600

gameDisplay = pygame.display.set_mode((vidd, hoejd))

jord = pygame.image.load(".bilder/Jord.png")
sand = pygame.image.load(".bilder/Sand.png")
sten = pygame.image.load(".bilder/Sten.png")
trae = pygame.image.load(".bilder/Trae.png")
graes = pygame.image.load(".bilder/Graes.png")
diamant = pygame.image.load(".bilder/Diamant.png")

person = pygame.image.load(".bilder/Person.png")
zombie = pygame.image.load(".bilder/Zombie.png")
ko = pygame.image.load(".bilder/Ko.png")

mus = pygame.image.load(".bilder/Mus.png")
pekmus = pygame.image.load(".bilder/Pekmus.png")
kryss = pygame.image.load(".bilder/Kryss.png")

block = ["jord", "sand", "sten", "trae", "graes", "diamant"]
bn = []
num = 0
for var in block:
    bn.append(0)

bakgrundsfarg = (0, 0, 255)

speed = 3

pappernu = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]


def nodvandiga_mappar():
    global name
    try:
        os.mkdir(".worlds")
    except os.error:
        pass

    # måste vara underst
    try:
        os.mkdir(".worlds/" + name)
        f = open(".worlds/" + name + "/nsjnfkjgvdkjny", "w")
        string = "abPcdefghQijklmnowxyzåäABCDEF%GHIJpqrstuvKLM4NORSTö(UVWXYZÅÄÖ :\n!?123567/ˆ¨˜*|-"
        while True:
            if string == "":
                f.close()
                return "finns inte"
            bs = random.choice(string)
            f.write(bs)
            string = string.replace(bs, "")
    except os.error:
        return "finns"


def nodvandiga_mappar_oppna():
    global name
    try:
        os.mkdir(".worlds")
    except os.error:
        pass

    # måste vara underst
    try:
        # bara checkar om den finns, tar sedan bort den
        os.mkdir(".worlds/" + name)
        os.rmdir(".worlds/" + name)
        return "finns inte"
    except os.error:
        return "finns"


def skriv(text, tx=400, ty=300, storlek=75, farg=(0, 0, 0)):
    font = pygame.font.SysFont(None, storlek)
    txt = font.render(text, True, farg)
    gameDisplay.blit(txt, (tx, ty))


def pygame_input(fraga):
    namn3 = ""
    while True:

        gameDisplay.fill((0, 245, 100))

        skriv(fraga, 0, 100, 50)

        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            key = pygame.key.name(event.key)  # Returns string id of pressed key.

            if len(key) == 1:  # This covers all letters and numbers not on numpad.
                if keys[pygame.K_LCTRL] and keys[pygame.K_v]:
                    try:
                        import clipboard
                        namn3 += clipboard.paste()
                    except ModuleNotFoundError:
                        pass
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:

                    namn3 += key.upper()
                else:
                    namn3 += key

            elif key == "backspace":
                namn3 = namn3[:len(namn3) - 1]
            elif key == "space":
                namn3 += " "
            elif event.key == pygame.K_RETURN:
                return namn3

        skriv(namn3, 0, 300, 50)
        pygame.display.update()


name = ""


def menu():
    global blittat
    global name
    global x, y
    global sida
    global usida
    global bn
    pygame.mouse.set_visible(False)
    musx, musy = 0, 0
    farg = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 525 > musx > 400 and 500 < musy < 530:
                    pygame.quit()
                    quit()
                if 535 > musx > 400 and 300 < musy < 330:
                    name = pygame_input("Vad ska den heta? ")
                    finns = nodvandiga_mappar()
                    if finns == "finns":
                        gameDisplay.fill((255, 0, 0))
                        skriv("Den finns redan.")
                        pygame.display.update()
                        time.sleep(2)
                    else:
                        x, y = round(vidd / 2), 50
                        sida, usida = 0, 0
                        num5 = 0
                        for var3 in bn:
                            if var3:
                                pass
                            bn[num5] = 0
                            num5 += 1
                        main()
                if 515 > musx > 400 and 400 < musy < 430:
                    name = pygame_input("Vad heter den? ")
                    finns = nodvandiga_mappar_oppna()
                    if finns == "finns inte":
                        gameDisplay.fill((255, 0, 0))
                        skriv("Den finns inte.")
                        pygame.display.update()
                        time.sleep(2)
                    else:
                        x, y = round(vidd / 2), 50
                        blittat = False
                        main()

        muspos = pygame.mouse.get_pos()
        musx, musy = muspos

        # originalet i R var (255, 100, 29)        
        gameDisplay.fill((100, 100, 255))
        skriv("MaxCraft R", 200, 100, 70, farg)
        skriv("Ny värld", 400, 300, 50)
        skriv("Öppna", 400, 400, 50)
        skriv("Avsluta", 400, 500, 50)

        if 535 > musx > 400 and 300 < musy < 330 or 515 > musx > 400 and 400 < musy < 430 or 525 > musx > 400 and 500 <\
                musy < 530:
            peka = True
        else:
            peka = False

        if peka:
            gameDisplay.blit(pekmus, muspos)
        else:
            gameDisplay.blit(mus, muspos)
        pygame.display.update()


# om man lägger till zip nån gång, tar texten från txt i zip      
def get_txt(var2):
    nu = str(var2)[2:]
    return nu[:-1]


def koda(text):
    bokstaver = "abPcdefghQijklmnowxyzåäABCDEFGHIJpqrstuvKLM4NORSTö(UVWXYZÅÄÖ :\n!?123567890.),-%"
    f2 = open(".worlds/" + name + "/nsjnfkjgvdkjny", "r")
    nyckel = f2.read()
    f2.close()
    stringen = ""
    num3 = 0
    while True:
        try:
            plats = bokstaver.find(text[num3])
        except IndexError:
            return vanda_om(stringen)
        stringen += nyckel[plats]
        num3 += 1


def avkoda(text):
    bokstaver = "abPcdefghQijklmnowxyzåäABCDEFGHIJpqrstuvKLM4NORSTö(UVWXYZÅÄÖ :\n!?123567890.),-%"
    f2 = open(".worlds/" + name + "/nsjnfkjgvdkjny", "r")
    nyckel = f2.read()
    f2.close()
    stringen = ""
    num4 = 0
    while True:
        try:
            plats = nyckel.find(text[num4])
        except IndexError:
            return vanda_om(stringen)
        stringen += bokstaver[plats]
        num4 += 1


def save_paper():
    global sida
    global usida
    sidnu = str(pappernu).replace("[", "")
    sidnu = sidnu.replace("]", "")
    sidnu = sidnu.replace("'", "")
    sidnu = koda(sidnu)
    fil = open(".worlds/" + name + "/iysfb134vx06732w8is88bvjx" + str(sida) + "wibf23s" + str(usida), "w")
    fil.write(sidnu)
    fil.close()


def paper_handler():
    global pappernu
    global sida
    global usida
    global blittat
    num2 = 0
    try:
        fil2 = open(".worlds/" + name + "/iysfb134vx06732w8is88bvjx" + str(sida) + "wibf23s" + str(usida), "r")
        nusid = fil2.read()
        nusid = avkoda(nusid)
        pappernu = nusid.split(", ")

    except FileNotFoundError:
        biom = random.randint(1, 3)
        if usida > 0:
            biom = 0
        if usida < 0:
            biom = -1
        while True:
            if biom == -1:
                pappernu[num2] = "luft"

            if biom == 0:
                pappernu[num2] = "sten"
                diamantkanske = random.randint(0, 150)
                if diamantkanske == 0:
                    pappernu[num2] = "diamant"

            if biom == 1:
                vad = random.randint(1, 2)
                if num2 > 159:
                    if vad == 1:
                        pappernu[num2] = "sand"
                    elif vad == 2:
                        pappernu[num2] = "jord"
                    else:
                        pappernu[num2] = "luft"
                else:
                    pappernu[num2] = "luft"
                    if num2 > 139:
                        gk = random.randint(1, 2)
                        if gk == 1:
                            pappernu[num2] = "graes"
            if biom == 2:
                vad = random.randint(1, 2)
                if vad == 1:
                    pappernu[num2] = "trae"
                if vad == 2:
                    pappernu[num2] = "luft"
                if num2 > 159:
                    pappernu[num2] = "jord"

            if biom == 3:
                vad = random.randint(1, 3)
                if vad == 1:
                    pappernu[num2] = "sten"
                else:
                    pappernu[num2] = "luft"
                if num2 - 20 > -1:
                    if pappernu[num2 - 20] == "sten":
                        pappernu[num2] = "sten"

            num2 += 1
            if num2 > 239:
                blittat = False
                break


def fa_pos(nummer):
    xf = (nummer % 20) * 50
    yf = int(nummer / 20) * 50
    return xf, yf


def vanda_om(text):
    return "".join(reversed(text))


blittat = False
x, y = round(vidd / 2), 50
kx, ky = 0, 0
hall = "h"
bakgrund = pygame.Surface((vidd, hoejd))


def rita_allt():
    global blittat
    global pappernu
    global x
    global y
    global bakgrund
    global kx
    global ky

    blittnum = 0
    if not blittat:
        gameDisplay.fill(bakgrundsfarg)
    while not blittat:
        if pappernu[blittnum] != "luft":
            try:
                gameDisplay.blit(globals()[pappernu[blittnum]], (fa_pos(blittnum)))
            except KeyError:
                pass
        blittnum += 1
        if blittnum > 239:
            nubild = pygame.Surface((vidd, hoejd))
            nubild.blit(gameDisplay, (0, 0))
            bakgrund = nubild
            blittat = True
    gameDisplay.blit(bakgrund, (0, 0))
    gameDisplay.blit(person, (x, y))
    if hall == "h":
        kx = x + 75
        ky = y + 25
    if hall == "v":
        kx = x - 25
        ky = y + 25
    if hall == "u":
        kx = x + 25
        ky = y - 25
    if hall == "n":
        kx = x + 25
        ky = y + 75
    if bn[block.index(halleri)] > 0:
        gameDisplay.blit(pygame.transform.scale(globals()[halleri], (20, 20)), (kx, ky))
    gameDisplay.blit(kryss, (kx, ky))


hopp = False
hoppnum = 0


def player_actions():
    global x
    global y
    global hall
    global hopp
    global hoppnum
    global kx
    global ky
    global blittat
    global pappernu
    global block

    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:
        paper_handler()

    try:
        if gameDisplay.get_at((x + 25, y + 50)) == bakgrundsfarg and not hopp and -25 < x and x + 50 < 1025:
            y += speed + 3
    except IndexError:
        if y + 55 > hoejd:
            y += speed + 3

    if keys[pygame.K_LEFT]:
        try:
            if gameDisplay.get_at((x - 3, y + 5)) == bakgrundsfarg:
                x -= speed
        except IndexError:
            if x - 4 < 0:
                x -= speed
        hall = "v"

    if keys[pygame.K_RIGHT]:
        try:
            if gameDisplay.get_at((x + 53, y + 5)) == bakgrundsfarg:
                x += speed
        except IndexError:
            if x + 54 > 1000:
                x += speed
        hall = "h"

    if keys[pygame.K_UP]:
        hall = "u"
    if keys[pygame.K_DOWN]:
        hall = "n"

    if keys[pygame.K_SPACE]:
        if not hopp:
            hopp = True
            hoppnum = 0

    if hopp:
        try:
            if gameDisplay.get_at((x + 25, y - 3)) == bakgrundsfarg:
                y -= speed
            else:
                hopp = False
        except IndexError:
            if y - 5 < 0:
                y -= speed
        hoppnum += 1
        if hoppnum > 30:
            hopp = False

    # blockhandlings
    if keys[pygame.K_x]:
        if 1000 > kx > 0 and 600 > ky > 0:
            bx = int(kx / 50)
            by = int(ky / 50)
            pblock = by * 20 + bx
            btyp = pappernu[pblock]
            if btyp != "luft":
                bn[block.index(btyp)] += 1
                pappernu[pblock] = "luft"
                blittat = False
    if keys[pygame.K_v]:
        if 1000 > kx > 0 and 600 > ky > 0 and bn[block.index(halleri)] > 0:
            bx = int(kx / 50)
            by = int(ky / 50)
            pblock = by * 20 + bx
            if pappernu[pblock] == "luft":
                bn[block.index(halleri)] -= 1
                pappernu[pblock] = halleri
                blittat = False


sida = 0
usida = 0

hnum = 0
halleri = "jord"


def in_game_meny():
    while True:
        muspos = pygame.mouse.get_pos()
        musx, musy = muspos

        rita_allt()
        skriv("Fortsätt", 400, 200)
        skriv("Meny", 400, 300)
        skriv("Avsluta", 400, 400)

        if 600 > musx > 400 and 200 < musy < 250 or 585 > musx > 400 and 400 < musy < 450 or 535 > musx > 400 and 300 <\
                musy < 350:
            gameDisplay.blit(pekmus, muspos)

        else:
            gameDisplay.blit(mus, muspos)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 600 > musx > 400 and 200 < musy < 250:
                    return
                if 585 > musx > 400 and 400 < musy < 450:
                    avsluta()
                if 535 > musx > 400 and 300 < musy < 350:
                    return "meny"

        pygame.display.update()


def avsluta(ut=True):  # om programmet ska exita
    save_paper()
    # sparar blocksiffrorna
    f = open(".worlds/" + name + "/sibfhikrbkafmcb", "w")
    nub = str(bn).replace("]", "")
    nub = nub.replace("[", "")
    nub = nub.replace("'", "")
    f.write(koda(nub))
    f.close()
    # sparar pappret man är på så att man börjar där nästa gång
    f2 = open(".worlds/" + name + "/aiduhfsghiysfgimcs", "w")
    f2.write(koda(str(sida) + "!" + str(usida)))
    f2.close()
    if ut:
        pygame.quit()
        quit()


# fixar alla data som inte är världen innan man börjar spela
def infor():
    global bn
    global sida
    global usida
    try:
        f = open(".worlds/" + name + "/sibfhikrbkafmcb", "r")
        v = avkoda(f.read())
        f.close()
        bn = v.split(", ")
        num5 = 0
        for var3 in bn:
            bn[num5] = int(var3)
            num5 += 1
    except FileNotFoundError:
        pass
    try:
        f2 = open(".worlds/" + name + "/aiduhfsghiysfgimcs", "r")
        v2 = avkoda(f2.read())
        f2.close()
        sida = int(v2.split("!")[0])
        usida = int(v2.split("!")[1])
    except FileNotFoundError:
        pass


class ai:
    def __init__(self, aix, aiy, typ):
        self.x = aix
        self.y = aiy
        self.typ = typ
        self.hnum = 0
        self.hopp = False
        if typ == "zombie":
            self.hoejd = 100
            self.vidd = 50
        if typ == "ko":
            self.hoejd = 50
            self.vidd = 100

    def hoppa(self):
        self.hnum += 1
        self.y -= 4
        if self.hnum > 30:
            self.hopp = False

    def rita(self):
        gameDisplay.blit(globals()[self.typ], (self.x, self.y))

    def aktivera_hopp(self):
        try:
            if gameDisplay.get_at((self.x + 10, self. y + self.hoejd + 1)) != bakgrundsfarg:
                self.hopp = True
                self.hnum = 0
        except IndexError:
            pass

    def rora_sig(self):
        self.rita()
        global x
        global y
        if self.typ == "zombie":
            if x > self.x:
                self.x += 1
            if self.x > x:
                self.x -= 1
            if self.y > y and self.hopp is False:
                self.aktivera_hopp()
        if self.typ == "ko":
            if not self.hopp:
                self.aktivera_hopp()
        try:
            if gameDisplay.get_at((self.x, self.y + self.hoejd)) == bakgrundsfarg:
                if self.hopp is False:
                    self.y += speed + 3
        except IndexError:
            if self.y < 0:
                self.y += 3
        if self.hopp is True:
            self.hoppa()


def main():
    clock = pygame.time.Clock()
    infor()
    paper_handler()
    global blittat
    global pappernu
    global x
    global y
    global bakgrundsfarg
    global speed
    global hall
    global sida
    global usida
    global hnum
    global halleri
    z = ai(700, 400, "ko")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                avsluta()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_q] or key[pygame.K_ESCAPE]:
                    menykanske = in_game_meny()
                    if menykanske == "meny":
                        avsluta(False)
                        return
                if key[pygame.K_n]:
                    hnum += 1
                    try:
                        halleri = block[hnum]
                    except IndexError:
                        hnum = 0
                        halleri = block[hnum]
                    for var4 in block:
                        if var4:
                            pass
                        if bn[block.index(halleri)] < 1:
                            hnum += 1
                            try:
                                halleri = block[hnum]
                            except IndexError:
                                hnum = 0
                                halleri = block[hnum]
                        else:
                            break

        rita_allt()
        player_actions()
        skriv(str(bn[block.index(halleri)]), int(vidd / 2), hoejd - 40, 30,
              (255, 255, 255))  # måste vara under player_actions för att inte spelaren ska kunna stå på siffran

        if x > 1000:
            save_paper()
            sida += 1
            paper_handler()
            x = 0
            blittat = False
        if x < -50:
            save_paper()
            sida -= 1
            paper_handler()
            x = 950
            blittat = False
        if y > 600:
            save_paper()
            usida += 1
            paper_handler()
            y = 0
            blittat = False
        if y < -50:
            save_paper()
            usida -= 1
            paper_handler()
            y = 500
            blittat = False

        for ais in ai:
            ais.rora_sig()

        pygame.display.update()


menu()
