"""Setup.py tests
"""

from projtools import data_hash

BOROUGH_10_21_HASH = "bcc488bec69c7a6ce7148dd5a05a025498c9488b"
BOROUGH_21_23_HASH = "ea7e1aa0dd0562ba2cc7ef8beffd1911f3c803f7"
LSOA_10_21_HASH = "f250f870067cd90a82b7acefbc3f7ccb2e765166"
LSOA_21_23_HASH = "8057ba79256769903b91b084e1ed0affd8e85277"
WARD_10_21_HASH = "e8778ba783691cffaaa85171c554538c849baf72"
WARD_21_23_HASH = "3db0bc2f73f95aba7c739d827145a4c85cf6d160"

def test_data_hash():
    """ Test that the data hash is correct"""
    assert data_hash.get_data_hash("lsoa_21_23.csv") == LSOA_21_23_HASH
    assert data_hash.get_data_hash("borough_10_21.csv") == BOROUGH_10_21_HASH
    assert data_hash.get_data_hash("borough_21_23.csv") == BOROUGH_21_23_HASH
    assert data_hash.get_data_hash("lsoa_10_21.csv") == LSOA_10_21_HASH
    assert data_hash.get_data_hash("ward_10_21.csv") == WARD_10_21_HASH
    assert data_hash.get_data_hash("ward_21_23.csv") == WARD_21_23_HASH
