import pytest

from service.genre import GenreService


# Создаем класс для тестирования сервиса жанров
class TestGenreService:

    # Инициализируем сервис работы с жанрами воткнув заглушку genre_dao
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        # Получаем необходимый нам жанр
        genre = self.genre_service.get_one(1)

        # Проверяем жанр на соответствия параметрам
        assert genre is not None
        assert genre.id is not None
        assert genre.id == 1

    def test_get_all(self):
        # Получаем список всех жанров
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        # Задаем тестовый входной параметр
        data = {"name": "Тест"}
        # Выполняем сервис добавления
        genre = self.genre_service.create(data)

        assert genre is not None
        assert genre.id == 3

    def test_update(self):

        # Задаем тестовый входной параметр
        g_data = {"id": 3, "name": "PyTest"}

        # Выполняем сервис добавления
        genre = self.genre_service.update(g_data)

        # Проверяем соответствие
        assert genre is not None
        assert genre.name == "PyTest"
        assert genre.id == 3

    def test_delete(self):
        self.genre_service.delete(3)



