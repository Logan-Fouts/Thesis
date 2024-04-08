import os
import sys
from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
import pytest

from Layers.layers import Layers


class TestLayers:
    @pytest.fixture
    def layers(self):
        return Layers()
