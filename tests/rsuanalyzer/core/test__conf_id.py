import pytest

from reprod.rsuanalyzer.core._conf_id import (
    _id_to_con_types, _id_to_lig_types, _list_chains_derived_from_the_ring)


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFFLL", ["RR", "LL"]),  # chain
        ("RRFFLLBB", ["RR", "LL"]),  # ring
        ("RRFFLLBBRLFB", ["RR", "LL", "RL"])  # ring
    ]
)
def test__id_to_lig_types(conf_id, expected):
    assert _id_to_lig_types(conf_id) == expected


@pytest.mark.parametrize(
    "conf_id, expected",
    [
        ("RRFFLL", ["FF"]),  # chain
        ("RRFFLLBB", ["FF", "BB"]),  # ring
        ("RRFFLLBBRLFB", ["FF", "BB", "FB"])  # ring
    ]
)
def test__id_to_con_types(conf_id, expected):
    assert _id_to_con_types(conf_id) == expected


@pytest.mark.parametrize(
    "ring_id, expected",
    [
        ("RRFFRRFF", ["RRFFRR", "RRFFRR"]),
        ("RRFFLLBB", ["RRFFLL", "LLBBRR"]),
        ("RRFFLLBBRLFB", ["RRFFLLBBRL", "RLFBRRFFLL", "LLBBRLFBRR"]),
        ("RRFFRRFFLLFF", ["RRFFRRFFLL", "RRFFLLFFRR", "LLFFRRFFRR"])
    ]
)
def test__list_chains_derived_from_the_ring(ring_id, expected):
    assert _list_chains_derived_from_the_ring(ring_id) == expected
