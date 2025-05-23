import os
import logging

# 05/23/2025 04:33:34 PM hello world!
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def get_valid_path():
    """
    Prompt user for a valid path until a correct one is provided.
    """
    while True:
        path = input("Enter directory path: ")
        if os.path.isdir(path):
            return path
        else:
            logging.error("Invalid path. Please try again.")


def get_files_by_extension():
    """
    Prompt user for extension and list matching files.
    """
    path = get_valid_path()
    ext = input("Enter file extension (e.g. .exr): ").strip()

    files = [f for f in os.listdir(path) if f.endswith(ext)]

    if not files:
        logging.info("No files found with extension: %s", ext)
        return

    logging.info(f"Number of files found: {len(files)}")
    for i, filename in enumerate(sorted(files), start=1):
        print(f"{i}. {filename}")


def main():
    get_files_by_extension()


if __name__ == "__main__":
    main()
