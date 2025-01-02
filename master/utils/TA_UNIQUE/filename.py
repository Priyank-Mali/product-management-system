import uuid
import os

def generate_unique_filename(instance,filename):
    extension = filename.split(".")[-1]
    new_filename = f'{str(uuid.uuid4())}_{instance.SUFFIX_WORD}.{extension}'

    return os.path.join(instance.DIR_NAME,new_filename)
