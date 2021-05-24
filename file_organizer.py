import os
import shutil


def main():

    doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.xlsm', '.xlsx', '.ppt')
    img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
    software_types = ('.exe', '.pkg', '.dmg')
    
    for _, dirs, files in os.walk(".", topdown=True):
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

            #else:
            #    print('Others')
                #if not 'Others' in dirs:
                #    os.mkdir(os.path.join(start_dir,'Others'))
                #    dirs.append('Others')
                #shutil.move(file, 'Others')
        break


if __name__ == '__main__':
    main()