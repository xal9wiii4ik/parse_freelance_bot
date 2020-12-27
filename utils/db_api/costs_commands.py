import sqlite3


class CostsCommands:
    """Команды для таблицы costs(parser_freelance_db)"""

    def __init__(self, database: str) -> None:
        """Инициализация(подключение к базе данных)"""

        self.connection = sqlite3.connect(database=database)
        self.cursor = self.connection.cursor()

    def add_new_costs(self, chat_id: int, cost: int) -> None:
        """Добавление новой категории стоимости"""

        with self.connection:
            self.cursor.execute('INSERT INTO costs (chat_id, cost) VALUES (?, ?)', (chat_id, cost))

    def get_count_cost(self, chat_id: int) -> int:
        """Получения кол-во категорий стоимости пользователя"""

        with self.connection:
            return len(self.cursor.execute('SELECT * FROM costs WHERE chat_id=?', (chat_id,)).fetchall())

    def get_costs(self, chat_id: int) -> list:
        """Получение категориий стоимости пользователя"""

        with self.connection:
            return self.cursor.execute('SELECT * FROM costs WHERE chat_id=?', (chat_id,)).fetchall()

    def exist_cost(self, chat_id: int, cost: int) -> bool:
        """Проверка на наличие категории стоимости"""

        with self.connection:
            return bool(self.cursor.execute(
                'SELECT * FROM costs WHERE chat_id=? and cost=?',
                (chat_id, cost)).fetchall()
                        )

    def delete_costs(self, chat_id: int) -> None:
        """Удаление категорий стоимости пользователя"""

        with self.connection:
            self.cursor.execute('DELETE FROM costs WHERE chat_id?', (chat_id,))

    def close(self) -> None:
        """Закрытие базы данных"""

        self.connection.close()
