# -*- coding: utf-8 -*-
import time
import math

# Глобальные переменные
str_lenght = 40  # Общая длина строки(символов) для форматирования карточек вывода
pi = math.pi

# Для оформления карточки вывода
title = "\033[31m{}\033[0m".format("Геометрическая фигура".center(str_lenght, "+"))
chap_init = "\033[33m{}\033[0m".format("Исходные параметры".center(str_lenght, "-"))
chap_cal = "\033[33m{}\033[0m".format("Вычисления".center(str_lenght, "-"))
ending = f'{"=" * str_lenght}'


class Geomshape:
    def __init__(self):
        # Названия фигур
        self.g_name1 = "\033[32m{}\033[0m".format("Точка").center(str_lenght + 9, "=")
        self.g_name2 = "\033[32m{}\033[0m".format("Отрезок").center(str_lenght + 9, "=")
        self.g_name3 = "\033[32m{}\033[0m".format("Квадрат").center(str_lenght + 9, "=")
        self.g_name4 = "\033[32m{}\033[0m".format("Прямоугольник").center(str_lenght + 9, "=")
        self.g_name5 = "\033[32m{}\033[0m".format("Параллелограмм").center(str_lenght + 9, "=")
        self.g_name6 = "\033[32m{}\033[0m".format("Многоугольник").center(str_lenght + 9, "=")
        self.g_name7 = "\033[32m{}\033[0m".format("Треугольник").center(str_lenght + 9, "=")
        self.g_name8 = "\033[32m{}\033[0m".format("Правильный треугольник").center(str_lenght + 9, "=")
        self.g_name9 = "\033[32m{}\033[0m".format("Окружность").center(str_lenght + 9, "=")
        self.g_name10 = "\033[32m{}\033[0m".format("Эллипс").center(str_lenght + 9, "=")

        # Названия параметров для ввода и вывода
        self.g_param_x = "Координата по оси X: "
        self.g_param_y = "Координата по оси Y: "
        self.g_param_rad = "Радиус: "
        self.g_param_per = "Периметр: "
        self.g_param_are = "Площадь: "
        self.g_param_diam = "Диаметр: "
        self.g_param_cen = "Центр: "
        self.g_param_len = "Длина: "
        self.g_param_sid = "Сторона: "
        self.g_param_ang = "Вершины: "
        self.g_param_hei = "Высота: "
        self.g_param_coord = "Координаты цента: "
        self.g_param_corn = "Угол (градус): "
        self.g_param_diag = "Диагональ: "


# вкусно и Точка


class Point(Geomshape):
    def __init__(self, point_x1, point_y1):
        self.point_x1 = point_x1
        self.point_y1 = point_y1
        super().__init__()

    def info(self):
        print("\n".join((f'{title}',
                         f'{self.g_name1}',
                         f'{chap_init}',
                         f'{self.g_param_x}{self.point_x1:>{str_lenght - len(self.g_param_x)}}',
                         f'{self.g_param_y}{self.point_y1:>{str_lenght - len(self.g_param_y)}}',
                         f'{ending}\n'
                         )))


class Direct(Point):
    def __init__(self, point_x, point_y, point_x2, point_y2):
        self.point_x2 = point_x2
        self.point_y2 = point_y2
        super().__init__(point_x, point_y)

    def direct_lenght(self):
        dir_len = ((self.point_x2 - self.point_x1) ** 2 + (self.point_y2 - self.point_y1) ** 2) ** 0.5
        return f'{dir_len:,.2f}'

    def direct_center(self):
        dir_cen_x = (self.point_x1 + self.point_x2) / 2
        dir_cen_y = (self.point_y1 + self.point_y2) / 2
        return f'x = {dir_cen_x:,.2f} y = {dir_cen_y:,.2f}'

    def info(self):
        print("\n".join((f'{title}',
                         f'{self.g_name2}',
                         f'{chap_init}',
                         f'{self.g_param_x}{self.point_x1:>{str_lenght - len(self.g_param_x)}}',
                         f'{self.g_param_y}{self.point_y1:>{str_lenght - len(self.g_param_y)}}',
                         f'{self.g_param_x}{self.point_x2:>{str_lenght - len(self.g_param_x)}}',
                         f'{self.g_param_y}{self.point_y2:>{str_lenght - len(self.g_param_y)}}',
                         f'{chap_cal}',
                         f'{self.g_param_coord}{self.direct_center():>{str_lenght - len(self.g_param_coord)}}',
                         f'{self.g_param_len}{self.direct_lenght():>{str_lenght - len(self.g_param_len)}}',
                         f'{ending}\n'
                         )))


