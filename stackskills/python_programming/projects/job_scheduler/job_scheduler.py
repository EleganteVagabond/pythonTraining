import regex
import datetime
import os
import sys

from data_structures.binary_search_tree import BST, Node
#Job file format
# time to run, duration, name of job

#Report format
#Added:\t {job name} || Rejected:\t {job name}
#Begin:\t {time}
#End:\t {time+run_time}
#Reason:\t {Time slot overlap}
#----

# Command line ops
# Please choose an option from the list below
# Press 1 to view today's scheduled jobs
# --> Full job schedule for today (sorted)
# --> ----
# --> Time: xx, Duration: xx, End: xx Jobname: xx
# --> ....
# --> ----
# Press 2 to add a job to today's schedule
# --> You have chosen to add a job to the schedule
# --> Enter the time in hh:mm format, example 18:30 or 6:30 -> (check format)
# --> Enter the duration of the job in minutes, ex 60 ->
# --> Enter the name of the job (case sensitive) ->
# --> Print output from file load ^^
# --> Press enter to continue
# Press 3 to remove a job from the schedule
# --> You have chosen to remove a job from the schedule
# --> Enter the time in hh:mm format, example 18:30 or 6:30 -> (check format)
# --> Enter the duration of the job in minutes, ex 60 ->
# --> Enter the name of the job (case sensitive) ->
# --> The name and/or duraiton of job did not match, delete failed
# --> Removing the job:
# --> Job description from list
# --> Job successfully removed
# --> Press enter to continue...
# Press 4 to quit
# --> Exiting the program ...
#Enter your choice->

class JobNode(Node) :
    def __init__(self, j_time, j_dur, j_name) :
        self.j_start_time = datetime.datetime.strptime(j_time,"%H:%M")
        self.j_dur = j_dur
        self.j_end_time = self.j_start_time + datetime.timedelta(minutes=int(j_dur)) #some calc
        self.j_name = j_name
        super(JobNode,self).__init__(self.j_start_time,self)

    def __str__(self):
        return f"Time: {self.j_start_time:%H:%M:%S}, Duration: {self.j_dur}, End: {self.j_end_time:%H:%M:%S}, JobName: {self.j_name}"

    def f_str(self):
        return f"{self.j_start_time:%H:%M},{self.j_dur},{self.j_name}\n"

class OverlapError(Exception) :
    def __init__(self,error_job,overlapped_job) :
        self.error_job = error_job
        self.overlapped_job = overlapped_job

class JobBST(BST) :

    def _insert(self, curr, key) :
        #overlap test. 3 scenarios
        #1) key ends during curr's run time
        #2) key starts before curr and ends after curr
        #3) key starts during curr's run time
        if (curr.j_start_time < key.j_end_time and key.j_end_time < curr.j_end_time) \
            or (key.j_start_time >= curr.j_start_time and key.j_start_time < curr.j_end_time) \
            or (curr.j_start_time < key.j_start_time and key.j_start_time < curr.j_end_time)  :
            #or (key.j_start_time < curr.j_start_time and curr.j_end_time < key.j_end_time) :
            raise OverlapError(key, curr)

        super(JobBST,self)._insert(curr,key)

class JobScheduler :

    time_regex = regex.compile("\d{1,2}:\d\d")
    dur_regex = regex.compile("\d\d")
    file = ""

    def __init__(self):
        self.bst = JobBST()

    def load_file(self, fname) :
        self.file = fname
        with open(fname,"r+") as job_file :
            for line in job_file :
                self.add_job(*line.strip().split(","))

    def save_file(self) :
        with open(self.file,"w+") as job_file :
            for node in self.bst.flatten() :
                job_file.write(node.f_str())

    def add_job (self,t,dur,name) :
        #Added:\t {job name} || Rejected:\t {job name}
        #Begin:\t {time}
        #End:\t {time+run_time}
        #Reason:\t {Time slot overlap}
        job = self.parse_job(t,dur,name)
        if job :
            # add job
            try :
                self.bst.insert(job.j_start_time,job)
                print(f"Added:\t\t{job.j_name}")
                print(f"Begin:\t\t{job.j_start_time:%H:%M:%S}")
                print(f"End:\t\t{job.j_end_time:%H:%M:%S}")
                print("-"*40)
                return True
            except OverlapError as oe:
                print(f"Rejected:\t{name}")
                print(f"Begin:\t\t{job.j_start_time:%H:%M:%S}")
                print(f"End:\t\t{job.j_end_time:%H:%M:%S}")
                print(f"Reason:\tTime slot overlap with {oe.overlapped_job.j_name}, please verify")
                print("-"*40)

        else :
            print(f"Rejected:\t{name}")
            print(f"Reason:\tTime or duration syntax incorrect, see above")
            print("-"*40)
            return False

    def parse_job(self,t,dur,name) :
        if self.verify_time_Format(t) and self.verify_duration(dur) :
            return JobNode(t,dur,name)
        else :
            return None

    def verify_time_Format(self,time_str) :
        if regex.match(JobScheduler.time_regex, time_str) :
            return True
        else :
            print("Time format incorrect, must be in HH:MM or H:MM format (i.e. 4:30 or 18:30)")

    def verify_duration(self,dur_str):
        if regex.match(JobScheduler.dur_regex, dur_str) :
            return True
        else :
            print("Duration format incorrect, must be in exactly 2 numerical digits (i.e. 30)")

    def list_jobs(self) :
        self.bst.in_order()

    def print_menu(self) :
        print("Press 1 to view today's scheduled jobs")
        print("Press 2 to add a job to today's schedule")
        print("Press 3 to remove a job from the schedule")
        print("Press 4 to quit")

    def input_job(self):
        print("You have chosen to add a job to the schedule")
        start_time = input("Enter the time in hh:mm format, example 18:30 or 6:30 --> ")
        duration = input("Enter the duration of the job in minutes, ex 60 --> ")
        job_name = input("Enter the name of the job (case sensitive) --> ")
        if self.add_job(start_time,duration,job_name) :
            self.save_file()

        input("Press enter to continue")

    def remove_job(self):
        print("You have chosen to remove a job from the schedule")
        start_time = input("Enter the time in hh:mm format, example 18:30 or 6:30 --> ")
        duration = input("Enter the duration of the job in minutes, ex 60 --> ")
        name = input("Enter the name of the job (case sensitive) --> ")
        try :
            t = datetime.datetime.strptime(start_time,"%H:%M")
            v = self.bst.find_val(t)
            if not v :
                print(f"Error: No job starts at {start_time}")
            else :
                if v.value.j_name != name or v.value.j_dur != duration :
                    print("Error: The name and/or duration of job did not match, delete failed")
                else :
                    print("Removing the job {name} from list...")
                    self.bst.delete_val(v.value.j_start_time)
                    self.save_file()
                    print("Job successfully removed")

        except ValueError :
            print(f"Error: Time {start_time} is in an invalid format, should be HH:MM i.e. 18:30 or 6:30 or 02:00")

        print("Press enter to continue")
        sys.stdin.read(1)

    def do_exit(self) :
        print("Exiting the program")
        exit()


    cmds = {"1" : list_jobs,
            "2" : input_job,
            "3" : remove_job,
            "4" : do_exit, }

    def process_command(self,cmd):
        method = self.cmds.get(cmd)
        if method :
            method(self)
