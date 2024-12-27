from countryinfo import CountryInfo

try:
    country = input("Entrer le nom d'un pays (En englais) : ")
    country_name = CountryInfo(country.upper())
    print(" ")
    print("PAYS : ", country.upper())
    print("Capital : ", country_name.capital())
    print("Langues : ", country_name.languages())
    print("Curr - Monney : ", country_name.currencies())
    print("Pays frontaliers : ", country_name.borders())
    print("Autres Surnoms : ", country_name.alt_spellings())
    print(" ")
except:
    print("\nNom du pays introuvable ! verifiez l'orthographe ou essayer un autre pays.")
finally:
    print("Programme terminé.")