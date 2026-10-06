# shared fixtures for every test in this folder
import pytest
import torch


@pytest.fixture(autouse=True)
def _seed():
    # same RNG state per test: random batches and inits are reproducible
    torch.manual_seed(0)
