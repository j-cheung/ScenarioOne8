directory='Desktop/ScenarioOne8/toDoList'

cd Documents/backup/
backupfile=`ls -r dbbackup*.bak | sort -n -t _ -k 2 | tail -1`

echo "restoring database with" $backupfile
scp $backupfile localuser@studvm32-p:$directory
ssh localuser@studvm32-p "cd $directory && mv db.sqlite3 db.sqlite3.old && sqlite3 db.sqlite3 < $backupfile && rm $backupfile"
