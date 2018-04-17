import opratka

#výjimky: ne číslo, jen len(pismeno) == 1

zvolene_slovo = opratka.zvol_slovo()

def hledani(sluvko, pismenko):
    #print(sluvko)

    if pismenko in sluvko:
        print("Ano, to tam je!")
        pozice = sluvko.index(pismenko) * 2
        opratka.retezec = opratka.retezec[:pozice] + pismenko + opratka.retezec[pozice + 1:]

        if sluvko.count(pismenko) > 1:
            pozice = sluvko.index(pismenko, pozice) * 2
            opratka.retezec = opratka.retezec[:pozice] + pismenko + opratka.retezec[pozice + 1:]

    else:
        print("Ne, to tam není.")
        opratka.pocet_chyb += 1
        opratka.sibenice()

    print(opratka.retezec)

def hra():
    while "_" in opratka.retezec:
        hledani(zvolene_slovo, input("Jaké zkusíš písmeno? "))



        if opratka.pocet_chyb == 10:
            print("Sorry, už visíš. Zkus to znovu.")
            break

    if "_" not in opratka.retezec:
        print("Gratulace, vyhrálas!")
