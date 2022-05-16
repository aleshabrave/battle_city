import pytest

from app.domain.data import Vector, Size


class TestsVector:
    @pytest.mark.parametrize(
        "vector1,vector2,expected",
        [
            (Vector(1, 1), Vector(-1, -1), Vector(0, 0)),
            (Vector(-102, 2), Vector(-102, 2), Vector(-204, 4)),
        ],
    )
    def test__add(self, vector1, vector2, expected):
        assert vector1 + vector2 == expected

    @pytest.mark.parametrize(
        "vector,scalar,expected",
        [
            (Vector(1, -1), 54, Vector(54, -54)),
            (Vector(0, 0), 100500, Vector(0, 0)),
            (Vector(1, 1), 0, Vector(0, 0)),
        ],
    )
    def test__mul(self, vector, scalar, expected):
        assert vector * scalar == expected


class TestsSize:
    @pytest.mark.parametrize(
        "size,scalar,expected",
        [(Size(1, 1), 54, Size(0, 0)), (Size(500, 1000), 500, Size(1, 2))],
    )
    def test__floordiv(self, size, scalar, expected):
        assert size // scalar == expected

    def test__floordiv_with_exception(self):
        with pytest.raises(ZeroDivisionError):
            Size(1, 1) // 0

    @pytest.mark.parametrize(
        "size,scalar,expected",
        [
            (Size(1, -1), 54, Size(54, -54)),
            (Size(0, 0), 100500, Size(0, 0)),
            (Size(1, 1), 0, Size(0, 0)),
        ],
    )
    def test__mul(self, size, scalar, expected):
        assert size * scalar == expected
