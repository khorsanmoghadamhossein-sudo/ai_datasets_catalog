import sys
from pathlib import Path 

base_path=Path(__file__).resolve().parent
src_dir=base_path/"src"

sys.path.append(str(src_dir))

def main():
    from ai_datasets import DataFactory

    config={
        "name":"penguin",
        "task_type":"multi class",
        "target_col":"species",
        "source":"kaggle",
        "path":r"D:\Doreh_AI\Advanced python for AI\j6\ai_datasets_catalog\data\raw\penguins.csv"
    }

    penguin_dataset=DataFactory.create_tabular(config=config)

    print(penguin_dataset.summery())

if __name__=="__main__":

    main()