import pytest
from main import Triangle


@pytest.mark.parametrize(
    "a, b, c, expected_type",
    [
        (3, 4, 5, "Разносторонний"),
        (5, 5, 8, "Равнобедренный"),
        (6, 6, 6, "Равносторонний"),
    ],
)
def test_valid_triangle_types_by_sides(a, b, c, expected_type):
    triangle = Triangle(a, b, c)
    assert triangle.type_by_sides() == expected_type


@pytest.mark.parametrize(
    "a, b, c, expected_area",
    [
        (3, 4, 5, 6.0),
        (5, 12, 13, 30.0),
        (6, 8, 10, 24.0),
    ],
)
def test_valid_triangle_area(a, b, c, expected_area):
    triangle = Triangle(a, b, c)
    assert pytest.approx(triangle.area(), 0.01) == expected_area


@pytest.mark.parametrize(
    "a, b, c, expected_angle_type",
    [
        (3, 4, 5, "Прямоугольный"),
        (5, 6, 7, "Остроугольный"),
        (7, 10, 5, "Тупоугольный"),
    ],
)
def test_valid_triangle_types_by_angles(a, b, c, expected_angle_type):
    triangle = Triangle(a, b, c)
    assert triangle.type_by_angles() == expected_angle_type


@pytest.mark.parametrize(
    "a, b, c",
    [
        (-3, 4, 5),
        (0, 4, 5),
        (1, 2, 3),
        (10, 2, 3),
    ],
)
def test_invalid_triangle_sides(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


@pytest.mark.parametrize(
    "a, b, c",
    [
        ("a", 2, 3),
        (2, "b", 3),
        (2, 3, "c"),
    ],
)
def test_invalid_triangle_non_numeric(a, b, c):
    with pytest.raises(ValueError, match="All sides must be numeric."):
        Triangle(a, b, c)
