import re

# re - biblioteka do działań z wyrażeniami regularnymi
# text = "Przykładowy tekst z adresem email: przykladowy@example.com"
text = "Przykładowy tekst z adresem email: rajkonkret660@gmail.com"

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
match = re.search(email_pattern, text)
if match:
    print("Znaleziono email:", match.group())  # Znaleziono email: przykladowy@example.com
# Znaleziono email: rajkonkret660@gmail.com

numbers_pattern = r'\d+'
numbers = re.findall(numbers_pattern, "Wtekście są liczby 123 i 456")
print(f"Numbers {numbers}")  # Numbers ['123', '456']
