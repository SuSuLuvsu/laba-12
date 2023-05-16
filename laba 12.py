def laba12_1():
    class IceCreamStand:
        def init(self, name, flavors):
            self.name = name
            self.flavors = flavors

        def show_flavors(self):
            print("Список доступных сортов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)

    my_stand = IceCreamStand("Кафе-мороженное", ['ванильное', 'шоколадное', 'клубничное', 'малиновое'])
    my_stand.show_flavors()


def laba12_2():
    class IceCreamStand:
        def init(self, name, flavors, location, working_hours, type_flavors):
            self.name = name
            self.flavors = flavors
            self.location = location
            self.working_hours = working_hours
            self.type_flavors = type_flavors

        def show_flavors(self):
            print("Список доступных сортов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)

        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f'Сорт {flavor} добавлен в список')

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f'Сорт {flavor} удален из списка')
            else:
                print(f'Сорт {flavor} не найден в списке')

        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f'Сорт {flavor} есть в списке')
            else:
                print(f'Сорта {flavor} нет в списке')

        def describe_stand(self):
            print(f"Стенд мороженного {self.name}")
            print(f"Место: {self.location}")
            print(f"Время работы: {self.working_hours}")

        def show_Typesflavors(self):
            print("Список доступных типов мороженого:")
            for types in self.type_flavors:
                print("- " + types)

    my_stand = IceCreamStand("Кафе-мороженное", ['ванильное', 'шоколадное', 'клубничное', 'малиновое'], 'Невский проспект',
                             '12.00 - 18.00', ['эскимо', 'стакан', 'фруктоввый лед', 'алкогольное'])

    my_stand.describe_stand()
    my_stand.show_flavors()
    my_stand.show_Typesflavors()

    my_stand.check_flavor("клубничное")
    my_stand.check_flavor("фисташковое")

    my_stand.add_flavor("фисташковое")
    my_stand.check_flavor("фисташковое")

    my_stand.remove_flavor("клубничное")
    my_stand.check_flavor("клубничное")


def lab12_3():
    class IceCreamStand:
        def init(self, name, flavors):
            self.name = name
            self.flavors = flavors

        def get_menu(self):
            menu = "Добро пожаловать в наше кафе-мороженного " + self.name + "\n"
            menu += "У нас есть следующие сорта:\n"
            for flavor in self.flavors:
                menu += "- " + flavor + "\n"
            return menu

    import tkinter as tk

    my_stand = IceCreamStand("фруктовый бум", ["ванильный", "шоколад", "ягодный"])

    root = tk.Tk()
    root.title("фруктовый бум")

    menu_label = tk.Label(root, text=my_stand.get_menu())
    menu_label.pack()

    root.mainloop()
