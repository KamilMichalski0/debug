# Plik: bug_hunt.py
#
# Cel: Obliczyć sumę i średnią arytmetyczną dla listy liczb.
# Ten plik zawiera celowe błędy do celów szkoleniowych.

def oblicz_statystyki(lista_liczb):
  suma = sum(lista_liczb)

  srednia = suma / len(lista_liczb)

  return suma, srednia

dane = [10, 20, 30, 40, 50, 60]
suma_wynik, srednia_wynik = oblicz_statystyki(dane)

print(f"Dane wejściowe: {dane}")
print(f"Suma: {suma_wynik}")
print(f"Średnia: {srednia_wynik}")

# Oczekiwana suma: 210
# Oczekiwana średnia: 35.0

