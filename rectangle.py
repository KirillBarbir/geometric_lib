def area(a, b):
    '''
        Функция принимает стороны прямоугольника и выводит его площадь

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника

        Возвращаемое значение:
            area(a, b) (float): площадь прямоугольника со сторонами a и b

        Пример использования:
            Входные данные
                2.0  3.0
            Выходные данные
                6.0
    '''
    return a * b 

def perimeter(a, b):
    '''
        Функция принимает стороны прямоугольника и выводит его периметр

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника

        Возвращаемое значение:
            perimeter(a, b) (float): периметр прямоугольника со сторонами a и b

        Пример использования:
            Входные данные
                2.0  3.0
            Выходные данные
                10.0
    '''
    return a + b + a + b