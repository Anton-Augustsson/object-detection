import os
import typer
from typing import Optional
from typing_extensions import Annotated

from typing import List
from scripts.data_collection.partition import partition_dataset, delete_partition_dataset
from scripts.data_collection.create_label_map import create_label_map

app = typer.Typer()

#@app.command()
#def partition_data_set(name: str):
#    file_pairs = []
#    for label in labels:
#        path = os.path.abspath(os.path.join(IMAGES_PATH, label))
#        file_pairs = file_pairs + get_file_pairs(path)
#    random_copy(file_pairs, train_path, test_path, 0.2)


@app.command()
def cmd_capture_images(name: str):
    """
    Starts OpenCV and automatically takes images while you orient 
    the objet in different angels.
    """
    print(f"Hello {name}")


@app.command()
def cmd_data_partition(ratio: float = typer.Argument(default=0.2) ):
    """
    """
    partition_dataset(ratio)


@app.command()
def cmd_data_partition_delete():
    """
    """
    delete_partition_dataset()


@app.command()
def cmd_generate_tfrecord(name: str):
    """
    """
    print(f"Hello {name}")


@app.command()
def cmd_create_label_map(label_names: List[str]):
    """
    Creates label_map.pbtxt file in annotations with the labels you entered.
    """
    # FIXME: does order matter?
    # TODO: change to generate label map
    create_label_map(label_names)

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
