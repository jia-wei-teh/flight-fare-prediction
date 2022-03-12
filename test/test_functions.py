from helper_functions import convert_duration_to_minute


def test_convert_duration_to_minute_normal():
    assert convert_duration_to_minute("2h 30m") == 150
    assert convert_duration_to_minute("1h 30m") == 90


def test_convert_duration_to_minute_missing_hour():
    assert convert_duration_to_minute("1h") == 60


def test_convert_duration_to_minute_missing_minute():
    assert convert_duration_to_minute("30m") == 30


def test_convert_duration_to_minute_empty():
    assert convert_duration_to_minute("") == 0
