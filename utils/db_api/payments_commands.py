import sqlite3

from datetime import datetime


class PaymentsCommands:
    """Команды для таблицы payments (parser_freelance_db)"""

    def __init__(self, database: str) -> None:
        """Инициализация(подключение к базе данных)"""

        self.connection = sqlite3.connect(database=database)
        self.cursor = self.connection.cursor()

    def exist_user(self, chat_id: int) -> bool:
        """Проверка на наличие пользователя в базе"""

        with self.connection:
            return bool(self.cursor.execute('SELECT * FROM payments WHERE chat_id=?', (chat_id,)))

    def add_new_subscriber(self, chat_id, payment_date: str) -> None:
        """Добавление новго пользователя"""

        with self.connection:
            self.cursor.execute('INSERT INTO payments (payment_state, chat_id, payment_date) VALUES (?)',
                                (True, chat_id, payment_date))

    def edit_payment_state_and_time(self, payment_state: bool,
                                    chat_id: int,
                                    payment_date: str = None) -> None:
        """Изменение состояния оплаты и даты оплаты"""

        with self.connection:
            self.cursor.execute(
                'UPDATE payments SET payment_state=?, payment_date=?, month=? WHERE chat_id=?',
                (payment_state, payment_date, True, chat_id)
            )

    def get_month(self, chat_id: int):
        """Получение месяца подписки"""

        with self.connection:
            return self.cursor.execute('SELECT month FROM payments WHERE chat_id=?',
                                       (chat_id,))

    def get_payment_users(self) -> list:
        """Получение списка оплаченных пользователей"""

        with self.connection:
            return self.cursor.execute('SELECT * FROM payments WHERE payment_state=?',
                                       (True,)).fetchall()

    def get_un_payment_users(self) -> list:
        """Получение списка не оплаченных пользователей"""

        with self.connection:
            return self.cursor.execute('SELECT * FROM payments WHERE payment_state=?',
                                       (False,)).fetchall()

    def update_un_payment_days(self, chat_id: int, unpaid_days: int) -> None:
        """Обновление не оплаченных дней"""

        with self.connection:
            self.cursor.execute(
                'UPDATE payments SET unpaid_days=? WHERE chat_id=?',
                (unpaid_days, chat_id)
            )

    def close(self) -> None:
        """Закрытие базы данных"""

        self.connection.close()
