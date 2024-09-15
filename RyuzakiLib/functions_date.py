import numpy as np
from datetime import datetime, timedelta

class UserDateEstimator:
    def __init__(self):
        self.user_data = {
            1000000000: datetime(2019, 1, 1),
            1100000000: datetime(2020, 1, 1),
            1191668125: datetime(2020, 6, 15)
        }
        
        self.user_ids = np.array(list(self.user_data.keys()))
        self.timestamps = np.array([dt.timestamp() for dt in self.user_data.values()])
        self.poly = np.poly1d(np.polyfit(self.user_ids, self.timestamps, 1))
        
    def estimate_registration_date(self, user_id):
        estimated_timestamp = self.poly(user_id)
        estimated_date = datetime.utcfromtimestamp(estimated_timestamp)
        return estimated_date.strftime("%B %Y")
