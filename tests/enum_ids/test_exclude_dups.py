import numpy as np
import pytest

from rsuanalyzer.calc_rsu.rsu import calc_rsu
from rsuanalyzer.enum_ids.exclude_dups import (_different_cut_points,
                                               _enantiomer, _id_to_dup_ids,
                                               _lig_con_set_revs,
                                               _order_reversed)


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFFLLBB", ["RRFFLLBB", "LLBBRRFF"]),
        ("RRFFLLBBRLFB", ["RRFFLLBBRLFB", "LLBBRLFBRRFF", "RLFBRRFFLLBB"])
    ]
)
def test_different_cut_points(conf_id, expected):
    assert _different_cut_points(conf_id) == expected


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFFLLBB", "LLFFRRBB"),
        ("RRFFLLBBRLFB", "LRBBLLFFRRBF")
    ]
)
def test_order_reversed(conf_id, expected):
    assert _order_reversed(conf_id) == expected


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFFLLBB", "LLFFRRBB"),
        ("RRFFLLBBRLFB", "LLFFRRBBLRFB")
    ]
)
def test_enantiomer(conf_id, expected):
    assert _enantiomer(conf_id) == expected


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFF", {"RRFF", "RLBF", "LRFB", "LLBB"}),
        ("RRFFLLBB", {
            "RRFFLLBB", "LRFFLLBF", "RRFFLRFB", "LRFFLRFF",
            "RRFBRLBB", "LRFBRLBF", "RRFBRRFB", "LRFBRRFF",
            "RLBFLLBB", "LLBFLLBF", "RLBFLRFB", "LLBFLRFF",
            "RLBBRLBB", "LLBBRLBF", "RLBBRRFB", "LLBBRRFF",
            })
    ]
)
def test_lig_con_set_revs(conf_id, expected):
    assert _lig_con_set_revs(conf_id) == expected


@pytest.mark.parametrize(
    "conf_id, theta, expected",
    [
        ("RRFFLLBB", 30, {
            "RRFFLLBB", "LLBBRRFF", "LLFFRRBB", "RRBBLLFF"
        }),
        ("RRFFLLFB", 30, {
            "RRFFLLFB", "LLFBRRFF", "LLFFRRBF", "RRBFLLFF",
            "LLFFRRFB", "RRFBLLFF", "RRFFLLBF", "LLBFRRFF"
        }),
        ("RRFFLLFB", 0, {
            "RRFFLLFB", "LRFFLLFF", "RRFFLRBB", "LRFFLRBF", 
            "RRFBRLFB", "LRFBRLFF", "RRFBRRBB", "LRFBRRBF", 
            "RLBFLLFB", "LLBFLLFF", "RLBFLRBB", "LLBFLRBF", 
            "RLBBRLFB", "LLBBRLFF", "RLBBRRBB", "LLBBRRBF", 

            "LLFBRRFF", "RLFBRRFB", "LLFBRLBF", "RLFBRLBB", 
            "LLFFLRFF", "RLFFLRFB", "LLFFLLBF", "RLFFLLBB", 
            "LRBBRRFF", "RRBBRRFB", "LRBBRLBF", "RRBBRLBB", 
            "LRBFLRFF", "RRBFLRFB", "LRBFLLBF", "RRBFLLBB", 

            "LLFFRRBF", "RLFFRRBB", "LLFFRLFF", "RLFFRLFB", 
            "LLFBLRBF", "RLFBLRBB", "LLFBLLFF", "RLFBLLFB", 
            "LRBFRRBF", "RRBFRRBB", "LRBFRLFF", "RRBFRLFB", 
            "LRBBLRBF", "RRBBLRBB", "LRBBLLFF", "RRBBLLFB", 

            "RRBFLLFF", "LRBFLLFB", "RRBFLRBF", "LRBFLRBB", 
            "RRBBRLFF", "LRBBRLFB", "RRBBRRBF", "LRBBRRBB", 
            "RLFFLLFF", "LLFFLLFB", "RLFFLRBF", "LLFFLRBB", 
            "RLFBRLFF", "LLFBRLFB", "RLFBRRBF", "LLFBRRBB", 

            "LLFFRRFB", "RLFFRRFF", "LLFFRLBB", "RLFFRLBF", 
            "LLFBLRFB", "RLFBLRFF", "LLFBLLBB", "RLFBLLBF", 
            "LRBFRRFB", "RRBFRRFF", "LRBFRLBB", "RRBFRLBF", 
            "LRBBLRFB", "RRBBLRFF", "LRBBLLBB", "RRBBLLBF", 

            "RRFBLLFF", "LRFBLLFB", "RRFBLRBF", "LRFBLRBB", 
            "RRFFRLFF", "LRFFRLFB", "RRFFRRBF", "LRFFRRBB", 
            "RLBBLLFF", "LLBBLLFB", "RLBBLRBF", "LLBBLRBB", 
            "RLBFRLFF", "LLBFRLFB", "RLBFRRBF", "LLBFRRBB", 

            "RRFFLLBF", "LRFFLLBB", "RRFFLRFF", "LRFFLRFB", 
            "RRFBRLBF", "LRFBRLBB", "RRFBRRFF", "LRFBRRFB", 
            "RLBFLLBF", "LLBFLLBB", "RLBFLRFF", "LLBFLRFB", 
            "RLBBRLBF", "LLBBRLBB", "RLBBRRFF", "LLBBRRFB", 

            "LLBFRRFF", "RLBFRRFB", "LLBFRLBF", "RLBFRLBB", 
            "LLBBLRFF", "RLBBLRFB", "LLBBLLBF", "RLBBLLBB", 
            "LRFFRRFF", "RRFFRRFB", "LRFFRLBF", "RRFFRLBB", 
            "LRFBLRFF", "RRFBLRFB", "LRFBLLBF", "RRFBLLBB", 
        }),
    ]
)
def test_id_to_ids_in_same_group(conf_id, theta, expected):
    assert _id_to_dup_ids(conf_id, theta) == expected



@pytest.mark.parametrize(
    "conf_id, theta",
    [
        ("RRFFLLFB", 30),
        ("RRFFLLFB", 0),
        ("RRFFLLFB", 90),
        ("RRFFLLFBRRBB", 30),
        ("RRFFLLFBRRBB", 0),
        ("RRFFLLFBRRBB", 90),
    ]
)
def test_ids_from_same_group_have_same_rsu(conf_id, theta):
    rsu = calc_rsu(conf_id, theta, 87)
    for conf_id2 in _id_to_dup_ids(conf_id, theta):
        rsu2 = calc_rsu(conf_id2, theta, 87)
        assert np.isclose(rsu, rsu2), f"RSU of {conf_id} and {conf_id2} are not the same. {rsu} != {rsu2} (theta={theta})"
