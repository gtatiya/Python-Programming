
import subprocess
import sys
import time


def sleep_and_display(seconds_to_wait):
    """
    Sleep and display the remaining time
    """
    if type(seconds_to_wait) == int:
        for remaining in range(seconds_to_wait, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} sec. remaining".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r")
        sys.stdout.flush()
    else:
        time.sleep(seconds_to_wait)

if __name__ == "__main__":
	"""
	This script kills teamviewer, launchs teamviewer and then wait in a forever loop
	"""

	sleep_time_sec = 60 * 4

	while True:

		# Finding processes running teamviewer
		list_cmd = subprocess.Popen("ps aux | grep teamviewer", shell=True, stdout=subprocess.PIPE)
		list_output = list_cmd.stdout.read().decode("utf-8")

		# Finding pids of processes running teamviewer
		pid_list = []
		for process in list_output.split("\n"):
			if "/opt/teamviewer/" in process:
				process = ' '.join(process.split())
				process = process.split(' ')
				print("process: ", process)
				pid_list.append(process[1])

		# Killing all the pids of processes running teamviewer
		for pid in pid_list:
			cmd = "kill -9 " + pid
			print(cmd)
			list_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
			list_output = list_cmd.stdout.read().decode("utf-8")

		# Launching teamviewer
		list_cmd = subprocess.Popen('teamviewer', shell=True, stdout=subprocess.PIPE)

		sleep_and_display(sleep_time_sec)
