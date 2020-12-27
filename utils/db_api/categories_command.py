import sqlite3


class CategoriesCommands:
    """Команды для таблицы categories (parser_freelance_db)"""

    def __init__(self, database: str) -> None:
        """Инициализация(подключение к базе данных)"""

        self.connection = sqlite3.connect(database=database)
        self.cursor = self.connection.cursor()

    def add_new_category_and_chat_id(self, chat_id: int, category: str) -> None:
        """Добавление категории пользователю"""

        with self.connection:
            self.cursor.execute('INSERT INTO categories (chat_id, category)  VALUES (?, ?)', (chat_id, category))

    def get_category(self, chat_id: int) -> list:
        """Получение категорий пользователя"""

        with self.connection:
            return self.cursor.execute('SELECT * FROM categories WHERE chat_id=?', (chat_id,)).fetchall()

    def exist_category(self, chat_id: int, category: str) -> bool:
        """Проверка имеет ли пользователь категорию"""

        with self.connection:
            return bool(self.cursor.execute(
                'SELECT * FROM categories WHERE chat_id=? and category=?',
                (chat_id, category)
            ).fetchall())

    def get_count_category(self, chat_id: int) -> int:
        """Получение числа категорий пользователя"""

        with self.connection:
            return len(self.cursor.execute(
                'SELECT * FROM categories WHERE chat_id=?', (chat_id,)
            ).fetchall())

    def delete_all_categories(self, chat_id) -> None:
        """Удаление всех категорий пользователя"""

        with self.connection:
            self.cursor.execute('DELETE FROM categories WHERE chat_id=?', (chat_id,))

    def close(self) -> None:
        """Закрытие базы данных"""

        self.connection.close()
