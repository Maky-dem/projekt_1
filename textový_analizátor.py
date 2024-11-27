"""
    projekt_1.py: první projekt do Engento Online Python Akademie
    autor: Markéta Fejtek
    email: demura.m@seznam.cz
"""
registrovane_uzivatele = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123",
    "liz": "pass123"}
odelovac = "_ " * 30
prihlasovaci_jmeno = input(str("username:"))
heslo = input(str("password:")) 
print(odelovac)
if prihlasovaci_jmeno in registrovane_uzivatele and\
    registrovane_uzivatele[prihlasovaci_jmeno] == heslo:
    print("Welcome to the app, ", prihlasovaci_jmeno)
else:
    print("Unregistered user, terminating the programm")
    quit()
TEXTS: list[str] = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
print("We have", len(TEXTS), "texts to be analyzed.")
print(odelovac)
text_k_analyza = input(("Enter a number btw. 1 and "+\
         str(len(TEXTS))+ ":"))
if text_k_analyza.isdigit() and int(text_k_analyza)\
     in range(1, len(TEXTS) + 1):
    print("Analysis in progress, text number :", text_k_analyza)
else:
    print("You have entered a number that we do not have in our offer,\
         terminating the programm")
    quit()
text_analizuji = TEXTS[int(text_k_analyza)-1]
slova_textu = text_analizuji.split()# rozdeleni textu na slova
print(odelovac) # rozdeleni textu na slova
print("There are", len(slova_textu), "words in the selected text.")
pocet_slov_zvp = sum( 1 for slovo in slova_textu if slovo.istitle() \
    and slovo.isalpha()) # počet slov z velkych písmen
print("There are", pocet_slov_zvp, "titlecase words.")
pocet_slov_vp = sum( 1 for slovo in slova_textu if slovo.isupper() \
    and slovo.isalpha()) # počet slov psaných velkými písmeny
print("There are", pocet_slov_vp,"uppercase words.")
pocet_slov_vp_mal = sum( 1 for slovo in slova_textu if slovo.islower() \
    and slovo.isalpha()) # počet slov psaných malými písmeny
print("There are", pocet_slov_vp_mal, "lowercase words.")
pocet_cisel = sum(1 for slovo in slova_textu if slovo.isdigit()) 
# počet čísel v textu
print("There are", pocet_cisel, "numeric strings.")
suma_vsech_cisel_v_textu = sum(int(slovo) for slovo in slova_textu\
     if slovo.isdigit()) # součet všech čísel v textu
print("The sum of all numbers", suma_vsech_cisel_v_textu)
import collections
def analizuj_delky_slov(slova_textu):
    delky_slov = []
    for slovo in text_analizuji.split():
        delky_slov.append(len(slovo))
    pocet_slov_dle_delky = collections.Counter(delky_slov)
    return delky_slov, pocet_slov_dle_delky
delky_slov, pocet_slov_dle_delky = analizuj_delky_slov(text_analizuji) 
odstup_tabulka = int(max(pocet_slov_dle_delky.values())) + 1  
print(odelovac) 
print("LEN| OCCURENCES", "|NR.", sep=" "*(odstup_tabulka-11))  
print(odelovac)
for length, occurrences in sorted(pocet_slov_dle_delky.items()):
    print(f"{length:3}| {'*' * occurrences:<{odstup_tabulka-1}}|{
        occurrences}".ljust(odstup_tabulka+3))

    


