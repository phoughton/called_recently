import time

class CallChecker:
    
    NUMBER_OF_CALLS_NEEDED=3
    HOW_RECENT = 3
    
    def __init__(self):
        self.list_of_calls = []
    
    def called_recently(self, current_time = time):
        
        self.list_of_calls.append(current_time.time())
        checked_list = [event_time for event_time in self.list_of_calls if (current_time.time()-event_time) < self.HOW_RECENT]
        
        self.list_of_calls = checked_list

        return len(checked_list) >= self.NUMBER_OF_CALLS_NEEDED
   
    