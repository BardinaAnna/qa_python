from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_rating(self):     #Проверяем присвоился или нет рейтинг
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        assert collector.get_book_rating('Имя ветра') == 1

    def test_set_book_rating_set_new_rating(self):  #Проверяем изменился ли рейтинг у книги
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')

        collector.set_book_rating('Имя ветра', 6)
        assert collector.get_book_rating('Имя ветра') == 6

    def test_set_book_rating_zero_rating(self):     #Негативный тест. На нулевой рейтинг (нижняя граница)
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')

        collector.set_book_rating('Имя ветра', 0)
        assert collector.get_book_rating('Имя ветра') == 1

    def test_set_book_rating_more_possible(self):   #Негативный тест. За верхней границей
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')

        collector.set_book_rating('Имя ветра', 12)
        assert collector.get_book_rating('Имя ветра') == 1

    def test_get_book_rating_get_book_rating(self): #Получить рейтинг по названию книги
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        assert collector.get_book_rating('Имя ветра') == 1

    def test_get_book_rating_get_book_rating(self): #Негативный тест. Нет такой книги
        collector = BooksCollector()

        assert collector.get_book_rating('Имя ветра') == None