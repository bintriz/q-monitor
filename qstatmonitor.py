import collections
import subprocess


class QStatMonitor:
    def __init__(self):
        self._update_command = "qstat"
        self.status = collections.defaultdict(dict)
        self.state = {}
        self.isDone = False

    def _update_qstat(self):
        p = subprocess.Popen(self._update_command,
                             shell=True,
                             stdout=subprocess.PIPE)
        output = p.stdout.read().split('\n')
        if output[0] == '':
            self.status = {}
            self.isDone = True
        else:
            output.pop(-1) # remove trailing
            output.pop(1)  # remove -----
            header = output.pop(0)
            header = header.split()
            for row in output:
                row = row.split()
                row[5] = ' '.join(row[5:7])
                self.status[row[0]] = dict(zip(header[1:6], row[1:6]))

    def _update_current_state(self):
        all_state = []
        for job_id in self.status:
            all_state.append(self.status[job_id]["state"])
        self.state = collections.Counter(all_state)

    def update(self):
        #assert not self.isDone, "Jobs already done."
        self._update_qstat()
        self._update_current_state()

    @property
    def num_jobs(self):
        self.update()
        return sum(self.state.values())
