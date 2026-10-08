# exercises: run with `pytest exercises/`; plain `pytest` only collects tests/
import pytest
import torch


@pytest.fixture(autouse=True)
def _seed():
    # same RNG state per test, so random inputs are reproducible
    torch.manual_seed(0)
