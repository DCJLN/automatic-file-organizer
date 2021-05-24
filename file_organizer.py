import os
import shutil
import sys


def main():

    if (len(sys.argv) != 2):
        print('Please, enter a valid number of argument (should be one, the top folder path).')
        sys.exit()
    else:
        top_dir = sys.argv[1]
        os.chdir(top_dir)

    doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.xlsm', '.xlsx', '.ppt')
    img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
    software_types = ('.exe', '.pkg', '.dmg', 'msi')
    
    try:
        for _, dirs, files in os.walk('.', topdown=True):
            for file in files:
                if file.endswith(doc_types):
                    if not 'Documents' in dirs:
                        os.mkdir('Documents')
                        dirs.append('Documents')
                    shutil.move(file, 'Documents')

                if file.endswith(img_types):
                    if not 'Images' in dirs:
                        os.mkdir('Images')
                        dirs.append('Images')
                    shutil.move(file, 'Images')

                if file.endswith(software_types):
                    if not 'Applications' in dirs:
                        os.mkdir('Applications')
                        dirs.append('Applications')
                    shutil.move(file, 'Applications')

                else:
                    if not 'Others' in dirs:
                        os.mkdir('Others')
                        dirs.append('Others')
                    shutil.move(file, 'Others')
            break
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()