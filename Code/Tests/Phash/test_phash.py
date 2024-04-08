import os
import sys
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
import pytest

from Phash.phash import Phash


class TestPhash:
    @pytest.fixture
    def phash(self):
        return Phash()
