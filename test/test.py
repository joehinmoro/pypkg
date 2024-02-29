from pypkg import data_sci

def test_sort_n_slice():
    """
    test the sort_n_slice function
    """

    assert data_sci.sort_n_slice([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert data_sci.sort_n_slice([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert data_sci.sort_n_slice([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'


def test_fibonacci():
    assert data_sci.fibonacci(40) == 63245986, "incorrect"
    assert data_sci.fibonacci(20) == 4181, "incorrect"
    assert data_sci.fibonacci(5) == 3, "incorrect"