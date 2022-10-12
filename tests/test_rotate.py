from unittest.mock import MagicMock, Mock
import pytest
from space_battle.game import Rotate, Vector, RotableAdapted


def test_rotate_object():
    uobj = {"direction": 1, "angular_velocity": 2, "direction_number": 8}
    rotatable_object = RotableAdapted(uobj)
    Rotate(rotatable_object).execute()
    assert rotatable_object.direction == 3


def test_rotate_object_around():
    uobj = {"direction": 1, "angular_velocity": 9, "direction_number": 8}
    rotatable_object = RotableAdapted(uobj)
    Rotate(rotatable_object).execute()
    assert rotatable_object.direction == 2


def test_raises_error_cannot_get_direction():
    uobj = {}
    rotatable_object = RotableAdapted(uobj)
    with pytest.raises(KeyError) as exc:
        Rotate(rotatable_object).execute()


def test_raises_error_cannot_get_angular_velocity():
    uobj = {}
    rotatable_object = RotableAdapted(uobj)
    with pytest.raises(KeyError) as exc:
        Rotate(rotatable_object).execute()


def test_raises_error_cannot_get_direction_number():
    uobj = {}
    rotatable_object = RotableAdapted(uobj)
    with pytest.raises(KeyError) as exc:
        Rotate(rotatable_object).execute()


def test_raises_error_cannot_set_direction():
    uobj = MagicMock(spec_set=dict)
    uobj.__setitem__ = Mock(side_effect=KeyError('direction'))
    rotatable_object = RotableAdapted(uobj)
    with pytest.raises(KeyError) as exc:
        Rotate(rotatable_object).execute()
