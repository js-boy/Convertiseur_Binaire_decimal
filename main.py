def binaire_decimal(binaire):
    decimal = 0 
    binaire_inverse = str(binaire)[::-1]
    
    for i in range(len(binaire_inverse)):
        if binaire_inverse[i] == '1':
            decimal += 2**i
    return decimal 

def demander_nombre_valide():
    while True:
        binaire = input("Tapez un nombre binaire (max 8 chiffres, 0 et 1 uniquement) : ").strip()
        
        if len(binaire) > 8:
            print("❌ Erreur : La séquence doit comporter 8 chiffres maximum.")
            continue 
            
        est_valide = all(c in '01' for c in binaire)
        
        if not est_valide:
            print("❌ Erreur : Votre chaîne contient des caractères autres que 0 et 1.")
            continue
            
        return binaire

saisie = demander_nombre_valide()
resultat = binaire_decimal(saisie)

print("-" * 30)
print(f"✅ Le binaire {saisie} vaut {resultat} en décimal.")


