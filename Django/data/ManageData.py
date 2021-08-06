import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

def GetDate(day, hour, minute):
    date = day + "T" + hour + minute
    return date


"""
def GetIdFromCity(city):
    for row in cur.execute("SELECT id_station FROM data_arduino WHERE region = ?", (city))
    
    return row[0]
    
def GetCoordinatesFromId(Id_station):
    for row in cur.execute("SELECT coordinates FROM data_arduino WHERE id_station = ?", Id_station)
    
    return row[0]
 


def GetDataFromId(Id_station, day):
    for row in cur.execute("SELECT temperature FROM data_data WHERE id_station_id = ? AND day = ?", Id_station, day)
        temp = int(row[0])
        
    for row in cur.execute("SELECT press FROM data_data WHERE id_station_id = ? AND day = ?", Id_station, day)
        pres = int(row[0])
    
    for row in cur.execute("SELECT rain FROM data_data WHERE id_station_id = ? AND day = ?", Id_station, day)
        rainn = int(row[0])
    
    for row in cur.execute("SELECT air_humidity FROM data_data WHERE id_station_id = ? AND day = ?", Id_station, day)
        air = int(row[0])
    
    for row in cur.execute("SELECT wind_speed FROM data_data WHERE id_station_id = ? AND day = ?", Id_station, day)
        speed = int(row[0])
      
    for row in cur.execute("SELECT wind_direction FROM data_data WHERE id_station_id = ? AND day = ?", Id_station, day)
        direction = int(row[0])

    data = [temp, pres, rainn, air, speed, direction]
    
    return data
"""
