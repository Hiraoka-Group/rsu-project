from rsuanalyzer.ranker.enum_conf_ids import (enum_conf_ids_including_dups,
                                              exclude_duplicates)


def test_enum_groups_case1():
    EXPECTED = {"RRFF", "RRFB", "RRBB", "RLFF", "RLFB", "RLBB"}
    theta = 30
    rings = enum_conf_ids_including_dups(1)
    groups = exclude_duplicates(rings, theta)
    assert groups == EXPECTED
