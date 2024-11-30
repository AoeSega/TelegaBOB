![image](https://github.com/user-attachments/assets/01d0aeff-a8bd-4b87-bd1c-1a44386a4a3c)

# Telegram Бот: Управление инвестициями  

Данный проект представляет Telegram-бота, который помогает пользователям управлять инвестициями. Бот позволяет выбирать инвестиционные стратегии, просматривать Dashboard и оставлять отзывы.  

---

## 📋 Возможности  

### 🔑 Основные функции  
- **Выбор стратегии инвестирования**:  
  Пользователь может указать бюджет и получить подходящие инвестиционные предложения.  

- **Просмотр Dashboard**:  
  Доступ к аналитической информации через специальную ссылку.  

- **Сбор отзывов**:  
  Пользователь может оставить отзыв после выбора стратегии.  

### 💡 Доступные команды  
| Команда     | Описание                                                    |  
|-------------|-------------------------------------------------------------|  
| `/start`    | Запускает бота или возвращает пользователя в главное меню.  |  
| `/help`     | Выводит список всех доступных команд с их описанием.        |  
| `/cancel`   | Отменяет текущий диалог и возвращает в главное меню.        |  
| `/dash`     | Отправляет ссылку на Dashboard.                             |  
| `/back`     | Возвращает пользователя к предыдущему пункту меню.          |  

---

## 🛠️ Установка и настройка  

### 🔹 Шаг 1: Установите Python  
Убедитесь, что на вашем устройстве установлен Python версии **3.8** или выше.  
Скачать Python можно с [официального сайта](https://www.python.org/downloads/).  

### 🔹 Шаг 2: Установите зависимости  
1. Склонируйте репозиторий:  
   ```bash
   git clone https://github.com/imposter/investment-bot.git
   cd investment-bot
   ```  
2. Установите необходимые библиотеки:  
   ```bash
   pip install aiogram
   ```  

### 🔹 Шаг 3: Создайте Telegram-бота  
1. Найдите [BotFather](https://t.me/botfather) в Telegram.  
2. Введите команду `/newbot` для создания нового бота.  
3. Укажите имя и username для бота.  
4. Скопируйте токен API, предоставленный BotFather.  

### 🔹 Шаг 4: Настройте токен  
Откройте файл `bot.py` и замените строку:  
```python
API_TOKEN = 'ВАШ_ТОКЕН'
```  
Вставьте ваш токен вместо `ВАШ_ТОКЕН`.  

### 🔹 Шаг 5: Запустите бота  
Выполните следующую команду:  
```bash
python bot.py
```  

После запуска бот готов к использованию в Telegram.  

---

## 🗂️ Структура меню  

### Главное меню  
- **"Хочу получить стратегию"**  
- **"Посмотреть Dashboard"**  

### Подменю выбора бюджета  
- 50-100$  
- 100-500$  
- 500$ и более  

### Опции стратегий  
Пользователь выбирает из предложенных вариантов стратегий, после чего бот подтверждает создание стратегии и предлагает оставить отзыв.  

---

## ⚠️ Примечания  

- **Изменение ссылки на Dashboard**:  
  В файле `bot.py` замените строку:  
  ```python
  "Ссылка на Dashboard: ССЫЛКА ДАШ"
  ```  
  на актуальную ссылку.  

- **Обработка ошибок**:  
  - Если бот не отвечает, проверьте правильность токена и активность скрипта.  
  - Убедитесь, что все зависимости установлены:  
    ```bash
    pip install aiogram
    ```  
  - Убедитесь, что бот добавлен в ваш контактный список Telegram.  
