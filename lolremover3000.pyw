import os
import shutil
import time
import winreg
import ctypes, sys
import signal


log_dir = f"C:/Users/{os.getlogin()}/AppData/local/Ultra top secret shit"
log_file_name = "lol_remover_log.txt"

delay = 3 # in minutes

# check if directory for log file exists
if not os.path.isdir(log_dir):
	os.mkdir(log_dir)

# open the log file
log_file = open(log_dir + '/' + log_file_name, "a")
log_file.close()

log_file = open(log_dir + '/' + log_file_name, "r+")

# make a sneaky copy of the script in case anyone finds and removes it
shutil.copy(os.path.realpath(__file__), log_dir)

# loop infinitely and check for lol every 3 mins
while True:
	try:
		# kill the fugnking Riot Games client
		processes = ['RiotClientCrashHandler.exe', 'RiotClientServices.exe', 'RiotClientUx.exe', 'RiotClientUxRenderer.exe']

		for process in processes:
			os.system("taskkill /F /im " + process)

		# get the location of the riot client
		key = winreg.OpenKeyEx(winreg.HKEY_CLASSES_ROOT, r'riotclient\\shell\\open\\command')
		value = winreg.QueryValueEx(key, '')

		riot_games_location = value[0].split("\"")[1].removesuffix('Riot Client\RiotClientServices.exe')


		if os.path.isdir(riot_games_location):
			shutil.rmtree(riot_games_location)
			log_file.writelines("Deleting " + riot_games_location)

		time.sleep(delay * 60)
	except Exception as e:
		print("Ayo we have an arror: " + str(e))

log_file.close()