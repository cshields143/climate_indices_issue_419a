import numpy as np
import pytest

@pytest.fixture(scope='module')
def values():
    return np.loadtxt('tests/fixture/values')

@pytest.fixture(scope='module')
def skews():
    return np.loadtxt('tests/fixture/skew')

@pytest.fixture(scope='module')
def locs():
    return np.loadtxt('tests/fixture/loc')

@pytest.fixture(scope='module')
def scales():
    return np.loadtxt('tests/fixture/scale')

@pytest.fixture(scope='module')
def outputs():
    return np.loadtxt('tests/fixture/out')
