from pykafka import KafkaClient
import json
from datetime import datetime
import uuid
import time

#READ COORDINATES FROM GEOJSON
input_file = open('./data/tphcm/data_tphcm_motorbike.json')
json_array = json.load(input_file)
coordinates = json_array['data']

#GENERATE UUID
def generate_uuid():
    return uuid.uuid4()

#KAFKA PRODUCER
client = KafkaClient(hosts="127.18.0.3:29092")
topic = client.topics['geodata_stream_topic_123']
producer = topic.get_sync_producer()

#CONSTRUCT MESSAGE AND SEND IT TO KAFKA
data = {}
data['service'] = 'alpha'

def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):
        data['key'] = data['service'] + '_' + str(generate_uuid())
        data['datetime'] = str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        data['unit'] = coordinates[i]['unit']
        data['latitude'] = coordinates[i]['coordinates'][0]
        data['longitude'] = coordinates[i]['coordinates'][1]
        data['color'] = coordinates[i]['color']
        message = json.dumps(data)
        print(message)
        producer.produce(message.encode('ascii'))
        time.sleep(1)

        #if bus reaches last coordinate, start from beginning
        if i == len(coordinates)-1:
            i = 0
        else:
            i += 1

generate_checkpoint(coordinates)
