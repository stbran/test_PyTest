# This test checks difference between local computer time and NTP-server time.
# Test is considered passed if difference is no more than 2 seconds.

import datetime
import ntplib

def test_checking_time():
    local_time = datetime.datetime.now().time()
    local_time_convert = datetime.timedelta(hours=local_time.hour, minutes=local_time.minute, seconds=local_time.second)

    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    server_time = datetime.datetime.fromtimestamp(response.tx_time)
    server_time_convert = datetime.timedelta(hours=server_time.hour, minutes=server_time.minute, seconds=server_time.second)
    assert (server_time.hour - local_time.hour == 0 and server_time.minute - local_time.minute == 0 and abs(server_time.second - local_time.second) <= 2), "It's wrong local time"
