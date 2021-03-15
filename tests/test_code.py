from dostuff.code import doAThing
import pytest
import numpy as np

@pytest.mark.usefixtures('values', 'skews', 'locs', 'scales', 'outputs')
def test_doAThing(values, skews, locs, scales, outputs):
    result = doAThing(values, skews, locs, scales)
    calculated_zeros = np.count_nonzero(result == 0)
    actual_zeros = np.count_nonzero(outputs == 0)
    assert calculated_zeros == actual_zeros
