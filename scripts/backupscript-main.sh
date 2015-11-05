directory='Desktop/ScenarioOne8/toDoList'
backupfile="dbbackup-$(date "+%Y%m%d%H%M").bak"

echo "storing database backup into" $backupfile
ssh localuser@studvm32-p "cd $directory && sqlite3 db.sqlite3 .dump > $backupfile && scp $backupfile localuser@studvm93-p:Documents/backup && rm $backupfile"
