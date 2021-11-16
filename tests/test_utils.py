import pytest

from hooks.pre_gen_project import validate_line_length


def test_validate_line_length():
    assert validate_line_length(88) is None

    with pytest.raises(ValueError):
        validate_line_length(1_000)

    with pytest.raises(ValueError):
        validate_line_length(-10)
