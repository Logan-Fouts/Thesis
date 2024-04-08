import os
import sys
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
import pytest

from Wrapper.wrapper import Wrapper


class TestWrapper:
    @pytest.fixture
    def wrapper(self):
        return Wrapper()
