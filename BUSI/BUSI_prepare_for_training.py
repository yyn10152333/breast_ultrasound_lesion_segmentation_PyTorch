import zipfile
from google_drive_downloader import GoogleDriveDownloader as gdd
import os

# os.rename('BUSI/BUSI_train_complete', 'BUSI/BUSI_train')

gdd.download_file_from_google_drive(file_id='Dataset_BUSI_with_GT',
                                    dest_path='./BUSI/BUSI.zip',
                                    unzip=True)

os.rename('BUSI/BUSI', 'BUSI/BUSI_train')
