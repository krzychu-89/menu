# menu

Instrukcja:

1) instalacja paczek:
pip install -r requirements.txt

2) zainstalować redisa zgodnie z dokumentacją: 
https://redis.io/download

3) ustawić baze danych w settings.py
ustawić adres i port redisa w settingsach

4) wygenerowanie danych:
python manage.py migrate
python manage.py generate_data
python manage.py createsuperuser i stworzyć użytkownika z dostępem do panelu admina

5) można uruchomić runserwerem, 
Panel Admina dostepny pod standardową ściężką .../admin


6) Jak widać warstwa wizualna nie jest moją mocną stroną.

Szczerze mówiąc nie do konca zrozumiałem, że strony mają przechodzić asynchronicznie.
Póki co są robione asynchroniczne zapytania ajaxowe, które pobierają dane, z tym że tak na prawde jest to 1 strona, 
która przeładowuje dane. Pewnie należało by jeszcze dodać jakieś blokowanie ekranu do czau aż nie przyjdzie odpowiedź z ajaxa i nie załaduje wyników lub coś innego co byśmy oczekiwali. Teoretycznie można by te zapytania wrzucić do asynchronicznych tasków celery, ale 
chyba trochę by się to mijało z celem w takim przypadku. Wyniki z restapi są cachowane Redisem.
