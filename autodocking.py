import pyautogui
import os, time


'''
This script automatically clicks the buttons in Hermes to run the docking
of beta tubulin subunits to ivermectin. Hermes GUI needs to be opened prior to 
running the program.
'''


current_frame = 125
last_frame = 167

def modify_config(n):
    cf = str(n)
    with open('gold.conf', 'r', encoding='utf-8') as config:
        data = config.readlines()
        data[30] = 'directory = C:/Users/Koneko/Desktop/doki_docking/' + 'tubulin_no_water/results/frame' + cf + '\n'
        data[79] = 'protein_datafile = C:/Users/Koneko/Desktop/' + 'doki_docking/tubulin_no_water/frame' + cf + '.pdb\n'
    
    with open('gold.conf', 'w', encoding='utf-8') as config:
        config.writelines(data)

def start_docking():
    pyautogui.leftClick(477, 40) # GOLD context menu
    pyautogui.leftClick(505, 65)  # setup and run a docking
    pyautogui.leftClick(1040, 557) # load existing
    pyautogui.leftClick(615, 86)
    pyautogui.write("C:\\Users\\Koneko\\Desktop\\doki_docking\\tubulin_no_water")
    pyautogui.press('enter')
    pyautogui.leftClick(732, 583)
    pyautogui.leftClick(726, 238)      # ID
    pyautogui.leftClick(1241, 317)    # Add hydrogens
    time.sleep(5)
    pyautogui.leftClick(999, 551)       # OK
    pyautogui.leftClick(896, 874)       # Run GOLD
    pyautogui.leftClick(979, 345)       # directory selection
    pyautogui.doubleClick()
    pyautogui.write("C:\\Users\\Koneko\\Desktop\\doki_docking\\tubulin_no_water\\results\\frame" + str(current_frame))
    pyautogui.leftClick(804, 486)       # click outside text box
    pyautogui.leftClick(912, 700)       # Save
    pyautogui.leftClick(1044, 551) 
    time.sleep(2)
    pyautogui.leftClick(1044, 551) # Start the docking
    
def cleanup():
    pyautogui.leftClick(1056, 750) # Close
    pyautogui.leftClick(1175, 872) # Finish
    pyautogui.leftClick(784, 547) # Checkbox
    pyautogui.leftClick(922, 700) # Save
    pyautogui.leftClick(1050, 546) # OK
    time.sleep(1)
    pyautogui.leftClick(1050, 546)
    time.sleep(1)
    pyautogui.rightClick(53, 285)
    pyautogui.leftClick(140, 480)
    

    
while current_frame <= last_frame:
    modify_config(current_frame)
    start_docking()
    time.sleep(1500)
    cleanup()
    current_frame += 1
        