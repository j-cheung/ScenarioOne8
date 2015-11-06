sudo systemctl stop httpd

cd ~/Desktop/ScenarioOne8
git pull
cp ~/Desktop/ScenarioOne8/scripts/pullUpdatesStaging.sh ~/


sudo systemctl start httpd