class Quadrilateral(Geomshape):
    angl = 4

    def __init__(self, side_a, side_b=None, height=None, corner=None):
        self.side_a = side_a
        self.side_b = side_b
        self.height = height
        self.corner = corner
        super().__init__()


class Square(Quadrilateral):
    def __init__(self, side_a):
        super().__init__(side_a)

    def sq_area(self):
        sq_area = self.side_a * self.side_a
        return f'{sq_area:,.2f}'

    def sq_perim(self):
        sq_perim = self.side_a * 4
        return f'{sq_perim:,.2f}'

    def sq_diag(self):
        sq_diag = self.side_a * 2 ** 0.5
        return f'{sq_diag:,.2f}'

    def info(self):
        print("\n".join((f'{title}',
                         f'{self.g_name3}',
                         f'{chap_init}',
                         f'{self.g_param_sid}{self.side_a:>{str_lenght - len(self.g_param_sid)}}',
                         f'{chap_cal}',
                         f'{self.g_param_are}{self.sq_area():>{str_lenght - len(self.g_param_are)}}',
                         f'{self.g_param_per}{self.sq_perim():>{str_lenght - len(self.g_param_per)}}',
                         f'{self.g_param_diag}{self.sq_diag():>{str_lenght - len(self.g_param_diag)}}',
                         f'{self.g_param_ang}{Square.angl:>{str_lenght - len(self.g_param_ang)}}',
                         f'{ending}\n'
                         )))


class Rectangle(Quadrilateral):
    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b)

    def re_area(self):
        re_area = self.side_a * self.side_b
        return f'{re_area:,.2f}'

    def re_perim(self):
        re_perim = self.side_a * 2 + self.side_b * 2
        return f'{re_perim:,.2f}'

    def re_diag(self):
        re_diag = (self.side_a ** 2 + self.side_b ** 2) ** 0.5
        return f'{re_diag:,.2f}'

    def info(self):
        print("\n".join([f'{title}',
                         f'{self.g_name4}',
                         f'{chap_init}',
                         f'{self.g_param_sid}{self.side_a:>{str_lenght - len(self.g_param_sid)}}',
                         f'{self.g_param_sid}{self.side_b:>{str_lenght - len(self.g_param_sid)}}',
                         f'{chap_cal}',
                         f'{self.g_param_are}{self.re_area():>{str_lenght - len(self.g_param_are)}}',
                         f'{self.g_param_per}{self.re_perim():>{str_lenght - len(self.g_param_per)}}',
                         f'{self.g_param_diag}{self.re_diag():>{str_lenght - len(self.g_param_diag)}}',
                         f'{self.g_param_ang}{Rectangle.angl:>{str_lenght - len(self.g_param_ang)}}',
                         f'{ending}\n'
                         ]))


