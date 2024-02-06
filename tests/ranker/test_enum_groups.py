from itertools import product

from rsuanalyzer.ranker.conf_group import conf_id_to_group_id
from rsuanalyzer.ranker.enum_groups import enum_groups


def test_enum_groups_case1():
    EXPECTED = {1: {"RRFF", "RRFB", "RRBB", "RLFF", "RLFB", "RLBB"}}
    assert enum_groups(1) == EXPECTED


def test_enum_groups_case2():
    LIG_TYPES = ["RR", "RL", "LR", "LL"]
    CON_TYPES = ["FF", "FB", "BF", "BB"]

    CON_LIG_TYPES = [lig_type + con_type for lig_type, con_type in product(LIG_TYPES, CON_TYPES)]

    for ring in (id_of_lig1 + id_of_lig2 for id_of_lig1, id_of_lig2 in product(CON_LIG_TYPES, repeat=2)):
        assert conf_id_to_group_id(ring) in enum_groups(2)[2]
    