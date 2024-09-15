import json
import pathlib
from typing import Callable
import time
from datetime import datetime
import numpy as np

class FunctionDate:
    def __init__(self, order: int = 3):
        self.order = order
        self.data_path = pathlib.Path.cwd().joinpath("dates.json")

        self.x, self.y = self._unpack_data()
        self._func = self._fit_data()

    def _unpack_data(self) -> (np.ndarray, np.ndarray):
        with open(self.data_path) as string_data:
            data = json.load(string_data)

        x_data = np.array(list(map(int, data.keys())))
        y_data = np.array(list(data.values()))

        return (x_data, y_data)

    def _fit_data(self) -> Callable[[int], float]:
        fitted = np.polyfit(self.x, self.y, self.order)
        func = np.poly1d(fitted)
        return func

    def add_datapoint(self, pair: tuple):
        with open(self.data_path) as string_data:
            data = json.load(string_data)
        data[str(pair[0])] = pair[1]
        with open(self.data_path, "w") as string_data:
            json.dump(data, string_data)
        self.x, self.y = self._unpack_data()
        self._func = self._fit_data()

    def func(self, tg_id: int) -> float:
        value = self._func(tg_id)
        current = time.time()
        if value > current:
            value = current
        return value
