import sqlite3

con = sqlite3.connect('Django/db.sqlite3')
cur = con.cursor()

Id_station = '01000001'
day = '2021-05-01 00:00:00'

for row in cur.execute("SELECT temperature FROM data_data WHERE id_station_id = ? AND day = ?", (Id_station, day,)):
        temp = row[0]
        
for row in cur.execute("SELECT press FROM data_data WHERE id_station_id = ? AND day = ?", (Id_station, day,)):
    pres = row[0]

for row in cur.execute("SELECT rain FROM data_data WHERE id_station_id = ? AND day = ?", (Id_station, day,)):
    rainn = row[0]

for row in cur.execute("SELECT air_humidity FROM data_data WHERE id_station_id = ? AND day = ?", (Id_station, day,)):
    air = row[0]

for row in cur.execute("SELECT wind_speed FROM data_data WHERE id_station_id = ? AND day = ?", (Id_station, day,)):
    speed = row[0]
  
for row in cur.execute("SELECT wind_direction FROM data_data WHERE id_station_id = ? AND day = ?", (Id_station, day,)):
    direction = row[0]

data = [temp, pres, rainn, air, speed, direction]
print(data)
