sudo systemctl stop httpd

cd ~/Desktop/ScenarioOne8
git pull
cp ~/Desktop/ScenarioOne8/scripts/pullUpdates.sh ~/

ssh localuser@studvm93-p "sh restorescript-main.sh" 

sudo systemctl start httpd