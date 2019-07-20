Project name: Fanfan
Developed by: @RicaYang @Lynn @JiahuanLi

# Description

# Todo
# implement the appointment information frame
# move the resize function to utility (Very important)
# maybe should change writing user information into selecting profilePhoto frame?

# This project is based on Python inbuilt GUI library Tkinter
# And encapsulated by using Pyinstaller
# Other used library: Pillow, time, calender

# Description of the files:
# mainLoop.py
# This file is used as the initializer of the project, the main window is initialized in this file.

#
# signup.py
# This file contains both signup and login frame. All frames are built in the format of class. And all classes are supposed to inherit from Frame
# The signup process are subdivided into three sections, and the login process is only in one frame
# class signupFirst takes two input fields in initializer. cvs is the canvas that are used to create the next frame
# master is the window which this frame is built upon (This is same for all other master in all other class)
# This signupFirst class contains four methods:
# The initializer
# createPage: takes no input, no return and creates the first signup page
# nextCallBack: the callback function called by next button, destroy the current page and creates the next page, pass down the value that user selected in this frame
# backCallBack: the callback function called by back button, destroy the current page and return to the previous page

# The signupSecond class contains five methods:
# The initializer
# createFrame: takes no input, no return and creates the second signup page
# birthdayCallback: takes no input, no return and creates a Toplevel window to select users' birthday --> linked to dateSelection.py
# nextCallback: the callback function called by next button, destroy the current page and creates the next page, pass down the value that user selected in this frame
# backCallback: the callback function called by back button, destroy the current page and return to the previous page

# The signupThird class contains four methods:
# The initializer
# createFrame: takes no input, no return and creates the third signup page
# nextCallback: the callback function called by next button, destroy the current page and creates the next page, store all information into ./Info/userInfo.txt
# backCallback: the callback function called by back button, destroy the current page and return to the previous page

# The login class contains four methods:
# The initializer
# createPage: takes no input, no return and creates the login page
# loginCallback: the callback function called by login button, check if the username and the password is correct, if correct then destroy the current page and load the user home page
#                if not correct then display an alert information
# signupCallback: the callback function called by signup button, destroy the current page and create the signupFirst frame

#
# sub.py
# This file only contains one class sub
# sub is the frame that allows user to select and upload their selected profile photo
# sub contains five method:
# The initializer
# createPage: takes no input, no return and create the page for user to select profile photo
# selectFileName: the callback function called by select photo button, use filedialog class to allow user to select a photo from their own device
# resize(same for all resize function below): change the size of a picture, takes three input, a picture, the intended height and width that wished to change to, and return the photo with input size
# nextCallback: the callback function called by next button, if all information is valid, then destroy the current frame and load the user home page

#
# userInformation.py
# This file contains 13 supporting methods
# readUserInfo: read all users' information from ./Info/userInfo.txt, all information will be read and stored in a list, each index are:
#               0.username 1.password 2.age 3.gender 4.interested topics 5.job 6.taste preference 7.price range 8.facebook account 9.date of birth
# writeUserInfo: write user information into ./Info/userInfo.txt
# writePhotoInfo: write the file name of the profile photo into ./Info/profilePhotoInfo.txt
# getPhotoInfo: takes a username as input, and returns that user's profilePhoto's file name
# returnUsername: return all username
# checkPassword: takes username and password as input, first check if the username exist, if exist then check if the password is valid, return true if find the username and the password is correct
#                return false if cannot find the username or the password is not valid
# searchUsername: takes username as input, return user information of that user
# updateUserTaste: takes username and new user preferred taste as input. Change the original user taste to new user taste
# updatePriceRange: takes username and new user preferred price range as input. Change the original user price range to new price range
# updateUserInfo: takes username and a list of new user information as input, the list should contain user's new interested topics and new job information. Change the original information to new information
# updateUsername: takes the original username and the new username as input. Change the original username to new username
# updatePassword: takes username and new password as input. Change the original password to new password
# updatePhotoInfo: takes username and new file name for profile photo. Change the original file name into new file name

