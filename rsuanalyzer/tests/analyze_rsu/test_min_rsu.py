import pytest

from rsuanalyzer.src.analyze_rsu.min_rsu import (
    _calc_min_rsu_for_specific_theta, calc_min_rsu_for_thetas)


@pytest.mark.parametrize(
    "conf_ids, mock_rsu_list, expected", [
        (["RRFF", "RRFB", "RRBF"], [0.2, 0.1, 0.3], ("RRFB", 0.1)),
        (["RRFF", "RRFB", "RRBF"], [0.1, 0.1, 0.3], ("RRFF", 0.1)),
        (["RRFFRRFF", "RRFFRRFB", "RRFFRRBF"], [0.2, 0.1, 0.3], (
            "RRFFRRFB", 0.1)),
    ]
)
def test_calc_min_rsu_for_specific_theta_case1(
        mocker, conf_ids, mock_rsu_list, expected):
    mocker.patch(
        "rsuanalyzer.src.analyze_rsu.min_rsu.calc_rsu", 
        side_effect=mock_rsu_list
    )
    theta = 30
    delta_ = 120
    min_rsu = _calc_min_rsu_for_specific_theta(conf_ids, theta, delta_)
    assert min_rsu == expected


@pytest.mark.parametrize(
    "mock_mins, expected_ids, expected_rsus", [
        (
            [("RRFF", 0.1), ("RRFB", 0.2), ("RRBF", 0.3)], 
            ["RRFF", "RRFB", "RRBF"], [0.1, 0.2, 0.3]),
        (
            [("RRFF", 0.1), ("RRFF", 0.2), ("RRFF", 0.3)], 
            ["RRFF", "RRFF", "RRFF"], [0.1, 0.2, 0.3]),
    ]
)
def test_calc_min_rsu_for_thetas(
        mocker, mock_mins, expected_ids, expected_rsus):
    mocker.patch(
        "rsuanalyzer.src.analyze_rsu.min_rsu._calc_min_rsu_for_specific_theta", 
        side_effect=mock_mins
    )
    thetas = [10, 20, 30]
    conf_ids = ["RRFF", "RRFB", "RRBF", "RRBB"]
    delta_ = 120
    min_rsu_table = calc_min_rsu_for_thetas(conf_ids, thetas, delta_)
    assert min_rsu_table["Theta"].to_list() == thetas
    assert min_rsu_table["Ring ID"].to_list() == expected_ids
    assert min_rsu_table["RSU"].to_list() == expected_rsus
