def parse_input(user_input): # розділяє введення користувача на команду та аргументи
    cmd, *args = user_input.strip().split()
    cmd = cmd.strip().lower()
    return cmd, *args


def normalize_name(name):
    return name.strip().capitalize() # видаляє пробіли та перетворює першу літеру на велику


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Please enter name and phone number."
        except IndexError:
            return "Please enter contact name"
    return inner # повертає функцію з обробкою помилок


@input_error # декоратор для обробки помилок введення
def add_contact(args, contacts): # додає новий контакт до телефонної книги
    if len(args) < 2: # перевірка наявності імені та частини номера
        raise ValueError
    name = normalize_name(args[0])
    if name in contacts: # перевірка наявності контакту
        raise KeyError
    phone = " ".join(args[1:])  # об’єднати решту аргументів у один рядок
    contacts[name] = phone # додавання контакту до словника
    return "Contact added."


@input_error
def change_contact(args, contacts): # змінює номер телефону контакту
    if len(args) < 2:
        raise ValueError
    name = normalize_name(args[0])
    phone = " ".join(args[1:])
    if name in contacts:
        contacts[name] = phone # оновлення номера телефону
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    name = normalize_name(args[0])
    return contacts[name] # повертає номер телефону контакту


def show_all(contacts): # показує список усіх збережених контактів
    if not contacts: # перевірка наявності контактів
        return "No contacts saved."
    result = [] # список для зберігання результатів
    for name, phone in contacts.items(): # перебір контактів
        result.append(f"{name}: {phone}") # форматування рядка
    return "\n".join(result) # об’єднання рядків у один з розділенням на нові рядки


def main(): # головна функція для запуску бота
    contacts = {} # словник для зберігання контактів
    print("Welcome to the assistant bot!")
    while True: # цикл для обробки команд користувача
        user_input = input("Enter a command: ") # введення команди користувача
        if not user_input.strip():
            continue

        command, *args = parse_input(user_input) # розділення введення на команду та аргументи

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Please try with key words: hello, add, change, phone, all, exit or close.")


if __name__ == "__main__":
    main()
