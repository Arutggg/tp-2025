class SortingStrategy:
    """Базовый класс стратегии сортировки."""
    def sort(self, data):
        raise NotImplementedError

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        # Сортировка пузырьком
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("Сортировка пузырьком")
        return arr

class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        # Быстрая сортировка
        print("Быстрая сортировка")
        return sorted(data)

class Sorter:
    """Контекст, который использует стратегию сортировки."""
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)

if __name__ == "__main__":
    print("=== STRATEGY ===")
    data = [5, 3, 8, 4, 2]
    sorter = Sorter(BubbleSortStrategy())
    print("Исходные данные:", data)
    print("Результат:", sorter.sort(data))

    sorter.set_strategy(QuickSortStrategy())
    print("Результат с другой стратегией:", sorter.sort(data))
    print()















class Request:
    """Простой запрос с типом и сообщением."""
    def __init__(self, request_type, message):
        self.request_type = request_type
        self.message = message

class Handler:
    """Базовый обработчик в цепочке."""
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        """Задать следующий обработчик и вернуть его (удобно строить цепочку)."""
        self.next = handler
        return handler

    def handle(self, request):
        """По умолчанию просто пересылаем дальше."""
        if self.next:
            self.next.handle(request)

class AuthHandler(Handler):
    def handle(self, request):
        if request.request_type == "auth":
            print(f"[AuthHandler] Обрабатываю запрос аутентификации: {request.message}")
        else:
            print("[AuthHandler] Не мой тип, передаю дальше...")
            super().handle(request)

class LogHandler(Handler):
    def handle(self, request):
        if request.request_type == "log":
            print(f"[LogHandler] Логирую событие: {request.message}")
        else:
            print("[LogHandler] Не мой тип, передаю дальше...")
            super().handle(request)

class ErrorHandler(Handler):
    def handle(self, request):
        if request.request_type == "error":
            print(f"[ErrorHandler] Обрабатываю ошибку: {request.message}")
        else:
            print("[ErrorHandler] Конец цепочки, обработчика нет.")

if __name__ == "__main__":
    print("=== CHAIN OF RESPONSIBILITY ===")
    auth = AuthHandler()
    log = LogHandler()
    error = ErrorHandler()

    # Строим цепочку: auth -> log -> error
    auth.set_next(log).set_next(error)

    auth.handle(Request("auth", "Логин пользователя"))
    auth.handle(Request("log", "Пользователь открыл страницу профиля"))
    auth.handle(Request("error", "Не удалось сохранить данные"))
    auth.handle(Request("unknown", "Какой-то странный запрос"))
    print()









class WordsCollection:
    """Коллекция слов, по которой можно итерироваться."""
    def __init__(self, words):
        self._words = words

    def __iter__(self):
        # Каждый раз при for возвращаем новый итератор
        return WordsIterator(self._words)

class WordsIterator:
    """Простой итератор по списку слов."""
    def __init__(self, words):
        self._words = words
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._words):
            word = self._words[self._index]
            self._index += 1
            return word
        # Сигнал Python'y, что элементы закончились
        raise StopIteration

if __name__ == "__main__":
    print("=== ITERATOR ===")
    words = WordsCollection(['Python', 'Patterns', 'Are', 'Cool'])
    
    print("Обход коллекции через for:")
    for w in words:
        print("Слово:", w)
    
    print("\nРучной обход через итератор:")
    iterator = iter(words)
    try:
        while True:
            print("Слово:", next(iterator))
    except StopIteration:
        print("Конец коллекции")
    print()





















    class Database:
        """Интерфейс базы данных."""
    def query(self, sql):
        raise NotImplementedError

class RealDatabase(Database):
    """Реальная база данных."""
    def query(self, sql):
        print(f"[RealDatabase] Выполняю запрос: {sql}")
        return f"Результат запроса: {sql}"

class DatabaseProxy(Database):
    """Прокси: проверяет доступ и только потом обращается к реальной БД."""
    def __init__(self, has_access):
        self.has_access = has_access
        self._real_db = RealDatabase()
        self._cache = {}

    def query(self, sql):
        if not self.has_access:
            print("[Proxy] Доступ запрещён! Запрос не будет выполнен.")
            return None
        
        print("[Proxy] Доступ разрешён")
        
        # Проверяем кэш
        if sql in self._cache:
            print("[Proxy] Возвращаем результат из кэша")
            return self._cache[sql]
        
        # Выполняем запрос и кэшируем результат
        result = self._real_db.query(sql)
        self._cache[sql] = result
        print("[Proxy] Результат закэширован")
        return result

if __name__ == "__main__":
    print("=== PROXY ===")
    
    # Пользователь без доступа
    user_db = DatabaseProxy(has_access=False)
    print("Пользователь пытается выполнить запрос:")
    user_db.query("SELECT * FROM users")
    
    print("\n" + "="*30)
    
    # Администратор с доступом
    admin_db = DatabaseProxy(has_access=True)
    print("Администратор выполняет запросы:")
    
    # Первый запрос - выполняется и кэшируется
    print("\nПервый запрос:")
    result1 = admin_db.query("SELECT * FROM users")
    print(f"Результат: {result1}")
    
    # Повторный запрос - берется из кэша
    print("\nПовторный запрос:")
    result2 = admin_db.query("SELECT * FROM users")
    print(f"Результат: {result2}")
    
    # Новый запрос - выполняется и кэшируется
    print("\nНовый запрос:")
    result3 = admin_db.query("SELECT name FROM products")
    print(f"Результат: {result3}")
    
    print()
































    class ExternalLogger:
        """Сторонний логгер с несовместимым интерфейсом."""
    def log_message(self, msg):
        print(f"[ExternalLogger] {msg}")

