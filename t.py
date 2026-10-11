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

print(dni_robocze.get("Satu"))  # jak nie ma klucza w slowniku to po cichu zwroci blad ale kod dalej bedie wykonwywany 
print(dni_robocze["Satu"]) # to wywali blad i nie pojdzie dalej bedzie krzyczal blad  - inwariant - cos co musi byc bo potem nie bedzi dialac kod



