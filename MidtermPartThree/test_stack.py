from operator import truediv
from stack import Stack
import pytest

class TestStack(object):
    @pytest.fixture
    def clean_stack(self):
        return Stack()

    def test_size(self, clean_stack: Stack):
        assert clean_stack.size() == 0

        clean_stack.items.append(1)

        assert clean_stack.size() == 1

    def test_push(self, clean_stack: Stack):
        clean_stack.push(1)
        assert clean_stack.items[0] == 1
        assert len(clean_stack.items) == 1

        clean_stack.push("item")
        assert clean_stack.items[1] == "item"
        assert len(clean_stack.items) == 2

    def test_pop(self, clean_stack: Stack):
        clean_stack.items = ["one", 2]

        item = clean_stack.pop()
        assert item == 2
        assert len(clean_stack.items) == 1

        item = clean_stack.pop()
        assert item == "one"
        assert len(clean_stack.items) == 0

        with pytest.raises(IndexError):
            clean_stack.pop()

    def test_peek(self, clean_stack: Stack):
        clean_stack.items = [1, "two"]

        item = clean_stack.peek()
        assert item == "two"
        assert len(clean_stack.items) == 2

        clean_stack.items = []

        with pytest.raises(IndexError):
            clean_stack.peek()

    def test_is_empty(self, clean_stack: Stack):
        assert clean_stack.isEmpty()

        clean_stack.items = [1]

        assert not clean_stack.isEmpty()

    def test_str(self, clean_stack: Stack):
        output = str(clean_stack)
        assert output == "[]"

        clean_stack.items = [1, "two"]
        output = str(clean_stack)
        assert output == "[1, 'two']"

