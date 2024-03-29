import pytest

from reprod.rsuanalyzer.analyze_rsu.small_rsu_ranking import \
    create_small_rsu_ranking


@pytest.mark.parametrize(
    "top_num, mock_rsus, expected_ids, expected_rsus", [
        (
            3, [0.2, 0.1, 0.3, 0.4], ["RRFB", "RRFF", "RRBF"], [0.1, 0.2, 0.3]),
        (
            2, [0.2, 0.1, 0.3, 0.4], ["RRFB", "RRFF"], [0.1, 0.2]),
        (
            2, [0.3, 0.1, 0.2, 0.4], ["RRFB", "RRBF"], [0.1, 0.2]),
    ]
)
def test_create_small_rsu_ranking(mocker, top_num, mock_rsus, expected_ids, expected_rsus):
    mocker.patch(
        "reprod.rsuanalyzer.analyze_rsu.small_rsu_ranking.calc_rsu",
        side_effect=mock_rsus
    )
    ring_ids = ["RRFF", "RRFB", "RRBF", "RRBB"]
    theta = 30
    delta_ = 120
    rank_table = create_small_rsu_ranking(ring_ids, theta, delta_, top_num)
    assert rank_table["Ring ID"].to_list() == expected_ids
    assert rank_table["RSU"].to_list() == expected_rsus
