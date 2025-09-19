# Zadanie Domowe: Debugging w Pythonie

## Cel zadania:
Samodzielne przećwiczenie procesu znajdowania i naprawiania błędu składni oraz błędu logicznego.

## Instrukcja Krok po Kroku:

### Pobierz akta sprawy:
Użyj skryptu `word_finder.py` z repozytorium. Jego celem jest znalezienie najdłuższego słowa w zdaniu.

### Śledztwo #1 (Błąd Składni):

Spróbuj uruchomić skrypt. Zobaczysz, że Python zgłosi błąd SyntaxError.

Poproś Claude'a o pomoc, np.: "Dostaję błąd SyntaxError w tym kodzie, pomóż mi go znaleźć". Zastosuj poprawkę.

### Śledztwo #2 (Błąd Logiczny):

Gdy kod już się uruchamia, zauważysz, że dla zdania testowego `Claude to mój niezawodny asystent AI` wynik jest poprawny.

Twoim zadaniem jest znaleźć przypadek, w którym kod się myli! Zmień wartość zmiennej `zdanie_testowe` na: `"Jeden prosty test kodu"`.

Uruchom skrypt ponownie. Zobaczysz, że wynikiem jest "prosty", chociaż "Jeden" jest tak samo długie.

Poproś Claude'a o znalezienie błędu w rozumowaniu, np.: "Ta funkcja powinna znaleźć pierwsze najdłuższe słowo, ale znajduje ostatnie. Gdzie jest błąd logiczny?". Zastosuj sugerowaną przez niego poprawkę.

## Oczekiwany Rezultat:
W pełni działający skrypt, który dla zdania "Jeden prosty test kodu" poprawnie identyfikuje i wyświetla słowo "Jeden" jako pierwsze najdłuższe.

## Dlaczego to ćwiczenie jest ważne?
Uczy Cię nie tylko naprawiania błędów, które widzisz, ale także testowania swojego kodu i znajdowania ukrytych problemów. To kluczowy krok w stronę pisania naprawdę solidnych programów! Powodzenia! 💪