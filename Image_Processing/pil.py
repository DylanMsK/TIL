from PIL import Image
from PIL.ExifTags import TAGS
import os


def extract_metadatas(folder_path):
    file_list = os.listdir(folder_path)
    for pic in file_list:
        path = folder_path + '/' + pic
        print('==========' + pic + '==========')
        if extract_exif(path) != None:
            GPSinfo = extract_GPS(path)
            DateTimeinfo = extract_DateTimeOriginal(path)
        else:
            pass
        print('\n')
    return None

def extract_DateTimeOriginal(file):
    try:
        print('\n- Time')
        exif = extract_exif(file)
        dateTimeOriginal = exif['DateTimeOriginal'].split()
        date = dateTimeOriginal[0].split(':')
        time = dateTimeOriginal[1].split(':')
        year, month, day = date[0], date[1], date[2]
        hour, minute, second = time[0], time[1], time[2]
        print('    Date: {}/{}/{}\n    Time: {}:{}:{}'.format(year, month, day, hour, minute, second))
        return date, time
    except:
        print('    There is no original datetime info in this picture')
        return None

def extract_GPS(file):
    try:
        print('- Loaction')
        # extrat GPS from the exif data
        exif = extract_exif(file)
        GPSInfo = exif['GPSInfo']
        latData = GPSInfo[2]
        lngData = GPSInfo[4]
        # calculate the lat/lng
        latDeg, latMin, latSec = latData[0][0] / float(latData[0][1]), latData[2][0] / float(latData[2][1]), latData[2][0] / float(latData[2][1])
        lngDeg, lngMin, lngSec = lngData[0][0] / float(lngData[0][1]), lngData[1][0] / float(lngData[1][1]), lngData[2][0] / float(lngData[2][1])
        # correct the lat/lng based on N/E/W/S
        Lat = round(latDeg + (latMin + latSec / 60.) / 60., 6)
        if GPSInfo[1] != 'N':
            Lat = Lat * -1
        Lng = round(lngDeg + (lngMin + lngSec / 60.) / 60., 6)
        if GPSInfo[3] != 'E':
            Lng = Lng * -1
        print("    Latitude: {}\n    Longitude: {}".format(Lat, Lng))
        return Lat, Lng
    except:
        print("    There is no GPS info in this picture!")
        return None

def extract_exif(file):
    extension = extension_checker(file)
    if (extension.lower() == 'jpg') | (extension.lower() == 'jpeg'):
        info = Image.open(file)._getexif()
        exif = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif[decoded] = value
        return exif
        
    else:
        print('Image format is wrong')
        return None

def extension_checker(file):
    extension = file.split('.')[-1]
    return extension

