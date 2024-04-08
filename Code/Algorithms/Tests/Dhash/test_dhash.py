import os
import sys
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
import pytest

from Dhash.dhash import Dhash


class TestDhash:
    @pytest.fixture
    def dhash(self):
        return Dhash()
