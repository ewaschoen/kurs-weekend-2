dni_robocze = {
    "Mon": "poniedzialek",
    "Tue": "wtorek",
    "Wed": "sroda",
    "Thu": "czwartek",
    "Fri": "piatek",
}

weekendy = {
    "Sat": "sobota",
    "Sun": "niedziela"
    }

nazwy_dni = {
    **weekendy,
}

# print(nazwy_dni[input("Podaj skrtowiec: ")])


print(dni_robocze)
print(weekendy)
print(nazwy_dni)

print(dni_robocze.get("Satu"))  # jak nie ma klucza w slowniku to
print(dni_robocze["Satu"])


