import os, shutil

def copy_static(path, destination, delete_public=False):
    if delete_public:
        # Delete public/
        if os.path.exists(destination):
            shutil.rmtree(destination)
        os.mkdir(destination)

    dir_content = os.listdir(path)

    for file in dir_content:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, destination)
            print(file_path)
        if os.path.isdir(file_path):
            new_path = os.path.join(destination, file)
            os.mkdir(new_path)
            copy_static(file_path, new_path)




def main():
    copy_static("./static", "./public", True)


if __name__ == "__main__":
    main()