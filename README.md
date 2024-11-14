
# Projekt rekrutacyjny: Junior AI Developer - Oxido

## Opis

To repozytorium zawiera rozwiązanie zadania rekrutacyjnego na stanowisko Junior AI Developer w firmie Oxido. Projekt jest prostą aplikacją w Pythonie, która korzysta z API OpenAI do generowania artykułu HTML opartego na dostarczonym tekście. Aplikacja umożliwia przetworzenie treści artykułu, dodanie miejsc na grafiki oraz wygenerowanie pełnego podglądu HTML.

## Zawartość Repozytorium

- **plik_tekstowy.txt**: Plik tekstowy zawierający treść artykułu do przetworzenia.
- **rekrutacja.py**: Główny skrypt odpowiedzialny za odczyt artykułu, przetwarzanie go przez OpenAI i generowanie pliku `artykul.html`.
- **artykul.html**: Wygenerowany plik HTML zawierający przetworzoną treść artykułu.
- **szablon.html**: Szablon HTML do podglądu artykułu z prostym stylem CSS.
- **podglad.html**: Pełny podgląd artykułu wygenerowany na podstawie szablonu i treści artykułu.

# Dla systemu Windows:

### Krok 1: Uruchom Visual Studio Code
Otwórz Visual Studio Code, aby rozpocząć konfigurację.

### Krok 2: Zainstaluj WSL
W terminalu Visual Studio Code wpisz:
```bash
wsl --install
```
Po zakończeniu instalacji system może poprosić o ponowne uruchomienie. Po restarcie uruchom ponownie terminal w Visual Studio Code i wpisz `wsl`, aby wejść do powłoki WSL.

### Krok 3: Skonfiguruj WSL
Przy pierwszym uruchomieniu WSL zostaniesz poproszony o utworzenie nazwy użytkownika oraz hasła dla środowiska Ubuntu.

### Krok 4: Zaktualizuj listę pakietów i zainstaluj Pythona oraz pip
W terminalu WSL wpisz:
```bash
sudo apt update
sudo apt install python3 python3-venv -y
sudo apt install python3-pip -y
```

### Krok 5: Przejdź do katalogu projektu
Zakładamy, że projekt znajduje się w folderze **Pobrane**. Przejdź do niego, wpisując:
```bash
cd /mnt/c/Users/TwojaNazwaUżytkownika/Downloads/projekt-oxido
```
> Uwaga: Upewnij się, że ścieżka odpowiada rzeczywistej lokalizacji pobranego projektu.

### Krok 6: Utwórz wirtualne środowisko
Utwórz wirtualne środowisko Python, wpisując:
```bash
python3 -m venv venv
```

### Krok 7: Aktywuj wirtualne środowisko
Aby aktywować wirtualne środowisko, wpisz:
```bash
source venv/bin/activate
```
Po aktywacji `(venv)` powinno pojawić się na początku wiersza poleceń, co oznacza, że środowisko jest aktywne.

### Krok 8: Zainstaluj bibliotekę `openai`
Zainstaluj bibliotekę `openai` w odpowiedniej wersji:
```bash
pip install openai==0.28.0
```

### Krok 9: Zmień klucz API OpenAI

- Modyfikacja skryptu, aby wpisać klucz API bezpośrednio w kodzie w miejscu, gdzie jest wywoływana zmienna `openai.api_key` w miejscu 'SET_YOUR_KEY'.

### Krok 10: Uruchom program
W terminalu wpisz:
```bash
python3 rekrutacja.py
python3 podglad.py
```
Po wykonaniu tej komendy program powinien się uruchomić i wygenerować pliki `artykul.html` oraz `podglad.html`.

# Dla systemu Linux:

### Krok 1: Pobierz repozytorium projektu
Otwórz terminal i sklonuj repozytorium projektu z GitHub:
```bash
git clone https://github.com/TwojeRepozytorium/projekt-oxido.git
cd projekt-oxido
```

### Krok 2: Zaktualizuj listę pakietów i zainstaluj Pythona oraz pip
W terminalu wpisz:
```bash
sudo apt update
sudo apt install python3 python3-venv -y
sudo apt install python3-pip -y
```
Upewnij się, że masz zainstalowaną odpowiednią wersję Pythona i pip.

### Krok 3: Utwórz wirtualne środowisko
W katalogu projektu utwórz wirtualne środowisko:
```bash
python3 -m venv venv
```

### Krok 4: Aktywuj wirtualne środowisko
Aktywuj środowisko w terminalu:
```bash
source venv/bin/activate
```
Powinno pojawić się `(venv)` na początku wiersza poleceń, co oznacza, że środowisko jest aktywne.

### Krok 5: Zainstaluj bibliotekę `openai` w wersji 0.28.0
Wpisz poniższą komendę, aby zainstalować `openai` w wymaganej wersji:
```bash
pip install openai==0.28.0
```

### Krok 6: Zmień klucz API OpenAI

- Modyfikacja skryptu, aby wpisać klucz API bezpośrednio w kodzie w miejscu, gdzie jest wywoływana zmienna `openai.api_key` w miejscu 'SET_YOUR_KEY'.

### Krok 7: Uruchom program
W terminalu wpisz:
```bash
python3 rekrutacja.py
python3 podglad.py
```
Po wykonaniu tej komendy program powinien się uruchomić i wygenerować pliki `artykul.html` oraz `podglad.html`.
