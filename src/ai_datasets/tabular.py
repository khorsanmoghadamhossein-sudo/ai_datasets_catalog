from .base import BaseDataset
import pandas as pd

class TabularDataset(BaseDataset):

    def __init__(self, info , csv_path):

        super().__init__(info)
        self.df=None
        self.csv_path=csv_path

    def load_data(self):

        self.df=pd.read_csv(self.csv_path)    
        return self.df
    
    def summery(self):

        if self.df is None:
            return self.load_data()
        print(self.info)
        print("shape of df: ", self.df.shape)