class Parallelogram(Quadrilateral):
    def __init__(self, side_a, height, corner):
        super().__init__(side_a, None, height, corner)

    def par_side_b(self):
        pa_side_b = round(self.height / math.sin(math.radians(self.corner)), 2)
        return pa_side_b

    def pa_area(self):
        pa_area = self.side_a * self.par_side_b() * math.sin(math.radians(self.corner))
        return f'{pa_area:,.2f}'

    def pa_perim(self):
        pa_perim = self.side_a * 2 + self.par_side_b() * 2
        return f'{pa_perim:,.2f}'

    def pa_diag(self):
        pa_diag_1 = (self.side_a ** 2 + self.par_side_b() ** 2 + 2 * self.side_a * self.par_side_b() * math.cos(
            math.radians(self.corner))) ** 0.5
        pa_diag_2 = (self.side_a ** 2 + self.par_side_b() ** 2 - 2 * self.side_a * self.par_side_b() * math.cos(
            math.radians(self.corner))) ** 0.5
        return f'd1 = {pa_diag_1:,.2f}   d2 = {pa_diag_2:,.2f}'

    def info(self):
        print("\n".join([f'{title}',
                         f'{self.g_name5}',
                         f'{chap_init}',
                         f'{self.g_param_sid}{self.side_a:>{str_lenght - len(self.g_param_sid)}}',
                         f'{self.g_param_hei}{self.height:>{str_lenght - len(self.g_param_hei)}}',
                         f'{self.g_param_corn}{self.corner:>{str_lenght - len(self.g_param_corn)}}',
                         f'{chap_cal}',
                         f'{self.g_param_are}{self.pa_area():>{str_lenght - len(self.g_param_are)}}',
                         f'{self.g_param_per}{self.pa_perim():>{str_lenght - len(self.g_param_per)}}',
                         f'{self.g_param_diag}{self.pa_diag():>{str_lenght - len(self.g_param_diag)}}',
                         f'{self.g_param_sid}{self.par_side_b():>{str_lenght - len(self.g_param_sid)}}',
                         f'{self.g_param_ang}{Rectangle.angl:>{str_lenght - len(self.g_param_ang)}}',
                         f'{ending}\n'
                         ]))


class PolygonShape(Geomshape):
    def __init__(self, side_a, count_side):
        self.side_a = side_a
        self.count_side = count_side
        super().__init__()

    def pol_ang(self):
        pol_ang = self.count_side
        return f'{pol_ang:,.2f}'

    def pol_area(self):
        pol_area = self.count_side * self.side_a ** 2 / 4 * (1 / math.tan(math.radians(180 / self.count_side)))
        return f'{pol_area:,.2f}'

    def pol_perim(self):
        pol_perim = self.side_a * self.count_side
        return f'{pol_perim:,.2f}'

    def pol_corn(self):
        pol_corn = (self.count_side - 2) / self.count_side * 180
        return f'{pol_corn:,.3f}'

    def info(self):
        print("\n".join([f'{title}',
                         f'{self.g_name6}',
                         f'{chap_init}',
                         f'{self.g_param_len}{self.side_a:>{str_lenght - len(self.g_param_len)}}',
                         f'{self.g_param_sid}{self.count_side:>{str_lenght - len(self.g_param_sid)}}',
                         f'{chap_cal}',
                         f'{self.g_param_are}{self.pol_area():>{str_lenght - len(self.g_param_are)}}',
                         f'{self.g_param_per}{self.pol_perim():>{str_lenght - len(self.g_param_per)}}',
                         f'{self.g_param_ang}{self.pol_ang():>{str_lenght - len(self.g_param_ang)}}',
                         f'{self.g_param_corn}{self.pol_corn():>{str_lenght - len(self.g_param_corn)}}',
                         f'{ending}\n'
                         ]))


