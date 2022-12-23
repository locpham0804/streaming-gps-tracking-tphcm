# streaming-gps-tracking-tphcm

## Tech

Simple use of kafka to create real time tracking GPS.

![GPS_Tracking_pipeline](/gps_pipeline.PNG)

## Features

Web UI with display unit details and filter unit for each services.

![GPS_Tracking_gif](/gps_track.gif)

## Installation

Install the kafka

At the root folder

```
docker-compose up
```

Install dependencies

```
cd python
pip install -r requirements.txt
```

## Start the app

Inside the python directory, open a terminal and run:
```
python3 app_tphcm.py
```

Open another terminal and run:
```
python3 kafka_stream_producer_tphcm_motorbike.py
```
