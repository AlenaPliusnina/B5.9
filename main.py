import time


class MyDecorator:
    def __init__(self):
        self.avg_time = 0

    def __enter__(self):
        return self.avg_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, num_runs):
        def actual_decorator(func):
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                self.avg_time += (t1 - t0)

                self.avg_time /= num_runs

            print("Выполнение заняло %.5f секунд" % self.avg_time)

        return actual_decorator


#  Класса-секундомер можно использовать как контекстный менеджер
with MyDecorator():
    #  Декоратор – объект класса-секундомера
    mydec = MyDecorator()

    # Декоратор для измерения скорости работы функций
    @mydec(num_runs=10)
    def my_decorated_function():
        for j in range(1000000):
            pass
