import zipfile
from google_drive_downloader import GoogleDriveDownloader as gdd
import os

# os.rename('BUSI/BUSI_train_complete', 'BUSI/BUSI_train')

gdd.download_file_from_google_drive(file_id='Dataset_BUSI.zip',
                                    dest_path='./BUSI/Dataset_BUSI.zip',
                                    unzip=True)

os.rename('BUSI/Dataset_BUSI_with_GT', 'BUSI/BUSI_train')
