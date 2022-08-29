
import pyautogui
import time
import subprocess
from coord_algo import spiral, math
from kml_editor import write_new_kml


#Open gEarth and close popup window
def load_g_earth(g_earth_exe):
    subprocess.Popen([g_earth_exe])
    pyautogui.moveTo(1980, 1311, duration=1)
    time.sleep(5)
    pyautogui.click(1980, 1311)
    time.sleep(2)
#Open KML file
def open_kml(kml_directory):
    try:
        pyautogui.moveTo(40, 5, duration = 0)#click out of terminal
        time.sleep(1)
        pyautogui.click(40, 5)
        pyautogui.hotkey("ctrlleft", "o")#open file explorer
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "l")#file explorer path hotkey
        time.sleep(1)
        pyautogui.write(kml_directory, interval=0.1)#type file directory
        time.sleep(1)
        pyautogui.typewrite(['enter'])
        time.sleep(1)

        #Close File explorer
        pyautogui.hotkey("ctrlleft", "f")#switch to file explorer window
        pyautogui.press(['esc'])#close filer explorer
        pyautogui.press(['esc'])#close filer explorer

        print('Successfully opened KML file')
    except Exception as e:
        print(e)
#Load Screen Shot settings !!!Only on first round!!!
def load_settings_file():
    screen_shot_settings = 'Desktop\ScreenShotApp\mapOptions'
    settings_file = 'settings.geprint'
    try:
        pyautogui.click(552, 164)#map options button
        time.sleep(.5)
        pyautogui.click(813, 862)#Load button
        time.sleep(.5)
        pyautogui.hotkey("ctrlleft", "l")#file explorer path hotkey
        time.sleep(.5)
        pyautogui.write(screen_shot_settings, interval=0.1)#go to file directory
        pyautogui.press(['enter'])
        pyautogui.hotkey("altleft", "d")#file explorer path hotkey
        pyautogui.press(['enter'])
        pyautogui.press(['enter'])
        pyautogui.write(settings_file, interval=0.1)#type file name
        pyautogui.press(['enter'])
        time.sleep(.5)
        pyautogui.click(1135, 931)
        pyautogui.press(['enter'])#exit popup
        print('[+] successfully set screen shot settings')
    except Exception as e:
        print(e)

def save_image(loop_counter):
    images_dir =  'Desktop\ScreenShotApp\sat_photos'
    sat_photo = 'sat_photo'
    try:
        pyautogui.moveTo(1145, 162, duration = 0)#click out of terminal
        time.sleep(2)
        pyautogui.click(1145, 162)
        time.sleep(2)
        pyautogui.hotkey("ctrlleft", "l")#file explorer path hotkey
        time.sleep(2)
        if loop_counter == 1:
            pyautogui.write(images_dir, interval=0.1)#go to sat_photo directory
            pyautogui.press(['enter'])
            pyautogui.click(850, 943)
            pyautogui.write(sat_photo+str(loop_counter), interval=0.1)#write file name
            pyautogui.press(['enter'])
        elif loop_counter > 1:
            pyautogui.click(850, 943)
            pyautogui.write(sat_photo+str(loop_counter), interval=0.1)#write file name
            pyautogui.press(['enter'])
        else:
            print('[-] something went wrong')
    except Exception as e:
        print(e)

def save_image_loop(loop_counter):
    try:
        time.sleep(5)
        pyautogui.moveTo(1145, 162, duration = 0)
        pyautogui.click(1145, 162)
        with pyautogui.hold('ctrlleft'):
            pyautogui.hotkey('alt', 's')

        time.sleep(2)
        if loop_counter == 1:
            load_settings_file()
            save_image(loop_counter)
            print(f'[+]Image: {loop_counter} successfully saved')
        elif loop_counter > 1:
            save_image(loop_counter)
            print(f'[+] Image: {loop_counter} successfully saved')
        else:
            print("[-] something went wrong, see save_image_loop")

        print("[+] Capture saved")

    except Exception as e:
        print(e)

#Track mouse function for testing
def track_mouse():
    try:
        while True:
            currentMouseX, currentMouseY = pyautogui.position()
            print(currentMouseX, currentMouseY)
            time.sleep(2)
    except KeyboardInterrupt:
        print('interrupted!')


def run_gearth_logic(coordinates):
    g_earth_exe = "C:\Program Files\Google\Google Earth Pro\client\googleearth.exe"
    kml_directory = 'Desktop\ScreenShotApp\coords\coords1'

    #track_mouse()
    #load_g_earth(g_earth_exe)
    for i in (coordinates):
        latitude = i[0]
        longitude = i[1]
        loop_counter = 1

        #Build KML
        #write_new_kml(latitude, longitude)
        #open_kml(kml_directory)
        save_image_loop(loop_counter)
        loop_counter += 1
        break

#Get Coordinate List
photo_total = 9 #Grid size variable
X = Y = int(math.sqrt(photo_total))
starting_latitude = 8.393900
starting_longitude = -83.139217
coordinates = spiral(X, Y, starting_latitude, starting_longitude)

run_gearth_logic(coordinates)
