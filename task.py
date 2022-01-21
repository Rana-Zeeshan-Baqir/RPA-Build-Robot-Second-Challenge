from libraries.challenge import Title
from config import OUTPUT, create_dir

def main():
    title_obj = Title()
    title_obj.dialog()
    title_obj.read_file()
    title_obj.open_browser()
    title_obj.order_robot()
    title_obj.archive()


if __name__ == "__main__":
    create_dir(OUTPUT)
    main()
