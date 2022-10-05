#potrzebne rzeczy
import requests

#link do pogody
link = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=9bf42cfd7b0efdc08e1d18087d83f5fe"

#zdefiniowanie funkcji, która przedstawi informacje, o które może zapytać użytkownik
#pogoda na dziś, pogoda na najbliższy tydzień, XD (to lepiej ograniczyć, bo umre)

#ogarnięcie dostępu do danych pogodowych (czy w tym miejscu? wyjdzie w praniu)

#przywitanie w aplikacji
print("Witaj w Personalnej Pogodynce. Możesz tutaj sprawdzić aktualną pogodę i prognozę na najbliższe dni.")

while True:
    #dla jakiego miasta będzie sprawdzana pogoda
    lokalizacja = input("Podaj nazwę miasta, w którym chcesz sprawdzić pogodę: ")
    x = link.format(lokalizacja)
 
#wywołanie funkcji dotyczącej poszukiwanego info

#input użytkownika + czy zamknąć program
    czy_wyjść = input("Czy zakończyć działanie programu? t/n ")
    if czy_wyjść == "t": break