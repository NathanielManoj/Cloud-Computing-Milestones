from google.cloud import pubsub_v1      # pip install google-cloud-pubsub  ##to install
import glob                             # for searching for json file 
import json
import os 
import csv                            # for reading csv file

# Search the current directory for the JSON file (including the service account key) 
# to set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
files=glob.glob("*.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=files[0];

# Set the project_id with your project ID
project_id="modified-badge-485416-p7";
topic_name = "Design";   # change it for your topic name if needed

# create a publisher and get the topic path for the publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
print(f"Published messages with ordering keys to {topic_path}.")

#read CSV file and
with open('Labels.csv', mode ='r')as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # convert the string to bytes (serialization)
        message=str(row).encode('utf-8')

        # send the value
        print("Producing a record: {}".format(message))    
        future = publisher.publish(topic_path, message);
    
    #ensure that the publishing has been completed successfully
        future.result()