class Rectangle:
    def __init__(self, length=1, width=1):
        self.width = self.set_width(width)
        self.length = self.set_length(length)

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def set_length(self, new_length):
        if self.check_value(new_length):
            self.length = new_length
        return self.length

    def set_width(self, new_width):
        if self.check_value(new_width):
            self.width = new_width
        return self.width

    @staticmethod
    def check_value(num):
        if not isinstance(num, (float, int)):
            raise TypeError('Incorrect value!')
        elif num <= 0 or num > 20:
            raise ValueError('Values must belong (0; 20)!')
        return True

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


def main():
    try:
        rec = Rectangle()
        print('w=', rec.get_width(), 'l=', rec.get_length())
        rec.set_width(12.0)
        rec.set_length(4.0)
        print('w=', rec.get_width(), 'l=', rec.get_length())
        print('S=', rec.area(), 'P=', rec.perimeter())
    except Exception as ex:
        print(ex)


main()
