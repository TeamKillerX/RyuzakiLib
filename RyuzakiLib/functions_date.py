# The MIT License (MIT)
# Copyright (c) 2022 penggrin

# meta developer: @penggrinmods
# scope: hikka_only
# requires: python-dateutil

import time
from datetime import datetime

import numpy as np
from dateutil.relativedelta import relativedelta

data = {
    "7117444122": 1723429195,
    "6602485156": 1723148395,
    "5396587273": 1648014800,
    "5336336790": 1646368100,
    "4317845111": 1620028800,
    "3318845111": 1618028800,
    "2018845111": 1608028800,
    "1919230638": 1598028800,
    "755000000": 1548028800,
    "782000000": 1546300800,
    "727572658": 1543708800,
    "616816630": 1529625600,
    "391882013": 1509926400,
    "400169472": 1499904000,
    "369669043": 1492214400,
    "234480941": 1464825600,
    "200000000": 1451606400,
    "150000000": 1434326400,
    "10000000": 1413331200,
    "7679610": 1389744000,
    "2768409": 1383264000,
    "1000000": 1380326400,
}

class UserDateEstimator:
    def __init__(self, order=3):
        self.order = order
        self.x, self.y = self._unpack_data()
        self._func = self._fit_data()

    def _unpack_data(self):
        x_data = np.array(list(map(int, data.keys())))
        y_data = np.array(list(data.values()))
        return x_data, y_data

    def _fit_data(self):
        fitted = np.polyfit(self.x, self.y, self.order)
        return np.poly1d(fitted)

    def func(self, tg_id: int):
        # Check if tg_id exists in the data
        if str(tg_id) in data:
            return data[str(tg_id)]  # Return exact value if found
        value = self._func(tg_id)
        if value > time.time():
            value = time.time()
        return value

    def time_format(self, unix_time):
        formatted_date = datetime.utcfromtimestamp(unix_time).strftime("%Y-%m-%d %H:%M:%S")
        d = relativedelta(datetime.now(), datetime.utcfromtimestamp(unix_time))
        age = f"{d.years} year{'s' if d.years != 1 else ''}, {d.months} month{'s' if d.months != 1 else ''}, {d.days} day{'s' if d.days != 1 else ''}"
        return formatted_date, age
