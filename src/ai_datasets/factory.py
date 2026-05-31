# factory

from .base import dataset_info
from .tabular import TabularDataset
from .image import ImageDataset
from .text import TextDataset

class DataFactory:

    @classmethod
    def create_tabular(cls , config):

        info=dataset_info.from_dic(config=config)
        return TabularDataset(info=info,csv_path=config['path'])
    
    @classmethod
    def creat_image(cls , config):
        info=dataset_info.from_dic(config)
        return ImageDataset(info,config['path'])
    
    @classmethod
    def create_text(cls , config):
        info=dataset_info.from_dic(config)
        return TextDataset(info , config['path'])