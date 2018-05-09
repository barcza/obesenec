from random import choice


#úvodní nastavení: prázdný řetězec a žádné chyby
retezec = "_ _ _ _ _"

pocet_chyb = 0

def zvol_slovo():
    #seznam, ze kterého zvolíme slovo
    slovo = ["balon", "zubař", "opice", "parno", "želva", "dveře", "kočka", "ratan"]
    return choice(slovo)

def sibenice():
    #obrázky, které to vykreslí, když se bude navyšovat počet chyb
    if pocet_chyb == 1:
        print(
    """





    ~~~~~~~""")
    elif pocet_chyb == 2:
        print(
    """+
    |
    |
    |
    |
    |
    ~~~~~~~""")
    elif pocet_chyb == 3:
        print(
    """+---.
    |
    |
    |
    |
    |
    ~~~~~~~""")
    elif pocet_chyb == 4:
        print(
    """+---.
    |   |
    |
    |
    |
    |
    ~~~~~~~""")
    elif pocet_chyb == 5:
        print(
    """+---.
    |   |
    |   O
    |
    |
    |
    ~~~~~~~""")
    elif pocet_chyb == 6:
        print(
    """+---.
    |   |
    |   O
    |   |
    |
    |
    ~~~~~~~""")
    elif pocet_chyb == 7:
        print(
    """+---.
    |   |
    |   O
    | --|
    |
    |
    ~~~~~~~""")
    elif pocet_chyb == 8:
        print(
    """+---.
    |   |
    |   O
    | --|--
    |
    |
    ~~~~~~~""")
    elif pocet_chyb == 9:
        print(
    """+---.
    |   |
    |   O
    | --|--
    |  /
    |
    ~~~~~~~""")
    elif pocet_chyb == 10:
        print(
    """+---.
    |   |
    |   O
    | --|--
    |  / \
    |
    ~~~~~~~""")
