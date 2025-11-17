class DatabaseConnection:
    """Класс для управления подключением к базе данных"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Создание нового подключения к базе данных...")
            cls._instance = super().__new__(cls)
            cls._instance.connection_string = "postgresql://localhost:5432/mydb"
        return cls._instance

    def query(self, sql):
        return f"Выполнение запроса '{sql}' через {self.connection_string}"

# Демонстрация работы паттерна
if __name__ == "__main__":
    # Первое обращение - создается экземпляр
    db1 = DatabaseConnection()
    print(f"db1 ID: {id(db1)}")
    print(db1.query("SELECT * FROM users") + "\n")

    # Второе обращение - возвращается тот же экземпляр
    db2 = DatabaseConnection()
    print(f"db2 ID: {id(db2)}")
    print(db2.query("INSERT INTO users VALUES (1, 'John')") + "\n")

    # Проверка, что это один и тот же объект
    print(f"db1 и db2 - это один объект: {db1 is db2}")

class Notification:
    """Базовый класс для уведомлений"""
    def send(self, message):
        return f"Отправка {self.__class__.__name__}: {message}"

class EmailNotification(Notification):
    """Email уведомление"""
    pass

class SMSNotification(Notification):
    """SMS уведомление"""
    pass

class PushNotification(Notification):
    """Push уведомление"""
    pass

class NotificationFactory:
    """Фабрика для создания уведомлений"""
    def create_notification(self, notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Неизвестный тип уведомления: {notification_type}")

# Демонстрация работы Factory Method
if __name__ == "__main__":
    print("\n" + "="*50)
    print("Демонстрация Factory Method паттерна")
    print("="*50)
    
    factory = NotificationFactory()
    
    # Создаем разные типы уведомлений
    email = factory.create_notification("email")
    sms = factory.create_notification("sms")
    push = factory.create_notification("push")
    
    # Отправляем сообщения
    print(email.send("Добро пожаловать в наше приложение!"))
    print(sms.send("Ваш код подтверждения: 123456"))
    print(push.send("У вас новое сообщение"))
    
    # Показываем типы объектов
    print(f"\nТип email уведомления: {type(email)}")
    print(f"Тип SMS уведомления: {type(sms)}")
    print(f"Тип push уведомления: {type(push)}")












class Notification:
    """Базовый класс для уведомлений"""
    def send(self, message):
        return f"Отправка {self.__class__.__name__}: {message}"

class EmailNotification(Notification):
    """Email уведомление"""
    pass

class SMSNotification(Notification):
    """SMS уведомление"""
    pass

class PushNotification(Notification):
    """Push уведомление"""
    pass

class NotificationFactory:
    """Фабрика для создания уведомлений"""
    def create_notification(self, notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Неизвестный тип уведомления: {notification_type}")

# Демонстрация работы Factory Method
if __name__ == "__main__":
    print("\n" + "="*50)
    print("Демонстрация Factory Method паттерна")
    print("="*50)
    
    factory = NotificationFactory()
    
    # Создаем разные типы уведомлений
    email = factory.create_notification("email")
    sms = factory.create_notification("sms")
    push = factory.create_notification("push")
    
    # Отправляем сообщения
    print(email.send("Добро пожаловать в наше приложение!"))
    print(sms.send("Ваш код подтверждения: 123456"))
    print(push.send("У вас новое сообщение"))
    
    # Показываем типы объектов
    print(f"\nТип email уведомления: {type(email)}")
    print(f"Тип SMS уведомления: {type(sms)}")
    print(f"Тип push уведомления: {type(push)}")
from abc import ABC, abstractmethod

# Абстрактный класс транспорта
class Transport(ABC):
    @abstractmethod
    def deliver(self, destination):
        pass

# Конкретные классы транспорта
class Truck(Transport):
    def deliver(self, destination):
        return f"Груз доставляется в {destination} на грузовике по дороге"

class Ship(Transport):
    def deliver(self, destination):
        return f"Груз доставляется в {destination} на корабле по морю"

class Plane(Transport):
    def deliver(self, destination):
        return f"Груз доставляется в {destination} на самолете по воздуху"

# Абстрактная фабрика логистики
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass
    
    def plan_delivery(self, destination):
        transport = self.create_transport()
        return transport.deliver(destination)

# Конкретные фабрики
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Plane()

# Демонстрация работы Factory Method
if __name__ == "__main__":
    print("\n" + "="*50)
    print("Демонстрация Factory Method паттерна (Логистика)")
    print("="*50)
    
    print("Планирование доставок:")
    
    # Наземная логистика
    road = RoadLogistics()
    print(road.plan_delivery("Санкт-Петербург"))
    
    # Морская логистика
    sea = SeaLogistics()
    print(sea.plan_delivery("Новороссийск"))
    
    # Воздушная логистика
    air = AirLogistics()
    print(air.plan_delivery("Пекин"))

# Абстрактная фабрика - UI элементы для разных ОС
from abc import ABC, abstractmethod

# Абстрактные продукты
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def input_text(self, text):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def toggle(self):
        pass

# Конкретные продукты для Windows
class WindowsButton(Button):
    def render(self):
        return "Отрисована кнопка в стиле Windows"
    
    def click(self):
        return "Кнопка Windows нажата"

class WindowsTextField(TextField):
    def render(self):
        return "Отображено текстовое поле в стиле Windows"
    
    def input_text(self, text):
        return f"Введен текст в Windows поле: {text}"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Отрисован чекбокс в стиле Windows"
    
    def toggle(self):
        return "Чекбокс Windows переключен"

# Конкретные продукты для Mac
class MacButton(Button):
    def render(self):
        return "Отрисована кнопка в стиле macOS"
    
    def click(self):
        return "Кнопка macOS нажата"

class MacTextField(TextField):
    def render(self):
        return "Отображено текстовое поле в стиле macOS"
    
    def input_text(self, text):
        return f"Введен текст в macOS поле: {text}"

class MacCheckbox(Checkbox):
    def render(self):
        return "Отрисован чекбокс в стиле macOS"
    
    def toggle(self):
        return "Чекбокс macOS переключен"

# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_text_field(self) -> TextField:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_text_field(self) -> TextField:
        return WindowsTextField()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_text_field(self) -> TextField:
        return MacTextField()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Клиентский код
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.text_field = None
        self.checkbox = None
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.text_field = self.factory.create_text_field()
        self.checkbox = self.factory.create_checkbox()
    
    def render_ui(self):
        results = []
        results.append(self.button.render())
        results.append(self.text_field.render())
        results.append(self.checkbox.render())
        return results
    
    def interact_with_ui(self):
        results = []
        results.append(self.button.click())
        results.append(self.text_field.input_text("Hello World"))
        results.append(self.checkbox.toggle())
        return results

# Демонстрация работы Abstract Factory
if __name__ == "__main__":
    print("\n" + "="*50)
    print("Демонстрация Abstract Factory паттерна")
    print("="*50)
    
    # Создаем приложение для Windows
    print("Создание приложения для Windows:")
    windows_factory = WindowsFactory()
    windows_app = Application(windows_factory)
    windows_app.create_ui()
    
    print("Отрисовка UI:")
    for result in windows_app.render_ui():
        print(f"  - {result}")
    
    print("Взаимодействие с UI:")
    for result in windows_app.interact_with_ui():
        print(f"  - {result}")
    
    print("\n" + "Создание приложения для macOS:")
    mac_factory = MacFactory()
    mac_app = Application(mac_factory)
    mac_app.create_ui()
    
    print("Отрисовка UI:")
    for result in mac_app.render_ui():
        print(f"  - {result}")
    
    print("Взаимодействие с UI:")
    for result in mac_app.interact_with_ui():
        print(f"  - {result}")


















# Абстрактная фабрика - UI элементы для разных ОС
from abc import ABC, abstractmethod

# Абстрактные продукты
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def click(self):
        pass

class TextField(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def input_text(self, text):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def toggle(self):
        pass

# Конкретные продукты для Windows
class WindowsButton(Button):
    def render(self):
        return "Отрисована кнопка в стиле Windows"
    
    def click(self):
        return "Кнопка Windows нажата"

class WindowsTextField(TextField):
    def render(self):
        return "Отображено текстовое поле в стиле Windows"
    
    def input_text(self, text):
        return f"Введен текст в Windows поле: {text}"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Отрисован чекбокс в стиле Windows"
    
    def toggle(self):
        return "Чекбокс Windows переключен"

# Конкретные продукты для Mac
class MacButton(Button):
    def render(self):
        return "Отрисована кнопка в стиле macOS"
    
    def click(self):
        return "Кнопка macOS нажата"

class MacTextField(TextField):
    def render(self):
        return "Отображено текстовое поле в стиле macOS"
    
    def input_text(self, text):
        return f"Введен текст в macOS поле: {text}"

class MacCheckbox(Checkbox):
    def render(self):
        return "Отрисован чекбокс в стиле macOS"
    
    def toggle(self):
        return "Чекбокс macOS переключен"

# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_text_field(self) -> TextField:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_text_field(self) -> TextField:
        return WindowsTextField()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_text_field(self) -> TextField:
        return MacTextField()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Клиентский код
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.text_field = None
        self.checkbox = None
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.text_field = self.factory.create_text_field()
        self.checkbox = self.factory.create_checkbox()
    
    def render_ui(self):
        results = []
        results.append(self.button.render())
        results.append(self.text_field.render())
        results.append(self.checkbox.render())
        return results
    
    def interact_with_ui(self):
        results = []
        results.append(self.button.click())
        results.append(self.text_field.input_text("Hello World"))
        results.append(self.checkbox.toggle())
        return results

# Демонстрация работы Abstract Factory
if __name__ == "__main__":
    print("\n" + "="*50)
    print("Демонстрация Abstract Factory паттерна")
    print("="*50)
    
    # Создаем приложение для Windows
    print("Создание приложения для Windows:")
    windows_factory = WindowsFactory()
    windows_app = Application(windows_factory)
    windows_app.create_ui()
    
    print("Отрисовка UI:")
    for result in windows_app.render_ui():
        print(f"  - {result}")
    
    print("Взаимодействие с UI:")
    for result in windows_app.interact_with_ui():
        print(f"  - {result}")
    
    print("\n" + "Создание приложения для macOS:")
    mac_factory = MacFactory()
    mac_app = Application(mac_factory)
    mac_app.create_ui()
    
    print("Отрисовка UI:")
    for result in mac_app.render_ui():
        print(f"  - {result}")
    
    print("Взаимодействие с UI:")
    for result in mac_app.interact_with_ui():
        print(f"  - {result}")
# Builder - построение сложных объектов
from abc import ABC, abstractmethod

# Продукт
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphics_card = None
        self.motherboard = None
        self.power_supply = None
    
    def __str__(self):
        specs = [
            f"Процессор: {self.cpu}",
            f"Оперативная память: {self.ram}",
            f"Накопитель: {self.storage}",
            f"Видеокарта: {self.graphics_card}",
            f"Материнская плата: {self.motherboard}",
            f"Блок питания: {self.power_supply}"
        ]
        return "Собранный компьютер:\\n" + "\\n".join(f"  - {spec}" for spec in specs)

# Строитель
class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()
    
    @abstractmethod
    def build_cpu(self):
        pass
    
    @abstractmethod
    def build_ram(self):
        pass
    
    @abstractmethod
    def build_storage(self):
        pass
    
    @abstractmethod
    def build_graphics_card(self):
        pass
    
    @abstractmethod
    def build_motherboard(self):
        pass
    
    @abstractmethod
    def build_power_supply(self):
        pass
    
    def get_computer(self):
        return self.computer

# Конкретные строители
class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel Core i9-14900K"
    
    def build_ram(self):
        self.computer.ram = "32GB DDR5 6000MHz"
    
    def build_storage(self):
        self.computer.storage = "2TB NVMe SSD + 4TB HDD"
    
    def build_graphics_card(self):
        self.computer.graphics_card = "NVIDIA RTX 4090 24GB"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS ROG MAXIMUS Z790"
    
    def build_power_supply(self):
        self.computer.power_supply = "1200W 80+ Platinum"

class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5-13400"
    
    def build_ram(self):
        self.computer.ram = "16GB DDR4 3200MHz"
    
    def build_storage(self):
        self.computer.storage = "1TB NVMe SSD"
    
    def build_graphics_card(self):
        self.computer.graphics_card = "Integrated Intel UHD Graphics"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS PRIME B760M-A"
    
    def build_power_supply(self):
        self.computer.power_supply = "550W 80+ Bronze"

class ServerComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "AMD EPYC 9754 (128 ядер)"
    
    def build_ram(self):
        self.computer.ram = "256GB DDR5 ECC"
    
    def build_storage(self):
        self.computer.storage = "8TB NVMe SSD RAID 10"
    
    def build_graphics_card(self):
        self.computer.graphics_card = "Basic GPU для вывода"
    
    def build_motherboard(self):
        self.computer.motherboard = "Supermicro H13DSH"
    
    def build_power_supply(self):
        self.computer.power_supply = "2000W Redundant PSU"

# Директор
class ComputerEngineer:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder
    
    def build_computer(self):
        print("Начинаем сборку компьютера...")
        self.builder.build_motherboard()
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_graphics_card()
        self.builder.build_power_supply()
        print("Сборка завершена!")

# Демонстрация работы Builder
if __name__ == "__main__":
    print("\\n" + "="*50)
    print("Демонстрация Builder паттерна")
    print("="*50)
    
    # Сборка игрового компьютера
    print("1. Сборка игрового компьютера:")
    gaming_builder = GamingComputerBuilder()
    engineer = ComputerEngineer(gaming_builder)
    engineer.build_computer()
    gaming_computer = gaming_builder.get_computer()
    print(gaming_computer)
    
    print("\\n2. Сборка офисного компьютера:")
    office_builder = OfficeComputerBuilder()
    engineer = ComputerEngineer(office_builder)
    engineer.build_computer()
    office_computer = office_builder.get_computer()
    print(office_computer)
    
    print("\\n3. Сборка серверного компьютера:")
    server_builder = ServerComputerBuilder()
    engineer = ComputerEngineer(server_builder)
    engineer.build_computer()
    server_computer = server_builder.get_computer()
    print(server_computer)






























# Builder - построение сложных объектов
from abc import ABC, abstractmethod

# Продукт
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.graphics_card = None
        self.motherboard = None
        self.power_supply = None
    
    def __str__(self):
        specs = [
            f"Процессор: {self.cpu}",
            f"Оперативная память: {self.ram}",
            f"Накопитель: {self.storage}",
            f"Видеокарта: {self.graphics_card}",
            f"Материнская плата: {self.motherboard}",
            f"Блок питания: {self.power_supply}"
        ]
        return "Собранный компьютер:\\n" + "\\n".join(f"  - {spec}" for spec in specs)

# Строитель
class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()
    
    @abstractmethod
    def build_cpu(self):
        pass
    
    @abstractmethod
    def build_ram(self):
        pass
    
    @abstractmethod
    def build_storage(self):
        pass
    
    @abstractmethod
    def build_graphics_card(self):
        pass
    
    @abstractmethod
    def build_motherboard(self):
        pass
    
    @abstractmethod
    def build_power_supply(self):
        pass
    
    def get_computer(self):
        return self.computer

# Конкретные строители
class GamingComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel Core i9-14900K"
    
    def build_ram(self):
        self.computer.ram = "32GB DDR5 6000MHz"
    
    def build_storage(self):
        self.computer.storage = "2TB NVMe SSD + 4TB HDD"
    
    def build_graphics_card(self):
        self.computer.graphics_card = "NVIDIA RTX 4090 24GB"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS ROG MAXIMUS Z790"
    
    def build_power_supply(self):
        self.computer.power_supply = "1200W 80+ Platinum"

class OfficeComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "Intel Core i5-13400"
    
    def build_ram(self):
        self.computer.ram = "16GB DDR4 3200MHz"
    
    def build_storage(self):
        self.computer.storage = "1TB NVMe SSD"
    
    def build_graphics_card(self):
        self.computer.graphics_card = "Integrated Intel UHD Graphics"
    
    def build_motherboard(self):
        self.computer.motherboard = "ASUS PRIME B760M-A"
    
    def build_power_supply(self):
        self.computer.power_supply = "550W 80+ Bronze"

class ServerComputerBuilder(ComputerBuilder):
    def build_cpu(self):
        self.computer.cpu = "AMD EPYC 9754 (128 ядер)"
    
    def build_ram(self):
        self.computer.ram = "256GB DDR5 ECC"
    
    def build_storage(self):
        self.computer.storage = "8TB NVMe SSD RAID 10"
    
    def build_graphics_card(self):
        self.computer.graphics_card = "Basic GPU для вывода"
    
    def build_motherboard(self):
        self.computer.motherboard = "Supermicro H13DSH"
    
    def build_power_supply(self):
        self.computer.power_supply = "2000W Redundant PSU"

# Директор
class ComputerEngineer:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder
    
    def build_computer(self):
        print("Начинаем сборку компьютера...")
        self.builder.build_motherboard()
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_graphics_card()
        self.builder.build_power_supply()
        print("Сборка завершена!")

# Демонстрация работы Builder
if __name__ == "__main__":
    print("\\n" + "="*50)
    print("Демонстрация Builder паттерна")
    print("="*50)
    
    # Сборка игрового компьютера
    print("1. Сборка игрового компьютера:")
    gaming_builder = GamingComputerBuilder()
    engineer = ComputerEngineer(gaming_builder)
    engineer.build_computer()
    gaming_computer = gaming_builder.get_computer()
    print(gaming_computer)
    
    print("\\n2. Сборка офисного компьютера:")
    office_builder = OfficeComputerBuilder()
    engineer = ComputerEngineer(office_builder)
    engineer.build_computer()
    office_computer = office_builder.get_computer()
    print(office_computer)
    
    print("\\n3. Сборка серверного компьютера:")
    server_builder = ServerComputerBuilder()
    engineer = ComputerEngineer(server_builder)
    engineer.build_computer()
    server_computer = server_builder.get_computer()
    print(server_computer)