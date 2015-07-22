import sys
import subprocess
import time

from qstatmonitor import QStatMonitor


def submit_job(command):
    print "Submit a job.\n"
    subprocess.Popen(command, shell=True)

def show_stat(qs):
    print "Current: {0}, Remain: {1} \n".format(
            sum(qs.state.values()),
            num_jobs - i - 1
            )


if __name__ == "__main__":
    MAX_JOBS = int(sys.argv[1])
    command = sys.argv[2:]
    print command
    qs = QStatMonitor()
    qsub_command = ''
    num_jobs = 5
    for i in range(num_jobs):
        if i == 0 or sum(qs.state.values()) < MAX_JOBS:
            submit_job(command)
            qs.update()
            show_stat(qs)
        else:
            while(True):
                print "Wait for available slot..."
                time.sleep(10)
                qs.update()
                if sum(qs.state.values()) < MAX_JOBS:
                    submit_job(command)
                    show_stat(qs)
                    break
