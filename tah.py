import opratka

zvolene_slovo = opratka.zvol_slovo()
#odpoved = input("Jaké zkusíš písmeno? ")

def over_delku(pismena):
    if len(pismena) == 1:
        return True
    else:
        return False

def over_pismeno(cislo):

    try:
        number = int(cislo)
    except ValueError:
        return True
    else:
        return False

def hledani(sluvko, pismenko):

    if pismenko in sluvko:
        print("Ano, to tam je!")
        pozice = sluvko.index(pismenko) * 2
        opratka.retezec = opratka.retezec[:pozice] + pismenko + opratka.retezec[pozice + 1:]

        if sluvko.count(pismenko) > 1:
            pozice = sluvko.index(pismenko, pozice) * 2
            opratka.retezec = opratka.retezec[:pozice] + pismenko + opratka.retezec[pozice + 1:]
            #to ale opraví jen dvě místa, nedokážu tam dostat cyklus, aby to udělalo na víc místech

    else:
        print("Ne, to tam není.")
        opratka.pocet_chyb += 1
        opratka.sibenice()

    print(opratka.retezec)

def hra():

    while "_" in opratka.retezec:

        while True:
            pismenko = input("Jaké zkusíš písmeno? ")
            if over_delku(pismenko) == True and over_pismeno(pismenko) == True:
                break
            else:
                print("Chci po tobě jedno písmeno")


        hledani(zvolene_slovo, pismenko)

        if opratka.pocet_chyb == 10:
            print("Sorry, už visíš. Zkus to znovu.")
            break

    if "_" not in opratka.retezec:
        print("Gratulace, vyhrálas!")
