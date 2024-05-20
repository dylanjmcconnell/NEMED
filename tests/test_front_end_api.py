import nemed
from nemed import downloader
import pytest
import os
import glob
import pandas as pd

cache = "./cache_nemed/"
start = "2023/01/01 00:00"
end = "2023/02/01 00:00"
end_marginal = "2023/01/02 00:00"

# files = glob.glob(cache + "*")
# for f in files:
#     os.remove(f)

pd.set_option('display.max_rows', None)


def test_get_total_emissions():
    result = nemed.get_total_emissions(start_time=start,
                                       end_time=end,
                                       cache=cache,
                                       filter_regions=None,
                                       by=None,
                                       generation_sent_out=True,
                                       assume_energy_ramp=True,
                                       return_pivot=False)
    assert (list(result.columns) == ['TimeEnding', 'Region', 'Energy', 'Total_Emissions', 'Intensity_Index'])
    assert len(result['TimeEnding']) == 31*288*6


def test_get_marginal_emissions():
    result = nemed.get_marginal_emissions(
        start_time=start,
        end_time=end_marginal,
        cache=cache
    )
    assert (list(result.columns) == ['Time', 'Region', 'Intensity_Index', 'DUID', 'CO2E_ENERGY_SOURCE'])
    # This fails because NEMED is currently filtering out the instances where loads set the energy market price.
    # See this happening on line 138 of mod_xml_cache.
    assert len(result['Time']) == 288*5


