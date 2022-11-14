import os
import time
import subprocess
import scenario


def get_cur_time():
    return time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))


RESULT_FOLDER = get_cur_time()
if RESULT_FOLDER not in os.listdir(os.getcwd()):
    os.mkdir(RESULT_FOLDER)
os.chdir(RESULT_FOLDER)

logcat = "adb logcat"
event = "adb logcat -b events -v time"
home = "adb shell input keyevent 3"

logcat_log = open("fulltime_logcat.txt", "a")
event_log = open("fulltime_eventlog.txt", "a")
proc_meminfo_log = open("fulltime_proc_meminfo.txt", "a")
dumpsys_meminfo_log = open("fulltime_dumpsys_meminfo.txt", "a")

logcat_pars = subprocess.Popen(logcat, stdout=logcat_log, shell=False)
event_pars = subprocess.Popen(event, stdout=event_log, shell=False)

sequence = 1
scenarios = scenario.SCENARIO * 5
for app in scenarios:
    print("run this app[{}/{}] : {}".format(sequence, len(scenarios), app))
    start = scenario.PACKAGE[app] + "/" + scenario.ACTIVITY[app]
    cmd = "adb shell am start -W " + start + " > launch.txt"
    os.system(cmd)
    time.sleep(10)

    cur_time = get_cur_time()
    dumpsys_meminfo = os.popen("adb shell dumpsys meminfo").read()
    proc_meminfo = os.popen("adb shell cat /proc/meminfo").read()
    proc_meminfo_log.write("{}\nrun this app : {}\n\n{}\n\n".format(cur_time, app, proc_meminfo))
    dumpsys_meminfo_log.write("{}\nrun this app : {}\n\n{}\n\n".format(cur_time, app, dumpsys_meminfo))

    sequence += 1
    os.system(home)
    proc_meminfo_log.flush()
    dumpsys_meminfo_log.flush()

proc_meminfo_log.close()
dumpsys_meminfo_log.close()

logcat_pars.terminate()
event_pars.terminate()

os.system("del /q launch.txt")
os.system("adb bugreport")
