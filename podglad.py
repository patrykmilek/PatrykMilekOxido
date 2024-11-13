# Wczytanie zawartości plików szablonu i artykułu
with open("szablon.html", "r", encoding="utf-8") as template_file:
    template_content = template_file.read()

with open("artykul.html", "r", encoding="utf-8") as article_file:
    article_content = article_file.read()

# Wstawienie treści artykułu do miejsca oznaczonego w szablonie
full_content = template_content.replace("<!-- Wklej zawartość pliku artykul.html tutaj -->", article_content)

# Zapisanie wynikowego pliku podglądu
with open("podglad.html", "w", encoding="utf-8") as preview_file:
    preview_file.write(full_content)

print("Plik 'podglad.html' został utworzony jako pełny podgląd artykułu.")
