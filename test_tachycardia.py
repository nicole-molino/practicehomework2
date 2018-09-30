from tachycardia import is_tachycardic
import pytest


@pytest.mark.parametrize("candidate,expected", [
    ("tachycardic", True),
    ("   tachyc-ardic", True),
    ("Tachyc..ardic", True),
    ("TACHYCARDIC", True),
    ("tachycardic tachycardic", False),
    ("not tachycardic", False),
    ("untachycardic", False)

])
def test_is_tachycardic(candidate, expected):
    response = is_tachycardic(candidate)
    assert response == expected
