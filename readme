# Rozwój systemu hydroponicznego w Django

Zadanie rekrutacyjne :)

## Wymagania


* Najnowsza wersja [Dockera](https://www.docker.com/get-started) i [Docker Compose](https://docs.docker.com/compose/install/).

## Instalacja Projektu

```
https://github.com/JakubPaszke/luna.git
cd luna
```

## Uruchomienie dockera

Jak w większości przypadków, uruchamiamy 
```
docker-compose build 
docker-compose up
```

Nie ma potrzeby migrowania danych, bo docker-compose robi to za nas (a baza danych nie rozwala się, dzięki plikowi wait-for-it.sh).

## Używanie Swaggera

Dla łatwiejszego testowania API, zainstalowałem Swaggera.
Wszelkie funkcje do testowania można znaleźć pod linkiem:
[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

Można przetestować wszelkie funkcjonalności. Funkcję register i login są niezbędne, żeby móc testować aplikację. Przycisk Authorize w prawym górnym rogu (i dostęp do wszystkich funkcji) działa na tokenie, uzyskanym z funkcji 'login'.

Najłatwiej testować wymagnia na:
- Sensory i Systemy -> CRUD /sensors/ i CRUD /hydroponics/
- Użytkownik powinien mieć możliwość otrzymania listy swoich
systemów hydroponicznych. -> GET /hydroponics
- Wszelkie metody pobierania danych powinny dawać możliwość
filtrowania danych (przedział czasowy, przedział wartości). -> GET /hydroponics, GET /sensors
- Metody te powinny też dawać opcje sortowania wyników po wybranych
parametrach. -> GET /hydroponics, GET /sensors
- W metodach, gdzie będzie to potrzebne należy zaimplementować
paginację danych. -> GET /hydroponics, GET /sensors
- Możliwość pobrania szczegółów konkretnego systemu z informacją o
10 ostatnich pomiarach. -> GET /hydroponics/<id>


## Uruchomienie testów

Użyłem biblioteki coverage. Można ją łatwo triggerować za pomocą:

```
coverage run --source='.' manage.py test
```

A następnie zobaczyć raport:
```
coverage raport
```