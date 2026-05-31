from .base import BaseDataset
import pandas as pd

class TextDataset(BaseDataset):

    def __init__(self, info , data_path):

        super().__init__(info)
        self.data_path=data_path
        self.texts=[]

    def load_data(self):

        self.texts=[]

        with open(self.data_path , "r", encoding='utf-8') as f:

            lines= f.readlines()

        for line in lines:

            clean_line=line.strip()
            self.texts.append(clean_line)

        return self.texts   


    def summery(self):

        if not self.texts:

            return self.load_data()

        print(self.info)
        print("number of texts:", len(self.texts)) 

