from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import csv

# create the driver, navigate to IC, and wait for the user to get to the correct screen
driver = webdriver.Chrome()
driver.get("https://trumbullct.infinitecampus.org/campus/trumbull.jsp")

input("Press Enter To Select Values")
loop = True

while (loop):

    # holder for student numbers from CSV file
    studentstoselect = []

    # load up the CSV values
    with open('C:/Users/ceide/Desktop/Python Scripts/SelectionFilterPopulator/input.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(row['student_studentNumber'])
            studentstoselect.append(row['student_studentNumber'])

    #shift view to iFrame and locate <select> element
    frame = driver.find_element(By.ID, "frameWorkspace")
    driver.switch_to.frame(frame)
    studentListSelect = Select(driver.find_element(By.ID, "allListID"))

    # find the button used to move values to right
    movebutton = driver.find_element(By.ID, "addSelection")

    # iterate through options and select ones in the list of students, then move them to the right
    for option in studentListSelect.options:

        optionStudentNumber = option.text.split('#',1)[1]
        print("Option Student Number: " + optionStudentNumber)

        if(optionStudentNumber in studentstoselect):
            option.click()
            movebutton.click()

    loopinput = input("Would you like to try again? (Y/N)")
    if (loopinput == 'N'):
        loop = False

print("Script Execution Complete")
driver.quit()