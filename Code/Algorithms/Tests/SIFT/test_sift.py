import os
import sys
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
import pytest

from SIFT.sift import SIFT


class TestSIFT:
    @pytest.fixture
    def sift(self):
        return SIFT()
