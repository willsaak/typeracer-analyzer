import pandas as pd


class DataConverter:
    def __init__(self, data):
        self._data = pd.DataFrame(data)

    def _prepare_data(self):
        pass

    def get_data(self):
        return self._data

    def plot(self):
        import matplotlib.pyplot as plt
        self._data.rolling(10).mean().plot()
        plt.show()
        self._data['Points'].plot()
