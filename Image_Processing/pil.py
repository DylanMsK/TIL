from PIL import Image
from PIL.ExifTags import TAGS


def extract_metadata(file):
    extension = file.split('.')[-1]
    if (extension.lower() == 'jpg') | (extension.lower() == 'jpeg'):
        img = Image.open(file)
        info = img._getexif()
        exif = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif[decoded] = value
        try:
            # extrat GPS from the exif data
            exifGPSInfo = exif['GPSInfo']
            latData = exifGPSInfo[2]
            lngData = exifGPSInfo[4]
            # calculate the lat/lng
            latDeg = latData[0][0] / float(latData[0][1])
            latMin = latData[1][0] / float(latData[1][1])
            latSec = latData[2][0] / float(latData[2][1])
            lngDeg = latData[0][0] / float(latData[0][1])
            lngMin = latData[1][0] / float(latData[1][1])
            lngSec = latData[2][0] / float(latData[2][1])
            # correct the lat/lng based on N/E/W/S
            Lat = round(latDeg + (latMin + latSec / 60.) / 60., 6)
            if exifGPSInfo[1] != 'N':
                Lat = Lat * -1
            Lng = round(lngDeg + (lngMin + lngSec / 60.) / 60., 6)
            if exifGPSInfo[3] != 'E':
                Lng = Lng * -1
            print("Latitude: {}, Longitude: {}".format(Lat, Lng))
        except:
            print("There is no GPS info in this picture!")
        
        try:
            exifDateTimeOriginal = exif['DateTimeOriginal'].split()
            date = exifDateTimeOriginal[0].split(':')
            time = exifDateTimeOriginal[1].split(':')
            year = date[0]
            month = date[1]
            day = date[2]
            hour = time[0]
            minute = time[1]
            second = time[2]
            print('Year: {}\nMonth: {}\nDay: {}\nHour: {}\nMinute: {}\nSecond: {}'.format(year, month, day, hour, minute, second))
        except:
            print('There is no DateTime info in this picture')
        
    else:
        print('Image format is wrong')
    print('Done')


    print(extract_metadata('20170712_201505.jpg'))