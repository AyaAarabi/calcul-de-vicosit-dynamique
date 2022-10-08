v = input("entrez la viscosite :")
d = input("entrez la densite: ")
try :
    d = float(d)
    v = float(v)
    µ = v * 0.0001 * 1000 * d
    print("la viscosite dynamique :",µ,"PI")
except:
    print("la valeur de la densité et / ou viscosité que vous avez donné est pas correct ")