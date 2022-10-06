#potrzebne rzeczy
import requests
import json

#link do pogody
link_dzisiaj = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=9bf42cfd7b0efdc08e1d18087d83f5fe"

#zdefiniowanie funkcji, która przedstawi informacje, o które może zapytać użytkownik
#pogoda na dziś, na jutro i na tydzień

#pogoda na dzisiaj
def dzisiaj():
    
    pass

def jutro():
    #pogoda na jutro
    pass

def tydzien():
    #pogoda na najbliższe 2 tygodnie
    pass

#przywitanie w aplikacji
print("Witaj w Personalnej Pogodynce. Możesz tutaj sprawdzić aktualną pogodę i prognozę na najbliższe dni.")

while True:
    #dla jakiego miasta będzie sprawdzana pogoda
    lokalizacja = input("Podaj nazwę miasta, w którym chcesz sprawdzić pogodę: ")
    x = link_dzisiaj.format(lokalizacja)
    r = requests.get(x)
    pogoda_dzisiaj = r.json()
    
    print(pogoda_dzisiaj)
#wywołanie funkcji dotyczącej poszukiwanego info

#input użytkownika + czy zamknąć program
    czy_wyjść = input("Czy zakończyć działanie programu? t/n ")
    if czy_wyjść == "t": break

