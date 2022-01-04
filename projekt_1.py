

# ověření hesel
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("Username: ")
password = input("Password: ")

if users.get(username) != password:
    print("Access denied. Wrong password or unregistered user.")
    print(exit)
    exit()
else:
    print("Welcome to the app, ", username)

# oddelovac
oddelovac = "- " * 40
print(oddelovac)

# texty k analýze
TEXTS = ['''
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

# počet textů k analýze
print("We have", len(list(TEXTS)), "text to be analyzed.")

print(oddelovac)

# volba textu
selected_text_number = int(input("Enter a number btw. 1 and 3 to select: "))

if 1 <= selected_text_number <= 3:
    selected_text = TEXTS[selected_text_number - 1]
    print(f"Selected number: {selected_text_number}")
else:
    print("Wrong number. Please select number btw. 1 and 3!")
    print(exit)
    exit()

print(oddelovac)

# navázání na select

text = TEXTS[selected_text_number - 1]

# počet slov

list_slov = []
for slovo in text.split():
    if len(slovo) >= 1:
        list_slov.append(slovo)

list_ocistenych_slov = []
for slovo in list_slov:
    ciste = slovo.strip(".,?")
    list_ocistenych_slov.append(ciste)


print("There are " + str(len(list_ocistenych_slov)) + " words in the selected text.")

# počet s velkým písmenem na začátku

slova_s_velkym_pismenem = []
for slovo in list_ocistenych_slov:
    if slovo.istitle():
        slova_s_velkym_pismenem.append(slovo)

print("There are " + str(len(slova_s_velkym_pismenem)) + " titlecase words.")

# počet slov s velkými písmeny
slova_cela_velka = []
for slovo in list_ocistenych_slov:
    if slovo.isupper():
        slova_cela_velka.append(slovo)

cista_slova_cela_velka = []
for slovo in slova_cela_velka:
    if slovo.isalpha():
        cista_slova_cela_velka.append(slovo)

print("There are " + str(len(cista_slova_cela_velka)) + " uppercase words.")

# počet slov s malými písmeny
slova_cela_mala = []
for slovo in list_ocistenych_slov:
    if slovo.islower():
        slova_cela_mala.append(slovo)

cista_slova_cela_mala = []
for slovo in slova_cela_mala:
    if slovo.isalpha():
        cista_slova_cela_mala.append(slovo)

print("There are " + str(len(cista_slova_cela_mala)) + " lowercase words.")

# počet čísel
cisla_v_textu = []
for cislo in list_ocistenych_slov:
    if cislo.isdigit():
        cisla_v_textu.append(cislo)

print("There are " + str(len(cisla_v_textu)) + " numeric strings.")

# suma čísel
ints = [int(item) for item in cisla_v_textu]
print("The sum of all the numbers: " + str(sum(ints)))

print(oddelovac)

# graf četností
pro_graf = []
for slovo in list_ocistenych_slov:
    delka_slova = (len(slovo))
    pro_graf.append(delka_slova)


counts = {}
for num in pro_graf:
    counts[str(num)] = counts.setdefault(str(num), 0) + 1


sorted_counts = {k: counts[k] for k in sorted(counts)}


# print(f"DÉLKA", sorted_counts.keys() , "ČETNOST", sorted_counts.values())
print("FREQUENCY TABLE")
print("Length " + " | " + " Occurences")
print(oddelovac)
for keys, values in sorted_counts.items():
    print(keys, "|",  values * "*", values)