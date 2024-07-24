import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    def test_add_new_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", [
        'Гордость и предубеждение и зомби',
        'Что делать если ваш кот хочет вас убить'
    ])
    def test_add_new_book_too_long_name(self, collector, book_name):
        long_name = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать если ваш кот хочет вас убить', 'Комедии')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert len(books) == 1
        assert 'Гордость и предубеждение и зомби' in books

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать если ваш кот хочет вас убить', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert len(children_books) == 1
        assert 'Гордость и предубеждение и зомби' in children_books

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 1
        assert books_genre['Гордость и предубеждение и зомби'] == 'Фантастика'

    def test_get_book_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        genre = collector.get_book_genre('Гордость и предубеждение и зомби')
        assert genre == 'Фантастика'

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert 'Гордость и предубеждение и зомби' in favorites
