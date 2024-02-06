from rsuanalyzer.core.rsu import calc_rsu
from rsuanalyzer.ranker.conf_group import conf_id_to_ids_in_same_group


def test_conf_id_to_ids_in_same_group_case1():
    conf_id = "RRFFLLBB"
    EXPECTED = {"RRFFLLBB", "LLBBRRFF", "LLFFRRBB", "RRBBLLFF"}
    assert conf_id_to_ids_in_same_group(conf_id) == EXPECTED

    # RSU should be the same for all the conformation IDs
    # in the same group.
    THETA = 30
    DELTA = 87
    rsu = calc_rsu(conf_id, THETA, DELTA)
    for conf_id2 in EXPECTED:
        assert rsu == calc_rsu(conf_id2, THETA, DELTA)


def test_conf_id_to_ids_in_same_group_case2():
    conf_id = "RLFBRRFF"
    EXPECTED = {
        "RLFBRRFF", "RRFFRLFB", "RRBFLRFF", "LRFFRRBF", 
        "LRFBLLFF", "LLFFLRFB", "LLBFRLFF", "RLFFLLBF"}
    assert conf_id_to_ids_in_same_group(conf_id) == EXPECTED

    # RSU should be the same for all the conformation IDs 
    # in the same group.
    THETA = 30
    DELTA = 87
    rsu = calc_rsu(conf_id, THETA, DELTA)
    for conf_id2 in EXPECTED:
        assert rsu == calc_rsu(conf_id2, THETA, DELTA)
