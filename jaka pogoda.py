import requests

# stałe
K_TO_C = 273.15

# przywitanie w aplikacji
print("Witaj w Personalnej Pogodynce. Możesz tutaj sprawdzić aktualną pogodę.")

# dla jakiego miasta będzie sprawdzana pogoda
lokalizacja = input("Podaj nazwę miasta, w którym chcesz sprawdzić pogodę: ")

# link do pogody
# link_dzisiaj = "https://api.openweathermap.org/data/2.5/weather?q={lokalizacja}&appid=9bf42cfd7b0efdc08e1d18087d83f5fe&lang=pl"
url_baza = "https://api.openweathermap.org/data/2.5/weather"
dane_do_linków = {"q": lokalizacja, "appid": "9bf42cfd7b0efdc08e1d18087d83f5fe", "lang": "pl"}

# fuknkcje drukujące pożądane info
def teraz():
    temp = float(pogoda_dzisiaj["main"]["temp_max"]) - K_TO_C
    print("W tym momencie w miejscowości", lokalizacja, "panuje temperatura:", int(temp), "stopni.")
    temp_odczuwalna = float(pogoda_dzisiaj["main"]["feels_like"]) - K_TO_C
    print("Temperatura odczuwalna wynosi", int(temp_odczuwalna), "stopni.")
    warunki = pogoda_dzisiaj["weather"][0]["description"]
    print("Na dworze jest", warunki + ".")
    ciśnienie = pogoda_dzisiaj["main"]["pressure"]
    print("Ciśnienie wynosi", ciśnienie, "hPa.")
    wilgotność = pogoda_dzisiaj["main"]["humidity"]
    print("Wilgotność jest na poziomie", wilgotność, "%")
    wiatr = pogoda_dzisiaj["wind"]["speed"]
    print("Wiatr ma prędkość", wiatr, "m/s.")


def jutro():
    pass


def tydzien():
    pass


# składamy link do kupy, pobieramy dane
pogoda_dzisiaj = requests.get(url_baza, params=dane_do_linków).json()

# prezentujemy dane   
teraz()