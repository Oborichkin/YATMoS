import pytest


class TestBigClass:
    def test_dummy_1(self):
        pass

    def test_dummy_2(self):
        pass

    def test_dummy_3(self):
        pass

    @pytest.mark.parametrize("a", [1,2,3])
    def test_parametrized_dummy(self, a):
        pass
