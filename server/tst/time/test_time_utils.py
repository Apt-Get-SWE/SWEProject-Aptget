from ...src.time.time_utils import get_current_epoch, epoch_to_datetime
import pytest


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
