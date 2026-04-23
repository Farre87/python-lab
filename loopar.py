
# For-loop - upprepa ett visst antal gånger

# range(5) = 0, 1, 2, 3, 4
for i in range(5):
    print("Varv nummer", i)

print("---")

# Loopa igenom en lista
frukter = ["äpple", "banan", "apelsin"]
for frukt in frukter:
    print("Frukt:", frukt)

print("---")

# While-loop - fortsätt till något stämmer

raknare = 0
while raknare < 5:
    print("Räknare:", raknare)
    raknare = raknare + 1

print("Klar!")    


# Loop + if tillsammans

print("---")

for i in range(10):
    if i % 2 == 0:
        print(i, "är ett jämnt tal")
    else:
        print(i, "är ett udda tal")