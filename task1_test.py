from task1 import Datacenter, getmaxind, getminind


def test_example1():
    dc_arr = [Datacenter(3) for i in range(3)]
    dc_arr[0].disable(1)
    dc_arr[1].disable(0)
    dc_arr[2].disable(2)
    assert getmaxind(dc_arr, 3) == 1
    dc_arr[0].reset()
    dc_arr[1].reset()
    dc_arr[0].disable(1)
    dc_arr[0].disable(2)
    dc_arr[1].disable(1)
    assert getmaxind(dc_arr, 3) == 2
    dc_arr[2].reset()
    assert getminind(dc_arr, 3) == 1


def test_example2():
    dc_arr = [Datacenter(2) for i in range(3)]
    dc_arr[0].disable(0)
    dc_arr[1].disable(1)
    dc_arr[1].reset()
    dc_arr[1].disable(0)
    dc_arr[1].disable(1)
    dc_arr[0].reset()
    assert getmaxind(dc_arr, 2) == 1
    dc_arr[1].disable(0)
    assert getminind(dc_arr, 2) == 2

def test_example3():
    dc_arr = [Datacenter(1)]
