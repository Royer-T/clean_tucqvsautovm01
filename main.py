import logging

#  import packages (modules/classes)
from cleanup.deletion import Clean

# constants
import constants

#  create and configure logger
log_file = constants.LOG_FILE
log_path = f'{constants.LOGDIRECTORY}/{log_file}'

logging.basicConfig(filename=log_path,
                    level=logging.DEBUG,
                    filemode='a',
                    force=True,
                    format='%(asctime)s - %(levelname)s - '
                           '%(name)s:%(message)s')


def delete_clean(cleanup_obj: Clean) -> None:
    """
    Delete the contents of a folder using the provided cleanup object.

    Args:
        cleanup_obj (Clean): An instance of the Clean class representing the
        folder to be cleaned.

    Returns:
        None
    """
    cleanup_obj.delete_folder_contents()


def main() -> None:
    """
    Main function that performs cleanup operations for different folders using
    the Clean class and delete_clean function.
    """
    logintimes = Clean(constants.LOGINTIMES)
    delete_clean(logintimes)

    connect = Clean(constants.CONNECT)
    delete_clean(connect)

    commonui = Clean(constants.COMMONUI)
    delete_clean(commonui)

    automationparent = Clean(constants.AUTOMATIONPARENT)
    delete_clean(automationparent)

    htcmobileapp = Clean(constants.HTCMOBILEAPP)
    delete_clean(htcmobileapp)


if __name__ == '__main__':
    main()
