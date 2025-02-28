class Transport:
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self._brand = brand  # Приватный атрибут
        self._model = model  # Приватный атрибут
        self._year = year  # Приватный атрибут

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        :return: Строка с информацией о транспортном средстве.
        """
        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление транспортного средства.

        :return: Официальная строка с информацией о транспортном средстве.
        """
        return f"Transport(brand='{self._brand}', model='{self._model}', year={self._year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        :return: Сообщение о запуске двигателя.
        """
        return f"{self._brand} {self._model} engine started."


class Car(Transport):
    """
    Класс для легковых автомобилей, наследующий от Transport.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param brand: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.doors = doors  # Используем свойство для установки количества дверей

    @property
    def doors(self) -> int:
        return self._doors

    @doors.setter
    def doors(self, value: int) -> None:
        if value < 0:
            raise ValueError("Количество дверей не может быть отрицательным.")
        self._doors = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        :return: Строка с информацией о легковом автомобиле.
        """
        return f"{super().__str__()} with {self._doors} doors"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление легкового автомобиля.

        :return: Официальная строка с информацией о легковом автомобиле.
        """
        return f"Car(brand='{self._brand}', model='{self._model}', year={self._year}, doors={self._doors})"

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового автомобиля.

        :return: Сообщение о запуске двигателя с дополнительной информацией.
        """
        return f"{super().start_engine()} This car has {self._doors} doors."


class Truck(Transport):
    """
    Класс для грузовых автомобилей, наследующий от Transport.
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        :param brand: Марка грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность в тоннах.
        """
        super().__init__(brand, model, year)  # Вызов конструктора базового класса
        self.capacity = capacity  # Используем свойство для установки грузоподъемности

    @property
    def capacity(self) -> float:
        return self._capacity

    @capacity.setter
    def capacity(self, value: float) -> None:
        if value < 0:
            raise ValueError("Грузоподъемность не может быть отрицательной.")
        self._capacity = value