class Logger:
    """Интерфейс логгера, который ожидает наш код."""
    def log(self, message):
        raise NotImplementedError

class LoggerAdapter(Logger):
    """Адаптер: делает ExternalLogger совместимым с Logger."""
    def __init__(self, external_logger):
        self._external_logger = external_logger

    def log(self, message):
        # Адаптируем вызов к нужному методу
        self._external_logger.log_message(message)

class OldPaymentSystem:
    """Старая платежная система с устаревшим интерфейсом."""
    def process_payment_usd(self, amount):
        print(f"[OldPaymentSystem] Обработка платежа: ${amount}")
        return f"Платеж ${amount} обработан"

class NewPaymentGateway:
    """Новый интерфейс платежной системы, который ожидает наше приложение."""
    def make_payment(self, amount_rub):
        raise NotImplementedError

class PaymentAdapter(NewPaymentGateway):
    """Адаптер для старой платежной системы."""
    def __init__(self, old_system):
        self._old_system = old_system

    def make_payment(self, amount_rub):
        # Конвертируем рубли в доллары и адаптируем вызов
        amount_usd = amount_rub / 75.0  # Примерный курс
        print(f"[PaymentAdapter] Конвертация {amount_rub} руб в ${amount_usd:.2f}")
        return self._old_system.process_payment_usd(amount_usd)

if __name__ == "__main__":
    print("=== ADAPTER ===")
    
    print("\n1. Адаптер для логгера:")
    external_logger = ExternalLogger()
    logger = LoggerAdapter(external_logger)
    
    logger.log("Приложение запущено")
    logger.log("Ошибка: что-то пошло не так")
    
    print("\n2. Адаптер для платежной системы:")
    old_payment = OldPaymentSystem()
    payment_adapter = PaymentAdapter(old_payment)
    
    result = payment_adapter.make_payment(1500)  # 1500 рублей
    print(f"Результат: {result}")
    
    print("\n3. Работа с разными суммами:")
    amounts = [500, 3000, 7500]
    for amount in amounts:
        result = payment_adapter.make_payment(amount)
        print(f"Платеж {amount} руб: {result}")
    
    print()






















from abc import ABC, abstractmethod

class Device(ABC):
    """Интерфейс устройства вывода."""
    @abstractmethod
    def display(self, data):
        pass

class Monitor(Device):
    def display(self, data):
        print(f"[Monitor] Показ на мониторе: {data}")

class Printer(Device):
    def display(self, data):
        print(f"[Printer] Печать на бумагу: {data}")

class Projector(Device):
    def display(self, data):
        print(f"[Projector] Проецирование на экран: {data}")

class OutputType(ABC):
    """
    Абстракция типа вывода.
    Хранит ссылку на Device, но сама решает как форматировать данные.
    """
    def __init__(self, device):
        self._device = device

    @abstractmethod
    def render(self, data):
        pass

class TextOutput(OutputType):
    def render(self, data):
        formatted_data = f"📝 Текст: {data}"
        self._device.display(formatted_data)

class ImageOutput(OutputType):
    def render(self, data):
        formatted_data = f"🖼️ Изображение: {data}"
        self._device.display(formatted_data)

class ChartOutput(OutputType):
    def render(self, data):
        formatted_data = f"📊 Диаграмма: {data}"
        self._device.display(formatted_data)

if __name__ == "__main__":
    print("=== BRIDGE ===")
    
    # Создаем устройства
    monitor = Monitor()
    printer = Printer()
    projector = Projector()
    
    print("\n1. Вывод текста на разные устройства:")
    text_on_monitor = TextOutput(monitor)
    text_on_printer = TextOutput(printer)
    text_on_projector = TextOutput(projector)
    
    text_on_monitor.render("Hello, World!")
    text_on_printer.render("Отчет за 2024 год")
    text_on_projector.render("Презентация проекта")
    
    print("\n2. Вывод изображений на разные устройства:")
    image_on_monitor = ImageOutput(monitor)
    image_on_printer = ImageOutput(printer)
    
    image_on_monitor.render("photo.jpg")
    image_on_printer.render("graph.png")
    
    print("\n3. Вывод диаграмм на разные устройства:")
    chart_on_monitor = ChartOutput(monitor)
    chart_on_projector = ChartOutput(projector)
    
    chart_on_monitor.render("Продажи по месяцам")
    chart_on_projector.render("Статистика посещений")
    
    print("\n4. Динамическая смена устройства:")
    output = TextOutput(monitor)
    output.render("Первоначальный вывод на монитор")
    
    # Меняем устройство вывода
    output._device = printer
    output.render("Тот же текст, но теперь на принтере")
    
    output._device = projector
    output.render("И теперь на проекторе")
    
    print()
    