class Triangle(Geomshape):
    def __init__(self, side_a, side_b, corner):
        self.side_a = side_a
        self.side_b = side_b
        self.corner = corner
        self.ang = 3
        super().__init__()

    def side_c(self):
        side_c = round((self.side_a ** 2 + self.side_b ** 2 - 2 * self.side_a * self.side_b * math.cos(
            math.radians(self.corner))) ** 0.5, 2)
        return side_c

    def tr_area(self):
        tr_area = 0.5 * self.side_a * self.side_b * math.sin(math.radians(self.corner))
        return f'{tr_area:,.2f}'

    def tr_perim(self):
        tr_perim = self.side_a + self.side_b + self.side_c()
        return f'{tr_perim:,.2f}'

    def info(self):
        print("\n".join([f'{title}',
                         f'{self.g_name7}',
                         f'{chap_init}',
                         f'{self.g_param_len}{self.side_a:>{str_lenght - len(self.g_param_len)}}',
                         f'{self.g_param_len}{self.side_b:>{str_lenght - len(self.g_param_len)}}',
                         f'{self.g_param_corn}{self.corner:>{str_lenght - len(self.g_param_corn)}}',
                         f'{chap_cal}',
                         f'{self.g_param_sid}{self.side_c():>{str_lenght - len(self.g_param_sid)}}',
                         f'{self.g_param_are}{self.tr_area():>{str_lenght - len(self.g_param_are)}}',
                         f'{self.g_param_per}{self.tr_perim():>{str_lenght - len(self.g_param_per)}}',
                         f'{self.g_param_ang}{self.ang:>{str_lenght - len(self.g_param_ang)}}',
                         f'{ending}\n'
                         ]))


class TrueTriangle(Geomshape):
    def __init__(self, side_a):
        self.side_a = side_a
        self.ang = 3
        super().__init__()

    def ttr_area(self):
        ttr_area = 3 ** 0.5 / 4 * self.side_a ** 2
        return f'{ttr_area:,.2f}'

    def ttr_perim(self):
        ttr_perim = self.side_a * 3
        return f'{ttr_perim:,.2f}'

    def info(self):
        print("\n".join([f'{title}',
                         f'{self.g_name8}',
                         f'{chap_init}',
                         f'{self.g_param_len}{self.side_a:>{str_lenght - len(self.g_param_len)}}',
                         f'{chap_cal}',
                         f'{self.g_param_are}{self.ttr_area():>{str_lenght - len(self.g_param_are)}}',
                         f'{self.g_param_per}{self.ttr_perim():>{str_lenght - len(self.g_param_per)}}',
                         f'{self.g_param_ang}{self.ang:>{str_lenght - len(self.g_param_ang)}}',
                         f'{ending}\n'
                         ]))


class Circle(Geomshape):
    def __init__(self, cir_rad):
        self.cir_rad = cir_rad
        super().__init__()

    def cir_len(self):
        cir_len = 2 * pi * self.cir_rad
        return f'{cir_len:,.2f}'

    def cir_area(self):
        cir_area = pi * self.cir_rad ** 2
        return f'{cir_area:,.2f}'

    def cir_diam(self):
        cir_diam = self.cir_rad * 2
        return f'{cir_diam:,.2f}'

    def info(self):
        print("\n".join((f'{title}',
                         f'{self.g_name9}',
                         f'{chap_init}',
                         f'{self.g_param_rad}{self.cir_rad:>{str_lenght - len(self.g_param_rad)}}',
                         f'{chap_cal}',
                         f'{self.g_param_diam}{self.cir_diam():>{str_lenght - len(self.g_param_diam)}}',
                         f'{self.g_param_are}{self.cir_area():>{str_lenght - len(self.g_param_are)}}',
                         f'{self.g_param_len}{self.cir_len():>{str_lenght - len(self.g_param_len)}}',
                         f'{ending}\n'
                         )))


class Ellipse(Geomshape):
    def __init__(self, radius_1, radius_2):
        self.radius_1 = radius_1
        self.radius_2 = radius_2
        super().__init__()

    def el_area(self):
        el_area = pi * self.radius_1 * self.radius_2
        return f'{el_area:,.2f}'

    def el_diam(self):
        el_diam_1 = self.radius_1 * 2
        el_diam_2 = self.radius_2 * 2
        return f'д1 = {el_diam_1:,.2f}  д2 = {el_diam_2:,.2f}'

    def info(self):
        print("\n".join((f'{title}',
                         f'{self.g_name10}',
                         f'{chap_init}',
                         f'{self.g_param_rad}{self.radius_1:>{str_lenght - len(self.g_param_rad)}}',
                         f'{self.g_param_rad}{self.radius_2:>{str_lenght - len(self.g_param_rad)}}',
                         f'{chap_cal}',
                         f'{self.g_param_diam}{self.el_diam():>{str_lenght - len(self.g_param_diam)}}',
                         f'{self.g_param_are}{self.el_area():>{str_lenght - len(self.g_param_are)}}',
                         f'{ending}\n'
                         )))

