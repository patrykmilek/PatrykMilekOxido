# Projekt rekrutacyjny: Junior AI Developer - Oxido

## Opis

To repozytorium zawiera rozwiązanie zadania rekrutacyjnego na stanowisko Junior AI Developer w firmie Oxido. Projekt jest prostą aplikacją w Pythonie, która korzysta z API OpenAI do generowania artykułu HTML opartego na dostarczonym tekście. Aplikacja umożliwia przetworzenie treści artykułu, dodanie miejsc na grafiki oraz wygenerowanie pełnego podglądu HTML.

## Zawartość Repozytorium

- **plik_tekstowy.txt**: Plik tekstowy zawierający treść artykułu do przetworzenia.
- **rekrutacja.py**: Główny skrypt odpowiedzialny za odczyt artykułu, przetwarzanie go przez OpenAI i generowanie pliku `artykul.html`.
- **artykul.html**: Wygenerowany plik HTML zawierający przetworzoną treść artykułu.
- **szablon.html**: Szablon HTML do podglądu artykułu z prostym stylem CSS.
- **podglad.html**: Pełny podgląd artykułu wygenerowany na podstawie szablonu i treści artykułu.
- **test.py**: Skrypt testowy do generowania linków do obrazów przy użyciu API OpenAI.

## Wymagania

- Python 3.8 lub nowszy
- Konto OpenAI oraz klucz API do wykorzystania modelu GPT

## Konfiguracja środowiska

Przed rozpoczęciem pracy z projektem zaleca się utworzenie wirtualnego środowiska w Pythonie, aby odizolować zależności projektu.

1. **Sklonuj repozytorium**:

   ```bash
   git clone https://github.com/TwojeRepozytorium/projekt-oxido.git
   cd projekt-oxido
