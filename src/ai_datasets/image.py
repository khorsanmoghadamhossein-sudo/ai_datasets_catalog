from .base import BaseDataset
import pandas as pd

class ImageDataset(BaseDataset):

    def __init__(self, info , image_dir):
        super().__init__(info)
        self.image_dir=image_dir
        self.image_paths=[]

    def load_data(self):
        
        self.image_paths=[]  

        for f in os.listdir(self.image_dir):
               
            if f.lower().endswith((".png",".jpj")):
                    
                full_path=os.path.join(self.image_dir, f)
                self.image_paths.append(full_path)

        return self.image_paths       


    def summery(self):

        if not self.image_paths:
            self.load_data()

        print("info: ",self.info)
        print("number of images: ", len(self.image_paths))        
