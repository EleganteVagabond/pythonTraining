from projects.job_scheduler.job_scheduler import JobScheduler

jst = JobScheduler()
jst.load_file("projects/job_scheduler/data.txt")
print("*"*40)

while True :
    jst.print_menu()
    cmd = input("?")
    jst.process_command(cmd)
