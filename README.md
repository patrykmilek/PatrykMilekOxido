
# Projekt rekrutacyjny: Junior AI Developer - Oxido

## Opis

To repozytorium zawiera rozwiązanie zadania rekrutacyjnego na stanowisko Junior AI Developer w firmie Oxido. Projekt jest prostą aplikacją w Pythonie, która korzysta z API OpenAI do generowania artykułu HTML opartego na dostarczonym tekście. Aplikacja umożliwia przetworzenie treści artykułu, dodanie miejsc na grafiki oraz wygenerowanie pełnego podglądu HTML.

## Zawartość Repozytorium

- **plik_tekstowy.txt**: Plik tekstowy zawierający treść artykułu do przetworzenia.
- **rekrutacja.py**: Główny skrypt odpowiedzialny za odczyt artykułu, przetwarzanie go przez OpenAI i generowanie pliku `artykul.html`.
- **artykul.html**: Wygenerowany plik HTML zawierający przetworzoną treść artykułu.
- **szablon.html**: Szablon HTML do podglądu artykułu z prostym stylem CSS.
- **podglad.html**: Pełny podgląd artykułu wygenerowany na podstawie szablonu i treści artykułu.

## Wymagania

- Python 3.8 lub nowszy

## Konfiguracja środowiska

Przed rozpoczęciem pracy z projektem zaleca się utworzenie wirtualnego środowiska w Pythonie, aby odizolować zależności projektu.

1. **Sklonuj repozytorium**:

   ```bash
   git clone https://github.com/TwojeRepozytorium/projekt-oxido.git
   cd projekt-oxido
   ```

2. **Utwórz wirtualne środowisko**:

   W systemie Linux/MacOS:

   ```bash
   python3 -m venv venv
   ```

   W systemie Windows:

   ```bash
   python -m venv venv
   ```

3. **Aktywuj wirtualne środowisko**:

   - **Linux/MacOS**:
     ```bash
     source venv/bin/activate
     ```

   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Zainstaluj wymagane pakiety**:

   Upewnij się, że masz zainstalowany moduł `openai`. Możesz go zainstalować z pliku `requirements.txt` lub bezpośrednio:

   ```bash
   pip install openai
   ```

## Uruchomienie projektu

Po skonfigurowaniu środowiska możesz uruchomić główny skrypt `rekrutacja.py`, aby wygenerować plik `artykul.html`.

```bash
python rekrutacja.py
```
Po uruchomieniu głównego skryptu uruchom `podglad.py`, aby wygenerować podgląd pliku.

```bash
python podglad.py
```

## Plik artykul.html

Wygenerowany plik `artykul.html` jest uproszczonym HTML zawierającym jedynie treść do osadzenia w `<body>` strony, zgodnie z wymaganiami zadania. Aby zobaczyć wizualizację, otwórz plik `podglad.html`, który zawiera pełny podgląd artykułu na podstawie szablonu.

## Autor

Zadanie wykonane jako część procesu rekrutacyjnego do firmy Oxido.
