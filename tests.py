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

    def test_add_new_book_add_an_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        collector.add_new_book('Имя ветра')

        assert len(collector.get_books_rating()) == 1

    def test_add_new_book_add_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        assert collector.get_book_rating('Имя ветра') == 1

    def test_set_book_rating_set_new_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')

        collector.set_book_rating('Имя ветра', 6)
        assert collector.get_book_rating('Имя ветра') == 6

    def test_set_book_rating_zero_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')

        collector.set_book_rating('Имя ветра', 0)
        assert collector.get_book_rating('Имя ветра') == 1

    def test_set_book_rating_more_possible(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')

        collector.set_book_rating('Имя ветра', 11)
        assert collector.get_book_rating('Имя ветра') == 1

    def test_get_book_rating_get_book_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        assert collector.get_book_rating('Имя ветра') == 1

    def test_get_book_rating_get_rating_for_missing_book(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Имя ветра') == None

    def test_get_books_with_specific_rating_get_list_books_on_tating(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')
        collector.add_new_book('Страхи мудреца')

        collector.set_book_rating('Имя ветра', 10)

        assert len(collector.get_books_with_specific_rating(10)) == 1

    def test_get_books_with_specific_rating_get_list_books_non_existent_tating(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')
        collector.add_new_book('Страхи мудреца')

        assert len(collector.get_books_with_specific_rating(10)) == 0

    def test_get_books_with_specific_rating_get_list_books_on_zero_tating(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')

        assert len(collector.get_books_with_specific_rating(0)) == 0

    def test_get_books_with_specific_rating_get_list_books_on_more_possible_tating(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')

        assert len(collector.get_books_with_specific_rating(11)) == 0

    def test_get_books_rating_get_list_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Имя ветра')
        collector.add_new_book('Страхи мудреца')

        assert len(collector.get_books_rating()) == 2

    def test_add_book_in_favorites_add_two_books_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        collector.add_new_book('Страхи мудреца')
        collector.add_book_in_favorites('Имя ветра')
        collector.add_book_in_favorites('Страхи мудреца')

        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_add_an_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        collector.add_book_in_favorites('Имя ветра')
        collector.add_book_in_favorites('Имя ветра')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_non_existing_book(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Имя ветра')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        collector.add_book_in_favorites('Имя ветра')
        collector.delete_book_from_favorites('Имя ветра')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_deleting_non_existent_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        collector.add_new_book('Страхи мудреца')
        collector.add_book_in_favorites('Имя ветра')
        collector.delete_book_from_favorites('Страхи мудреца')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_get_list_of_favorites_books_from_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Имя ветра')
        collector.add_new_book('Страхи мудреца')
        collector.add_book_in_favorites('Имя ветра')
        collector.add_book_in_favorites('Страхи мудреца')

        assert len(collector.get_list_of_favorites_books()) == 2
