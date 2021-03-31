import pandas as pd


class DataConverter:
    def __init__(self, values, columns):
        self._data = pd.DataFrame(values, columns=columns)
        self._prepare_data()

    def _prepare_data(self):
        self._data['Points'] = self._data['Points'].apply(lambda x: int(x))
        self._data['Speed'] = self._data['Speed'].apply(lambda x: int(x[:-4]))
        self._data['Accuracy'] = self._data['Accuracy'].apply(lambda x: float(x[:-1]))
        self._data['Race #'] = self._data['Race #'].apply(lambda x: int(x))
        self._data = self._data.set_index('Race #')
        self._data = self._data.sort_index()

    def get_data(self):
        return self._data

    def plot(self):
        import matplotlib.pyplot as plt
        self._data.rolling(10).mean().plot()
        plt.show()
        self._data['Points'].plot()