#  Начинаем с заставки :)


print("\033[34m{}\033[0m".format(
    f'..........@@@@.....................................................................................\n'
    f'.........@@..@.....................................................................................\n'
    f'.........@....@....................................................................................\n'
    f'........@@....@....................................................................................\n'
    f'........@.....@..........@@@@@@@...@@@@@@......@@@@@@@@....@@@@@@@@@@@@@.@@@@...@@@@@@.............\n'
    f'.......@@.....@@.........@@@@@@@..@@@@@@@..@@@@@@@@@@@@@@@....@@@@@@.....@@@@..@@@@@@..............\n'
    f'.......@.......@........@@@@.@@@.@@@.@@@@.@@@@..@@@@..@@@@....@@@@@.....@@@@..@@@@@@@..............\n'
    f'......@@.......@........@@@..@@@@@@..@@@..@@@@..@@@@.@@@@.....@@@@......@@@@@@@.@@@@@..............\n'
    f'......@........@........@@@..@@@@@..@@@@...@@@@@@@@@@@@.......@@@@.....@@@@@@@..@@@@...............\n'
    f'......@........@@......@@@@..@@@@...@@@........@@@@..........@@@@@.....@@@@@....@@@@...............\n'
    f'.....@..........@..................................................................................\n'
    f'..@@@...........@...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..@@@@@>...\n'
    f'................@@.@@..............................................................................\n'
    f'.................@@@...............................................................................\n'))

print(f"\nЗадание №11 \"Геометрические фигуры\"\n"
      f"\nДаны следующие фигуры:\n")

