import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_folder(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for file in files:
                dropbox_path = os.path.join(root,file_to)
                relative_path = os.path.relpath(dropbox_path,file_from)
                dropbox_path = "/"+file_to+"/"+relative_path
                print(dropbox_path)
                with open(file_from,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A-8VdqkC1wyJGRzMGt3Mwhdb6aV8iDYp3FmfJIe0NvcoE3WM_mlC9ukMwcRMtX5vZv0iZV_GYPDlgUCbshzV7M9_OqCesakdWO5WlhlEE3IXv_1S9P5siyVTYBkkfJaGr4otSXk'
    transferdata = TransferData(access_token)

    file_from = input("Enter Your Source Location: ")
    file_to = input("Write your Location: ")
    transferdata.upload_folder(file_from,file_to)
    print("Files uploaded successfully!")

if __name__ == '__main__':
    main()