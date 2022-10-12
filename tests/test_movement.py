from unittest.mock import MagicMock, Mock
import pytest
from space_battle.game import Move, Vector, MovableAdapter


def test_move_object():
    uobj = {"position": Vector(12, 5), "velocity": Vector(-7, 3)}
    movable_object = MovableAdapter(uobj)
    assert movable_object.position == Vector(12, 5)
    assert movable_object.velocity == Vector(-7, 3)
    Move(movable_object).execute()
    assert movable_object.position == Vector(5, 8)


def test_raises_error_cannot_get_position():
    uobj = {}
    movable_object = MovableAdapter(uobj)
    with pytest.raises(KeyError) as exc:
        Move(movable_object).execute()


def test_raises_error_cannot_get_velocity():
    uobj = {}
    movable_object = MovableAdapter(uobj)
    with pytest.raises(KeyError) as exc:
        Move(movable_object).execute()


def test_raises_error_cannot_set_position():
    uobj = MagicMock(spec_set=dict)
    uobj.__setitem__ = Mock(side_effect=KeyError('position'))
    movable_object = MovableAdapter(uobj)
    with pytest.raises(KeyError) as exc:
        Move(movable_object).execute()
