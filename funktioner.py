# Funktioner - skriv kod en gång, använd många gånger!

# def = define = "skapa en funktion"

def halsa(namn):
    print("Hej", namn, "!")

# Anropa funktionen

halsa("Farre")
halsa("Anna")
halsa("Erik")

print("---")

# Funktion med flera parameter
def addera(x, y):
    resultat = x + y
    print(x, "+", y, "=", resultat)

addera(5, 3)
addera(10, 20)
addera(100, 200)

print("---")

# Funktion som returerar ett värde

def multiplicera(x, y):
    return x * y

svar = multiplicera(5, 4)
print("5 x 4 =", svar)

# Praktiskt exempel - BMI-kalkylator

def berakna_bmi(vikt, langd):
    bmi = vikt / (langd ** 2)
    bmi = round(bmi, 1)  # Avrunda till 1 docimal

    if bmi < 18.5:
        kategori = "undervikt"
    elif bmi < 25:
        kategori = "Normalvikt"
    elif bmi < 30:
        kategori = "Övervikt"
    else:
        kategori = "Fetma"

    print("BMI:", bmi, "→", kategori)

# Testa funktionen

berakna_bmi(70, 1.75)   
berakna_bmi(90, 1.80)
berakna_bmi(55, 1.70)

