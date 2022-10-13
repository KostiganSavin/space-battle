from unittest.mock import MagicMock, Mock
import pytest
from space_battle.game import Move, Vector


def test_move_object():
    mock_movable = MagicMock()
    mock_movable.get_position = Mock(spec=Vector, return_value=Vector(12, 5))
    mock_movable.get_velocity = Mock(spec=Vector, return_value=Vector(-7, 3))
    mock_movable.set_position = Mock(return_value=None)
    Move(mock_movable).execute()
    mock_movable.get_position.assert_called_once()
    mock_movable.get_velocity.assert_called_once()
    mock_movable.set_position.assert_called_once_with(Vector(5, 8))


def test_raises_error_cannot_get_position():
    mock_movable = MagicMock()
    mock_movable.get_position = Mock(side_effect=Exception)
    with pytest.raises(Exception):
        Move(mock_movable).execute()


def test_raises_error_cannot_get_velocity():
    mock_movable = MagicMock()
    mock_movable.get_velocity = Mock(side_effect=Exception)
    with pytest.raises(Exception):
        Move(mock_movable).execute()


def test_raises_error_cannot_set_position():
    mock_movable = MagicMock()
    mock_movable.set_position = Mock(side_effect=Exception)
    with pytest.raises(Exception):
        Move(mock_movable).execute()
