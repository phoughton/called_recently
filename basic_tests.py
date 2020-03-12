import pytest
from called_recently import CallChecker
import time as clock_time
from unittest.mock import MagicMock, Mock


def test_simplist_example():
    
    recent_call_checker = CallChecker()
    
    assert recent_call_checker.called_recently() == False
    assert recent_call_checker.called_recently() == False
    assert recent_call_checker.called_recently() == True
    assert recent_call_checker.called_recently() == True
    assert recent_call_checker.called_recently() == True

    
@pytest.mark.parametrize("time_delays, expected_results", [
        ([0.0, 1.0, 2.0], [False, False, True]),
        ([0.0, 1.0, 2.99], [False, False, True]),
        ([0.0, 0.01, 0.02], [False, False, True]),
        ([0.0, 50.0, 100.0], [False, False, False]),
        ([0.0, 5.0, 10], [False, False, False]),
        ([0.0, 1.0, 3.1], [False, False, False]),
        ([0.0, 1.0, 3.1, 3.2], [False, False, False, True]),
        ([10.0, 11.0, 13.1, 13.2], [False, False, False, True])
    ])
def test_custom_times(time_delays, expected_results):
    
    now_time = clock_time.time()
    recent_call_checker = CallChecker()

    mock_time = Mock()
    
    for index in range(len(time_delays)):
        
        mock_time.time = MagicMock(return_value=now_time + time_delays[index])
        assert recent_call_checker.called_recently(mock_time) == expected_results[index], \
            f"Failed when times were: {recent_call_checker.list_of_calls}, and we just sent: {mock_time.time()}. " + \
            f"The full list of times sent was: {time_delays} and expected results was: {expected_results}"
