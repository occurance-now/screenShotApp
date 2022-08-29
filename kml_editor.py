import re


def write_new_kml(latitude, longitude):
    filename = 'coords/coords1.kml'

    #write new latitude
    with open(filename, 'r+') as f:
        filetext= f.read()
        f.seek(0)
        f.write(re.sub(r'<latitude>.*?</latitude>',f'<latitude>{latitude}</latitude> ',filetext))
        f.truncate()
        f.close()

    #write new longitude
    with open(filename, 'r+') as f:
        filetext= f.read()
        f.seek(0)
        f.write(re.sub(r'<longitude>.*?</longitude>',f'<longitude>{longitude}</longitude> ',filetext))
        f.truncate()
        f.close()

#write_new_kml(latitude, longitude)

if __name__ == "__main__":
    print("Called when executing just this file")
    latitude = 9
    longitude = -90
