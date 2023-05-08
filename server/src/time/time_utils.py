import time
import datetime


def get_current_epoch():
    """
    Get timestamp epoch value. This should be the value stored in db.
    Convert to regular datetime based on timezone for display.
    """
    return int(time.time())


def epoch_to_datetime(timestampEpoch):
    if timestampEpoch < 0:
        raise ValueError("Invalid timestamp epoch value")
    return datetime.datetime.utcfromtimestamp(timestampEpoch)
