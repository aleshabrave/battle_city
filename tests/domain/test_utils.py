import pytest

from app.domain.utils import Methods, Size, Vector


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
        [
            (Size(1, -1), 54, Size(54, -54)),
            (Size(0, 0), 100500, Size(0, 0)),
            (Size(1, 1), 0, Size(0, 0)),
        ],
    )
    def test__mul(self, size, scalar, expected):
        assert size * scalar == expected


class TestsMethods:
    @pytest.mark.parametrize(
        "source,other,expected",
        [
            (
                (Vector(1, 1), Size(1, 1)),
                (Vector(3, 2), Size(1, 1)),
                False,
            ),
            (
                (Vector(1, 1), Size(3, 3)),
                (Vector(3, 2), Size(1, 1)),
                True,
            ),
            (
                (Vector(1, 1), Size(2, 2)),
                (Vector(2, 1), Size(2, 2)),
                True,
            ),
            (
                (Vector(1, 1), Size(2, 2)),
                (Vector(1, 1), Size(2, 2)),
                True,
            ),
            (
                (Vector(1, 2), Size(2, 2)),
                (Vector(3, 1), Size(2, 2)),
                False,
            ),
            (
                (Vector(1, 1), Size(1, 2)),
                (Vector(1, 4), Size(1, 2)),
                False,
            ),
            (
                (Vector(1, 1), Size(1, 1)),
                (Vector(0, 0), Size(1, 1)),
                False,
            ),
        ],
    )
    def test__are_intersected(
        self, source: tuple[Vector, Size], other: tuple[Vector, Size], expected
    ):
        actual = Methods.are_intersected(source, other)

        assert actual == expected
