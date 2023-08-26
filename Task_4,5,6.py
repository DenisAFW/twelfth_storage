# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.
# ----------------------------------------------------------
# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.
# ----------------------------------------------------------
# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше или равно {self.max_value}')


class Rectangle:
    __slots__ = ('_height', '_width')

    height = Range(1, 100)
    width = Range(1, 100)

    def __init__(self, height: int, width=None):
        self._height = height
        if width:
            self._width = width
        else:
            self._width = height

    def get_perimetr(self):
        return 2 * (self._height + self._width)

    def get_area(self):
        return self._width * self._height

    # @property
    # def height(self):
    #     return self._height
    #
    # @property
    # def width(self):
    #     return self._width

    # @height.setter
    # def height(self, value):
    #     if value <= 0:
    #         raise ValueError("должно быть больше нуля")
    #     self._height = value
    #
    # @width.setter
    # def width(self, value):
    #     if value <= 0:
    #         raise ValueError("должно быть больше нуля")
    #     self._width = value

    def __str__(self):
        return f'прямоугольник ({self._height}x{self._width}), S= {self.get_area()}'

    def __repr__(self):
        return f'размеры:({self._height}x{self._width}), S= {self.get_area()}'


if __name__ == "__main__":
    rect = Rectangle(2, 5)
    rect.width = -1
    print(rect)
