import os
import shutil


def move_file(command: str) -> None:
    if not command:
        return

    _, source, destination = command.split(" ")

    destination_dir = os.path.dirname(destination)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    shutil.copy(source, destination)
    os.remove(source)
