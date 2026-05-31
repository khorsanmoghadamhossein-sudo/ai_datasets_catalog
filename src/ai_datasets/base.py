class dataset_info:

    count=0 # class variables

    def __init__(self,name,target_col,task_type,path, source=None):

        self.name = name
        self.task_type = task_type
        self.target_col = target_col
        self.source = source
        self.path=path

        dataset_info.count+=1


    @classmethod
    def from_dic(cls , config):

        return cls(

            name=config['name'],
            task_type=config['task_type'],
            target_col=config['target_col'],
            source=config.get("source"),
            path=config['path']
        )



    def __str__(self):
        return f"name: {self.name}  , task_type: {self.task_type}, target: {self.target_col} , source: {self.source} , path: {self.path}"   


class dataset_Util:

    @staticmethod
    def is_large(n_rows,limit=50000):
        return n_rows>limit
    
    @staticmethod
    def is_classification(task_type):
        return "classification" in task_type
    

class BaseDataset:

    def __init__(self,info):
        
        self.info=info

    def summery(self):

        print("general info:", self.info)    