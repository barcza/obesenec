from random import choice

retezec = "_ _ _ _ _"

pocet_chyb = 0

def zvol_slovo():
    slovo = ["balon", "zubař", "opice", "dveře", "kočka", "parno", "želva", "ratan"]
    return choice(slovo)

def sibenice():
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
