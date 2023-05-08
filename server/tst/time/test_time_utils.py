from ...src.time.time_utils import get_current_epoch, epoch_to_datetime
import pytest
from unittest.mock import patch
import datetime


class TestTimeUtils:
    @pytest.fixture
    def get_test_epoch(self):
        return 40246871

    def test_get_current_epoch(self):
        timestampEpoch1 = get_current_epoch()
        timestampEpoch2 = get_current_epoch()
        assert timestampEpoch1 <= timestampEpoch2

    def test_epoch_to_datetime(self, get_test_epoch):
        timestampEpoch = get_test_epoch
        date_time = epoch_to_datetime(timestampEpoch)
        assert date_time.year == 1971
        assert date_time.month == 4
        assert date_time.day == 11
        assert date_time.hour == 19
        assert date_time.minute == 41

    def test_epoch_to_datetime_min_max(self):
        min_epoch = 0
        max_epoch = 2**32 - 1
        min_date_time = epoch_to_datetime(min_epoch)
        max_date_time = epoch_to_datetime(max_epoch)
        assert min_date_time == datetime.datetime(1970, 1, 1, 0, 0)
        assert max_date_time == datetime.datetime(2106, 2, 7, 6, 28, 15)

    def test_epoch_to_datetime_invalid_value(self):
        with pytest.raises(ValueError):
            epoch_to_datetime(-1)

    @patch('time.time', return_value=1620290400)
    def test_get_current_epoch_mocked_time(self, _):
        timestampEpoch = get_current_epoch()
        assert timestampEpoch == 1620290400

    @patch('time.time', side_effect=[1620290400, 1620290410])
    def test_get_current_epoch_mocked_time_passing(self, _):
        timestampEpoch1 = get_current_epoch()
        timestampEpoch2 = get_current_epoch()
        assert timestampEpoch1 < timestampEpoch2
        assert timestampEpoch2 - timestampEpoch1 == 10
