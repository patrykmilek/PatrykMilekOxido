import openai
import re

openai.api_key = 'SET_YOUR_KEY'

def generate_image_url(description):
    """
    Funkcja generuje URL do obrazu za pomocą API DALL-E.
    """
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def generate_html_from_text(article_text, prompt):
    """
    Funkcja wysyła tekst artykułu i prompt do API OpenAI, aby wygenerować przetworzony HTML.
    """
    full_prompt = f"{prompt}\n\nArtykuł:\n{article_text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=1500,
        temperature=0.5
    )

    html_output = response.choices[0].message['content'].strip()
    return html_output

def replace_image_placeholders_with_generated_links(html_content):
    """
    Funkcja zastępuje wszystkie wystąpienia <img src='image_placeholder.jpg'> linkami do obrazów
    wygenerowanymi przez DALL-E.
    """
    def replace_match(match):
        alt_text = match.group(1)
        image_url = generate_image_url(alt_text)
        return f"<img src='{image_url}' alt='{alt_text}'>"

    updated_html = re.sub(r"<img src='image_placeholder.jpg' alt='(.*?)'>", replace_match, html_content)
    return updated_html

with open("plik_tekstowy.txt", "r", encoding="utf-8") as file:
    article_text = file.read()

prompt = (
    "Przekształć poniższy artykuł na sformatowany HTML, używając odpowiednich tagów HTML "
    "do organizacji treści, takich jak <h1> dla tytułu, <h2> dla nagłówków sekcji, oraz <p> dla akapitów. "
    "Dodaj grafiki tam, gdzie uważasz to za stosowne, umieszczając tagi <img> z atrybutem "
    "src='image_placeholder.jpg'. W atrybucie alt dodaj szczegółowy opis grafiki, który można użyć "
    "jako prompt do jej wygenerowania. Dodaj także podpis pod każdym obrazkiem, korzystając z tagu <figcaption>, "
    "aby opisać jego zawartość w kontekście artykułu. "
    "Wygeneruj tylko kod HTML dla zawartości do umieszczenia wewnątrz tagów <body>. "
    "Nie dołączaj sekcji <html>, <head> ani innych zewnętrznych elementów."
)

html_content = generate_html_from_text(article_text, prompt)

html_content_with_images = replace_image_placeholders_with_generated_links(html_content)


with open("artykul.html", "w", encoding="utf-8") as file:
    file.write(html_content_with_images)

print("Wygenerowany HTML został zapisany w pliku 'artykul.html'")
