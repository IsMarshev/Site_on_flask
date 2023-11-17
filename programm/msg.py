from app import db
from app.model import User

def create_user():
    new_user = User(
        name='John Doe',
        username='john_doe',
        email='john.doe@example.com',
    )

    # Установка пароля (примечание: для реального приложения используйте хеширование пароля)
    new_user.set_password('password123')

    # Добавление пользователя в сессию и запись в базу данных
    db.session.add(new_user)
    db.session.commit()