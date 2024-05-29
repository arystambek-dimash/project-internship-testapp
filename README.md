# Test project

## Getting Started

These instructions will help you get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Poetry (for managing dependencies)

### Installation

1. Clone the repository:

   ```sh
      https://github.com/arystambek-dimash/projectInternTest.git

## 1.Navigate to the project directory:

```bash
cd projectInternTest
```

## 2.Install project dependencies using Poetry:

```bash
poetry install
```

# Running the Application

## 1.Activate the virtual environment:

```bash
poetry shell
```

## 3.Start the FastAPI application:

```bash
uvicorn main:app --reload
```

The server will now be running at http://127.0.0.1:8000/. You can access it through your web browser or using tools like
curl.

# API Documentation
## Эндпоинты

### Студенты

#### Получить всех студентов

- **Эндпоинт:** `GET /students`
- **Описание:** Получает список всех студентов с пагинацией.
- **Параметры:**
    - `skip` (int, опционально): Количество записей для пропуска при пагинации.
    - `limit` (int, опционально): Максимальное количество записей для возврата.
- **Ответ:**
    - `200 OK` при успешном выполнении, возвращает список студентов.
    - `400 Bad Request` если возникла ошибка.

#### Создать нового студента

- **Эндпоинт:** `POST /students`
- **Описание:** Создает нового студента.
- **Тело запроса:**
    - `first_name` (str): Имя студента.
    - `last_name` (str): Фамилия студента.
    - `date_of_birth` (date): Дата рождения студента.
    - `date_of_join` (date): Дата присоединения студента.
    - `gender` (str): Пол студента.
- **Ответ:**
    - `201 Created` при успешном выполнении, возвращает созданного студента.
    - `400 Bad Request` если возникла ошибка.

#### Получить студента по ID

- **Эндпоинт:** `GET /students/{student_id}`
- **Описание:** Получает студента по его ID, включая его оценки.
- **Параметры:**
    - `student_id` (int): ID студента для получения.
- **Ответ:**
    - `200 OK` при успешном выполнении, возвращает студента с его оценками.
    - `404 Not Found` если студент не найден.
    - `500 Internal Server Error` если возникла ошибка.

#### Обновить студента по ID

- **Эндпоинт:** `PATCH /students/{student_id}`
- **Описание:** Обновляет информацию о студенте.
- **Параметры:**
    - `student_id` (int): ID студента для обновления.
- **Тело запроса:**
    - `first_name` (str): Имя студента.
    - `last_name` (str): Фамилия студента.
    - `date_of_birth` (date): Дата рождения студента.
    - `date_of_join` (date): Дата присоединения студента.
    - `gender` (str): Пол студента.
- **Ответ:**
    - `200 OK` при успешном выполнении, возвращает обновленного студента.
    - `404 Not Found` если студент не найден.
    - `400 Bad Request` если возникла ошибка.

#### Удалить студента по ID

- **Эндпоинт:** `DELETE /students/{student_id}`
- **Описание:** Удаляет студента по его ID.
- **Параметры:**
    - `student_id` (int): ID студента для удаления.
- **Ответ:**
    - `200 OK` при успешном выполнении, возвращает ID удаленного студента.
    - `404 Not Found` если студент не найден.
    - `500 Internal Server Error` если возникла ошибка.

### Оценки

#### Получить оценку по ID

- **Эндпоинт:** `GET /scores/{score_id}`
- **Описание:** Получает оценку по ее ID.
- **Параметры:**
    - `score_id` (int): ID оценки для получения.
- **Ответ:**
    - `200 OK` при успешном выполнении, возвращает оценку.
    - `404 Not Found` если оценка не найдена.
    - `500 Internal Server Error` если возникла ошибка.

#### Создать новую оценку

- **Эндпоинт:** `POST /scores`
- **Описание:** Создает новую оценку для студента.
- **Тело запроса:**
    - `score` (int): Значение оценки.
    - `subject` (str): Предмет оценки.
    - `student_id` (int): ID студента для ассоциации с оценкой.
- **Ответ:**
    - `201 Created` при успешном выполнении, возвращает созданную оценку.
    - `400 Bad Request` если возникла ошибка.

#### Обновить оценку по ID

- **Эндпоинт:** `PATCH /scores/{score_id}`
- **Описание:** Обновляет информацию об оценке.
- **Параметры:**
    - `score_id` (int): ID оценки для обновления.
- **Тело запроса:**
    - `score` (int): Значение оценки.
    - `subject` (str): Предмет оценки.
    - `student_id` (int): ID студента для ассоциации с оценкой.
- **Ответ:**
    - `200 OK` при успешном выполнении, возвращает обновленную оценку.
    - `404 Not Found` если оценка не найдена.
    - `400 Bad Request` если возникла ошибка.

#### Удалить оценку по ID

- **Эндпоинт:** `DELETE /scores/{score_id}`
- **Описание:** Удаляет оценку по ее ID.
- **Параметры:**
    - `score_id` (int): ID оценки для удаления.
- **Ответ:**
    - `200 OK` при успешном выполнении, возвращает ID удаленной оценки.
    - `404 Not Found` если оценка не найдена.
    - `500 Internal Server Error` если возникла ошибка.