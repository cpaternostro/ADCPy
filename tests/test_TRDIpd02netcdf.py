# Here we test the converting a pd0 file to netcdf format.
#
# these tests are designed to follow the example here
# http://doc.pytest.org/en/latest/fixture.html
import pytest
from pathlib import Path

here = Path(__file__).parent

@pytest.fixture
def trdipd0_convert_pd0file():
    import TRDIstuff.TRDIpd0tonetcdf as TRDIpd0
    import numpy as np
    # this is a test data file, very simple ADCP file
    # of older Workhorse ADCP data with only profiler
    pd0_input_file = here.joinpath("..//data//demo1//9991wh000.000")
    netcdf_output = here.joinpath("9991wh000.cdf")
    serial_number = "473"
    delta_t = "900"  # seconds, as a string
    time_type = "CF"  # the time variable will have a CF time format
    ensembles_to_process = [265, np.inf]
    ensemble_count, netcdf_index, read_error = TRDIpd0.convert_pd0_to_netcdf(pd0_input_file, netcdf_output,
                                                                             ensembles_to_process,
                                                                             serial_number, time_type, delta_t)
    return ensemble_count, netcdf_index, read_error


def test__output(trdipd0_convert_pd0file):
    ensemble_count, netcdf_index, read_error = trdipd0_convert_pd0file
    assert ensemble_count == 499
    assert read_error is None

