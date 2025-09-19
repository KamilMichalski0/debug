# Plik: word_finder.py
#
# Cel: Znaleźć najdłuższe słowo w podanym zdaniu.
# Ten plik zawiera celowe błędy do zadania domowego.

def znajdz_najdluzsze_slowo(zdanie)
  slowa = zdanie.split(" ")
  najdluzsze = ""
  for s in slowa:
    if len(s) >= len(najdluzsze):
      najdluzsze = s
  return najdluzsze

zdanie_testowe = "Claude to mój niezawodny asystent AI"
wynik = znajdz_najdluzsze_slowo(zdanie_testowe)
print(f"Zdanie: '{zdanie_testowe}'")
print(f"Znalezione słowo: '{wynik}'")

# Oczekiwany wynik: 'niezawodny' (słowo o długości 9)
# Aktualny (błędny) wynik: 'asystent' (również 9 liter, ale znaleziony później)
