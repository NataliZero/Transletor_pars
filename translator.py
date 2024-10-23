from googletrans import Translator  # Импортируем модуль для перевода
import requests  # Импортируем модуль для отправки HTTP-запросов
from bs4 import BeautifulSoup  # Импортируем BeautifulSoup для парсинга HTML

# Создаём объект для перевода
translator = Translator()

# Получаем случайное слово с сайта randomword.com
url_word = "https://randomword.com/"
response_word = requests.get(url_word)  # Отправляем запрос на сайт
soup_word = BeautifulSoup(response_word.text, "html.parser")  # Разбираем HTML-код страницы

# Извлекаем слово и его определение
word = soup_word.find("div", id="random_word").text  # Ищем тег div с id "random_word"
definition = soup_word.find("div", id="random_word_definition").text  # Ищем тег div с id "random_word_definition"

# Переводим слово и его определение на русский язык
translated_word = translator.translate(word, src='en', dest='ru').text  # Переводим слово на русский
translated_definition = translator.translate(definition, src='en', dest='ru').text  # Переводим определение

# Выводим результат
print(f"Слово: {translated_word}")
print(f"Определение: {translated_definition}")
