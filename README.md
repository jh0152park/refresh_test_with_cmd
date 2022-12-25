# Simple Android Platform Mulitasking Performance(Refresh) Test Scritp
------------------------------

# Overview
This script helpful to check about the multitasking performance every single application on test devices.

Currently support only windows PC and used adb am start command like below.

+ adb -s [device id] shell am start -W [package name]/[activity name]

Test application secanrio included 20 different applications also its 1 cycle(shopping, game, sns, etc...)

We will launch total 5 cycle(launch 100 time each test applications)

------------------------------


# Requirement
1. adb (Android Debug Bridge)
2. Android platform device (Its would be better if the OS version higher than 11)
------------------------------

# Result Files
1. full time proc/meminfo log file
2. full time dumpsys meminfo log file
3. full time logcat log file
4. full time event log file
5. dumpstate(bugreport) of last status after finished test
------------------------------

# Test Application and Scenario Sequence
![reentry_performance](https://user-images.githubusercontent.com/118165975/209472287-5f947738-ba1a-4acc-a724-50390b71c3eb.png)
