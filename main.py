import sys
import subprocess
import time

from qstatmonitor import QStatMonitor


def submit_job(command):
    print "Submit a job.\n"
    #subprocess.Popen("qsub ../job.sh out.out", shell=True)
    subprocess.Popen(command, shell=True)

def show_stat(qs):
    print "Current: {0}, Remain: {1} \n".format(
            qs.num_jobs,
            num_jobs - i - 1
            )


if __name__ == "__main__":
    MAX_JOBS = int(sys.argv[1])
    command = sys.argv[2:]
    qs = QStatMonitor()
    num_jobs = 5

    # Submitting jobs
    for i in range(num_jobs):
        show_stat(qs)
        if i == 0 or qs.num_jobs < MAX_JOBS:
            submit_job(command)
        else:
            while(True):
                print "Wait for available slot..."
                print i
                time.sleep(1)
                print ("wait tot:", qs.num_jobs)
                if qs.num_jobs < MAX_JOBS:
                    submit_job(command)
                    show_stat(qs)
                    break

    # Waiting for done
    while(True):
        print "Wait for done!"
        time.sleep(5)
        if qs.num_jobs == 0:
            break
    print "Done!"

    # Do Aggregation
    print "Do something more!"
