# MQTT-Subscribe-Publish-IoT
The scope of this project is to demonstrate the functionality of IoT message exachange MQTT protocol. 

####Project Structure:  
├── publish  
├── subscribe  
├── docker-compose.yaml  
├── requirements.txt  
└── README.md  

This application can run locally but can be deployed as well because is fully dockerized:
####Run Local:
It works for python 3.6
1. Install requrements:  
`pip install -r requirements.txt`  
2. Run python files:  
`python publish/publish_topic.py`  
`python subscribe/subscribe_topic.py`

####Deploy using docker compose to build the images and run the containers:  
1. Attached Mode: `docker-compose build && docker-compose up`
2. Detached mode:  `docker-compose build && docker-compose up -d`

Check that docker images are running using the command:  
`docker ps`


    
