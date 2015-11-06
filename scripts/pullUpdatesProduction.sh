sudo systemctl stop httpd

cd ~/Desktop/ScenarioOne8
git pull
cp ~/Desktop/ScenarioOne8/scripts/pullUpdatesProduction.sh ~/

ssh localuser@studvm93-p "sh restorescript-main.sh" 

sudo systemctl start httpd