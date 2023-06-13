import logging
import os

#  set the logging behaviour
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s '
                                               '- %(name)s:%(message)s')
logger = logging.getLogger(__name__)


class Clean:
    """
    Initialize a Clean object with the specified path.

    Args:
        path (str): The path to the folder.
    """
    def __init__(self, path):
        self.path = path
        self.total_size = 0

    def delete_folder_contents(self):
        """
        Recursively delete all files and subdirectories inside the specified
        folder with administrator privileges, and log the size of the top-most
        folder deletion.

        Note:
        - This method does not delete the root folder itself.
        - If a file or subdirectory cannot be deleted due to insufficient
        permissions, an exception will be raised.
        """
        self.total_size = self.calculate_folder_size(self.path)
        self.delete_folder(self.path)

        logger.info(f'Deleted {self.total_size} MB from the contents of: {self.path}')

    @staticmethod
    def calculate_folder_size(folder_path: str) -> float:
        """
        Recursively calculate the size of a folder.

        Args:
            folder_path (str): The path to the folder.

        Returns:
            float: The total size of the folder in megabytes (MB), rounded to
            one decimal place.
        """
        total_size = 0
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)

        # Convert bytes to megabytes
        size_in_mb = total_size / (1024 * 1024)
        size_in_mb_rounded = round(size_in_mb, 1)

        return size_in_mb_rounded

    @staticmethod
    def delete_folder(folder_path: str) -> None:
        """
        Recursively delete the contents of a folder with administrator privileges.

        Args:
            folder_path (str): The path to the folder.

        Returns:
            None
        """
        for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)
            for dirname in dirnames:
                dir_path = os.path.join(dirpath, dirname)
                os.rmdir(dir_path)
