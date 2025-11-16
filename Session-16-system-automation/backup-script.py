import os
import shutil
from datetime import datetime

# for windows
# source_dir='./'
# backup_dir='D://backups/'
# Linux/mac/ubuntu
source_dir='/home/sonam/developers'
backup_dir='/home/sonam/backup'
# Create backup diretcory if not exist
os.makedirs(backup_dir,exist_ok=True)
timestamp= datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
# backup file name
backup_file_name=f"backup-{timestamp}"
back_path=os.path.join(backup_dir,backup_file_name)
shutil.make_archive(back_path,'zip',source_dir)
print('Backup completed successfully')