#  Создаём словарь доступных фигур и выводим его на экран
gs = Geomshape()
while True:
    time.sleep(0.25)
    geom_dict = {1: gs.g_name1.replace("=", ""),
                 2: gs.g_name2.replace("=", ""),
                 3: gs.g_name3.replace("=", ""),
                 4: gs.g_name4.replace("=", ""),
                 5: gs.g_name5.replace("=", ""),
                 6: gs.g_name6.replace("=", ""),
                 7: gs.g_name7.replace("=", ""),
                 8: gs.g_name8.replace("=", ""),
                 9: gs.g_name9.replace("=", ""),
                 10: gs.g_name10.replace("=", "")
                 }
    for key, value in geom_dict.items():
        print(f'{" " * 2}{key}.{" " * (3 - len(str(key)))} {value}')
        time.sleep(0.25)

    #  Cоздаём пустое множество для возможности ввода только одного вида геометрической фигуры

    geom_list = set()

    #  Цикл для выбора фигур из списка доступных

    num = int(float(input(f"\nВведите номер фигуры из списка или 0 для завершения ввода: ")))
    while num != 0:
        if max(geom_dict.keys()) >= num >= min(geom_dict.keys()):
            geom_list.add(num)
            num = int(float(input(f'Выбрана фигура \"{geom_dict[num]}\" добавить еще? для завершения ввода "0": ')))
        else:
            print(f'Числа \"{"\033[31m{}\033[0m".format(num)}\" нет в списке, смотри внимательнее еще раз')
            for key, value in geom_dict.items():
                print(f'{" " * 2}{key}.{" " * (2 - len(str(key)))} {value}')
            num = int(float(input(f"\nВведите номер фигуры из списка или 0 для завершения: ")))

    print(f'\nВыбор сделан:')
    for elem in geom_list:
        print(f'{geom_dict.get(elem)}', end="\n")
        time.sleep(0.25)

    for i in range(len(geom_list)):
        shape = geom_list.pop()
        if shape == 1:
            print(gs.g_name1)
            out_point_x = float(input("Введите координату X:"))
            out_point_y = float(input("Введите координату Y:"))
            p = Point(out_point_x, out_point_y)
            p.info()
        elif shape == 2:
            print(gs.g_name2)
            out_point_x = float(input("Введите координату X1:"))
            out_point_y = float(input("Введите координату Y1:"))
            out_point_x1 = float(input("Введите координату X2:"))
            out_point_y1 = float(input("Введите координату Y2:"))
            d = Direct(out_point_x, out_point_y, out_point_x1, out_point_y1)
            d.info()
        elif shape == 3:
            print(gs.g_name3)
            out_side_a = float(input("Введите сторону квадрата:"))
            s = Square(out_side_a)
            s.info()
        elif shape == 4:
            print(gs.g_name4)
            out_side_a = float(input("Введите сторону прямоугольника:"))
            out_side_b = float(input("Введите вторую сторону прямоугольника:"))
            while out_side_a == out_side_b:
                print("\033[31m{}\033[0m".format("Стороны прямоугольника не могут быть равны"))
                out_side_a = float(input("Введите сторону прямоугольника:"))
                out_side_b = float(input("Введите вторую сторону прямоугольника:"))
            r = Rectangle(out_side_a, out_side_b)
            r.info()
        elif shape == 5:
            print(gs.g_name5)
            out_side_a = float(input("Введите сторону параллелограмма:"))
            out_height = float(input("Введите высоту параллелограмма:"))
            out_corner = float(input("Введите угол между сторонами параллелограмма:"))
            r = Parallelogram(out_side_a, out_height, out_corner)
            r.info()
        elif shape == 6:
            print(gs.g_name6)
            out_side_a = int(float(input("Введите сторону многоугольника:")))
            out_count = int(float(input("Введите кол-во сторон многоугольника:")))
            while out_count < 5:
                print("\033[31m{}\033[0m".format("В многоугольнике не может быть меньше 5 сторон, повторите ввод"))
                out_count = int(float(input("Введите кол-во сторон многоугольника:")))
            ps = PolygonShape(out_side_a, out_count)
            ps.info()
        elif shape == 7:
            print(gs.g_name7)
            out_side_a = float(input("Введите сторону треугольника:"))
            out_side_b = float(input("Введите вторую сторону треугольника:"))
            out_corner = float(input("Введите угол между сторонами:"))
            tr = Triangle(out_side_a, out_side_b, out_corner)
            tr.info()
        elif shape == 8:
            print(gs.g_name8)
            out_side_a = float(input("Введите сторону правильного треугольника:"))
            ttr = TrueTriangle(out_side_a)
            ttr.info()
        elif shape == 9:
            print(gs.g_name9)
            out_cir_rad = float(input("Введите радиус окружности:"))
            cir = Circle(out_cir_rad)
            cir.info()
        elif shape == 10:
            print(gs.g_name10)
            out_radius_1 = float(input("Введите первый радиус эллипса:"))
            out_radius_2 = float(input("Введите второй радиус эллипса:"))
            while out_radius_1 == out_radius_2:
                print("\033[31m{}\033[0m".format("Радиусы не могут быть равны, повторите ввод."))
                out_radius_1 = float(input("Введите первый радиус эллипса:"))
                out_radius_2 = float(input("Введите второй радиус эллипса:"))
            el = Ellipse(out_radius_1, out_radius_2)
            el.info()
    if len(geom_list) == 0:
        yes_no = input("Список фигур пуст, повторить ввод \"+ / -\" :")
        if yes_no == "-":
            print("\033[36m{}\033[0m".format("Экипаж прощается с вами и желает Вам приятного... "))
            break
        if yes_no == "+":
            print("\033[32m{}\033[0m".format("Поехали!"))
            continue
