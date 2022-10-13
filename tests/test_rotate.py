from unittest.mock import MagicMock, Mock
import pytest
from space_battle.game import Rotate


def test_rotate_object():
    rotatable_object = MagicMock()
    rotatable_object.get_direction = Mock(return_value=1)
    rotatable_object.get_angular_velocity = Mock(return_value=2)
    rotatable_object.get_direction_number = Mock(return_value=8)
    rotatable_object.set_direction = Mock()
    Rotate(rotatable_object).execute()
    rotatable_object.set_direction.assert_called_once_with(3)


def test_rotate_object_around():
    rotatable_object = MagicMock()
    rotatable_object.get_direction = Mock(return_value=1)
    rotatable_object.get_angular_velocity = Mock(return_value=9)
    rotatable_object.get_direction_number = Mock(return_value=8)
    rotatable_object.set_direction = Mock()
    Rotate(rotatable_object).execute()
    rotatable_object.set_direction.assert_called_once_with(2)


def test_raises_error_cannot_get_direction():
    rotatable_object = MagicMock()
    rotatable_object.get_direction = Mock(side_effect=Exception)
    with pytest.raises(Exception):
        Rotate(rotatable_object).execute()


def test_raises_error_cannot_get_angular_velocity():
    rotatable_object = MagicMock()
    rotatable_object.get_angular_velocity = Mock(side_effect=Exception)
    with pytest.raises(Exception):
        Rotate(rotatable_object).execute()


def test_raises_error_cannot_get_direction_number():
    rotatable_object = MagicMock()
    rotatable_object.get_direction_number = Mock(side_effect=Exception)
    with pytest.raises(Exception):
        Rotate(rotatable_object).execute()


def test_raises_error_cannot_set_direction():
    rotatable_object = MagicMock()
    rotatable_object.set_direction = Mock(side_effect=Exception)
    with pytest.raises(Exception):
        Rotate(rotatable_object).execute()
