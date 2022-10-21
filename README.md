# qa_python второй спринт Anna Bardina

test_add_new_book_add_two_books - Добавление двух книг

test_add_new_book_add_an_existing_book - Проверяем, что нельзя добавить уже существующую книгу

test_add_new_book_add_rating - Проверяем, присвоился или нет рейтинг книге

test_set_book_rating_set_new_rating - Проверяем, изменяется ли рейтинг у книги

test_set_book_rating_zero_rating - рейтинг не может быть меньше 1

test_set_book_rating_more_possible - рейтинг не может быть больше 10

test_get_book_rating_get_book_rating - получить рейтинг по названию книги

test_get_book_rating_get_rating_for_missing_book - Проверяем, что ничего не ломается, если запросить рейтинг не существующей книги

test_get_books_with_specific_rating_get_list_books_on_tating - Получаем список книг по определенному рейтингу

test_get_books_with_specific_rating_get_list_books_non_existent_tating - Проверяем, что если сделать запрос по несуществующему рейтингу, то список будет пуст

test_get_books_with_specific_rating_get_list_books_on_zero_tating - Вернеться пустой список, если сделать запрос с рейтингом меньше 1

test_get_books_with_specific_rating_get_list_books_on_more_possible_tating - Вернеться пустой список, если сделать запрос с рейтингом больше 10

test_get_books_rating_get_list_two_books - Получаем список из двух книг

test_add_book_in_favorites_add_two_books_in_favorites - Добавление в избранного двух книг

test_add_book_in_favorites_add_an_existing_book - Проверяем, что нельзя добавить в избранное книгу дважды

test_add_book_in_favorites_add_non_existing_book - В избранное не добавиться книга, которой мы не добавили рейтинг

test_delete_book_from_favorites_delete_book_from_favorites - Удаление книги из избранного

test_delete_book_from_favorites_deleting_non_existent_book_from_favorites - Проверяем, что при удалении из избранного несуществующей книги в избранном, ничего лищнего не удаляется

test_get_list_of_favorites_books_get_list_of_favorites_books_from_two_books - получение списка избранного из двух книг