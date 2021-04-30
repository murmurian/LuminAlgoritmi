numeroKaytetty = [False for i in range(6)]
ruudut = [0, 0, 0, 0, 0, 0, 0]
ratkaisuja = 0

def ratkaise(ruutu : int):
    global ratkaisuja
    if ruutu == 7:
        return
    if ruudut[0] + ruudut[1] + ruudut[3] + ruudut[4] == a and ruudut[1] + ruudut[2] + ruudut[4] + ruudut[5] == b and ruudut[5] != 0:
        print(ruudut[0:3])
        print(ruudut[3:6])
        ratkaisuja += 1
        print("Ratkaisuja:", ratkaisuja)
        return
    for i in range(1, 7):
        if ruudut[ruutu] == 0:
            if not numeroKaytetty[i - 1]:
                ruudut[ruutu] = i
                numeroKaytetty[i - 1] = True
                ratkaise(ruutu + 1)
                ruudut[ruutu] = 0
                numeroKaytetty[i - 1] = False

a = 14
b = 12

ratkaise(0)