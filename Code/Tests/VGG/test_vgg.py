import os
import sys
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
import pytest

from VGG.vgg import VGG


class TestVGG:
    @pytest.fixture
    def vgg(self):
        return VGG()
