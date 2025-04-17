# 1. Базовий образ з Python
FROM python:3.12

# 2. Робоча директорія всередині контейнера
WORKDIR /tests

# 3. Копіюємо requirements.txt всередину контейнера
COPY requirements.txt .

# 4. Встановлюємо всі бібліотеки з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копіюємо папку з тестами в контейнер
COPY tests/ /tests

# 6. За замовчуванням запускаємо bash (можна передати команду через docker-compose)
ENTRYPOINT ["python"]
CMD ["lab_6.py"]