#
# appointmentInfo.py
# This file contains 9 supporting methods
# readAppointment: read all appointment information from ./Info/appointmentInfo.txt, all information will be read and stored in a list, each index are:
#                  0.first username 1.second username 2.time information[0.date 1.lunch/dinner 2.time span] 3.name of the restaurant 4.status:pending/goingto/finished
# writeAppointment: write new appointment information into ./Info/appointmentInfo.txt
# isExist: check if the user already have an appointment at designated day
# getAppointment: get the appointment of a specific user
# listToDateInfo: take a list of date information([0.date, 1.lunch/dinner, 2.time span]), and change it into a string
# changeToGoingto: change the status of an appointment to Goingto
# changeToFinished: change the status of an appointment to Finished
# listToString: take a list as input and connect every element into a string
# stringToList: take a string as input and change it into a list

#
# timeInfo.py
# This file contains 9 supporting methods
# calculateDate: a recursive function that calculate what the date would be after certain days. This function takes four inputs, year, month, day, and how many days remains to calculate
# generateDateRangeToEndOfMonth: this function takes a specific date as input, and generate a list of dates, starting from the input day and end at the end of that month
# generateMonthRangeAcrossYear: this function takes a starting month and an ending month as input, and generate a range of months across the years
# readTimeSpan: read all time information from ./Info/timeInfo.txt, all information will be read and stored in a list, each index are:
#               0.username 1.preferred dates and times([0.date, 1.dinner/lunch, 2.time span]), and so on
# checkTimeSpan: check whether if the time span stored in the file had passed, if passed then clear those time spans from the file
# writeTimeInfo: write new time information into ./Info/timeInfo.txt
# toSingleString: this method takes a list as input and change it into a string
# isTimeSpanExist: take a time span and username as input, and check if the time span already exist for that user
# checkIfTimeMatch: take two usernames as input, and check if the two users have same preferred time range stored in the file

#
# restaurant.py
# This file contains 6 supporting methods
# readRestaurant: read all restaurants' information from ./Info/restaurant.txt, all information will be read and stored in a list, each index represents:
#                 0.name of the restaurant, 1.what type of food, 2.price range
# transNametoNum: takes a list of restaurant information, and change each's type of food to a num, the transfer table is following:
#                 0.Thai 1.Chinese 2.Fast 3.American 4.Japanese 5.Sea 6.Italian 7.Desert 8.Korean 9.Mexican 10.Vietnam 11.Peru 12.African 13.Vegetarian
# matchAgeAndGender: takes a user's information as input, also takes preferred gender and preferred age as input, and return if this user matches the preferred gender and age
# matchTopicsAndJob: takes a user's information as input, also takes preferred job and topic as input,
#                    return true if the user's job matches the preferred job, and there are more than two topics are matched, otherwise return false
# matchRestaurant: takes a user's information as input, also takes preferred taste and price range as input
#                  return true if the user's preferred taste has a match with input preferred taste, and also the price range are matched, otherwise return false
# searchRestaurant: takes a specific type of food as input, and returns all restaurants that is the input type of food

#
# selectRestaurant.py
# This file contains only 1 supporting method, but it is the core of the matching process
# selectRestaurant: takes user preferences and a list of users as input, user preference should be as following format
#                   0.username, 1.preferred gender, 2.preferred age, 3.preferred taste, 4.preferred price range, 5.interested topic, 6.current job
#                   the method takes the preference of that user and matches another user with that user. The method will return a restaurant selected by the system, if no match then return null
#                   the matching process is:
#                   1.match age and gender, 2. match interested topics and jobs, 3.match if the two users' have a same time span stored in the file
#                   4.match preferred type of food and price range, 5.if there are more than one other possible users or more than one possible restaurant, randomly select a user and a restaurant

#
# dateSelection.py
# This file contains only 1 class
# The timeSelection class will generate a frame that allows user to select a date
# This class contains 11 functions
# The initializer
# createFrame: creates all the elements in the date selection frame
# leftCallback: the callback function called by left button, it goes back to previous month, and change the frame accordingly
# rightCallback: the callback function called by right button, it goes forward to next month, and change the frame accordingly
# selected: the callback function that bind with the month selection combo box, once select a month, it will change the frame accordingly
# calculateDays: this function takes a year and a month as input, calculate how many days this month should contain
# calculateStartDay: this function takes a year and a month as input, calculate the first day of that month, and which day(Monday-Sunday) it is
# dayCallback: the callback function called by all day buttons. All day buttons are stored in a list, this function will take the index of that button as input, and store the day
# resize: same as above
# reset: reset the frame to its original status
# calculateAge: calculate the age based on selected date