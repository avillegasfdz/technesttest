pip install Flask
pip install requests
sudo apt install python3-flask

cd oddsum_project/src/oddsum
sh run_service.sh &
cd ../../..

cd process_project/src/process
sh run_service.sh &
cd ../../..
