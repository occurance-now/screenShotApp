import math

def change_direction(cycle, current_direction):
    direction = ['east','north','west','south']

    if cycle == 0:
        current_direction = direction[cycle]
        cycle += 1
    elif cycle < 3:
        current_direction = direction[cycle]
        cycle += 1
    else:
        current_direction = direction[cycle]
        cycle = 0

    return cycle, current_direction

def get_coords(current_direction, latitude, longitude):
    df = 2/69

    if current_direction == 'east':
        dl = round((df / (math.cos(math.radians(latitude)))), 3)
        longitude= round((longitude + dl), 7)
    elif current_direction == 'north':
        latitude = round((latitude + df), 7)
    elif current_direction == 'west':
        dl = round((df / (math.cos(math.radians(latitude)))), 3)
        longitude = round((longitude - dl), 7)
    elif current_direction == 'south':
        latitude = round((latitude - df), 7)
    else:
        print('something went wrong')

    return latitude, longitude

def spiral(X, Y, latitude, longitude):
    #grid setup
    x = y = 0
    dx = 0
    dy = -1

    #Lat/Lon setup
    cycle = 0
    current_direction = 'east'
    latitude = 8.393900 #f
    longitude = -83.139217 #l
    coords = []
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            #print (x, y)
            if x == 0 and y == 0:
                lat_long = (latitude, longitude)
                coords.append(lat_long)
                #print("latitude: " + str(latitude), "longitude: " + str(longitude))
            else:
                latitude, longitude = get_coords(current_direction, latitude, longitude)
                lat_long = (latitude, longitude)
                coords.append(lat_long)
                #print("latitude: " + str(latitude), "longitude: " + str(longitude))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
            cycle, current_direction = change_direction(cycle, current_direction)
            #print(current_direction)
        x, y = x+dx, y+dy


    return coords

if __name__ == "__main__":
    print("Called when executing just this file")
# photo_total = 9 #Grid size variable
# X = Y = int(math.sqrt(photo_total))
# starting_latitude = 8.393900
# starting_longitude = -83.139217
# coordinates = spiral(X, Y, starting_latitude, starting_longitude)
#
# print(coordinates)
