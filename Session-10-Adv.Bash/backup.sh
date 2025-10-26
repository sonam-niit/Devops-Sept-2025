SOURCE_DIR=/home/sonam/developers

BACKUP_DIR=myapp
ARCHIVE_FILE="app_backup.tar.gz"

mkdir -p "$BACKUP_DIR"

## Create Compressed File
tar -czf "$BACKUP_DIR/$ARCHIVE_FILE" -C "$SOURCE_DIR" .

echo "Backup created successfully $BACKUP_DIR/$ARCHIVE_FILE" 