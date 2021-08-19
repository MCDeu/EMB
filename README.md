# Electronics Monitor Board

## __Google Summer Of Code 2021__

__Welcome to Electronics Monitor Board Project__

This project is developed in a context of a scolarship in the program Google Summer Of Code 2021 and is a web application based on Django that pretends to display on the Liquid Galaxy a visualization therefore farmers can control the state and weather of their crop, analyzing atmospheric and ground magnitudes, witch has been recorded in a meteorological station made with an Arduino and external sensors that send the data to the server every 30 minutes.

<p align="center">
 <img width="700" src=Django/data/static/Logo_EMB.png>
</p>

## Source files

The application runs in a Django environment, so the files that are part of its structure will not be listed.

Below are the files that contain the core of the application and the functions needed for it to work properly

```bash
────EMB
    │   DataBase
    │   DataBase.c
    │   db.sqlite3
    │
    ├───EMB_Code_Arduino
    │     EMB_Code_Arduino.ino
    │
    └───Django
        │   app.conf
        │   requirements.txt
        │   setMasterFiles.py
        │   startDjango.py
        │
        └───data
                ConfigurationFile.py
                GenerateKML.py
                global_vars.py
                ManageData.py
                utils.py
```
- **DataBase**: Executable file to fill the database.
- **DataBase.c**: File to fill the database.
- **EMB_Code_Arduino/EMB_Code_Arduino.ino**: Arduino code to use in the meteorological stations.
- **django/app.conf**: Configuration file with customizable parameters. The parameters of this file are described below.
- **django/requirements.txt**: File with the required packages for the application to work properly.
- **django/seasight_forecasting/ConfigurationFile.py**: This file contains the initialization of the configuration file by dumping its content into global variables.
- **django/seasight_forecasting/GenerateKML.py**: This file contains the methods to create the KML file.
- **django/seasight_forecasting/global_vars.py**: This file contains a list of global variable that are filled with information from configuration file.
- **django/seasight_forecasting/ManageData.py**: This file contains the methods related to data management: filtering, data loading, data from API downloading, ...
- **django/seasight_forecasting/utils.py**: This file contains the common methods to run threads, create and send files, send FlyTo and Orbits, ...

### Configuration File
```bash
[FILES]
kml_destination_path = data/static/
kml_destination_file = destination.kml
kml_orbit_file = orbit.kml
image_destination_path = data/static/

[KML]
number_of_clusters = 200
cmap = PRGn
sleep_in_thread = 1
altitude = 15000
range = 6000000

[INSTALLATION]
server_IP = 192.168.1.105
lg_IP = lg@192.168.1.115
lg_pass = lqgalaxy
screen_for_logos = 4
project_location = Desktop/Project/
logs = False
```

- **[FILES] section**: This section includes all paths and file names of non-application data.
- **[KML] section**: This section includes the necessary parameters for the KML creation, such as the number of clusters to display, the colormap for the regions color, the time between the historic KMLs and parameters related to the altitude and the range of the FlyTo.
- **[INSTALLATION] section**: This section includes IPs of the server and the Liquid Galaxy, the screens the user wants to display the logos and colorbar and the project location folder.


## Installing / Getting started
[Install Guide](../master/docs/INSTALL.md)

### Built With
Python3, Django, Arduino.ino

## License
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/)
