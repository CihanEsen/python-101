import unittest

from exercises import gym


class TestGym(unittest.TestCase):
    def test_enter(self):
        pure_gym = gym.Gym(3)
        a = gym.Group(1)
        b = gym.Group(3)
        c = gym.Group(4)

        assert pure_gym.enter(a)
        assert pure_gym.active_members == 1
        assert not pure_gym.enter(c)

        pure_gym.leave(a)
        assert pure_gym.active_members == 0

        assert pure_gym.enter(b)
        assert pure_gym.active_members == 3
