import random
from email_generator import generate_emails
from search.binary_search import binary_search_iter

from analysis.runtime_analyzer import analyze_func

email_domains =["google.com","aol.com","juno.com","cs.utah.edu","eng.utah.edu","qcomm.com","waterford.edu","rxamerica.com"]
email_usernames = ["Drew","Andrew","andrew.elegante","elegante","drew","high.priest.of.good.times","hpogt1"]
email_list_size = 1000000
emails, run_time = analyze_func(generate_emails,email_list_size,email_usernames,email_domains)
print(f"generated {email_list_size} emails in {run_time:.4f} seconds")
emails, run_time = analyze_func(sorted,emails)
print(f"sorted {email_list_size} emails in {run_time:.4f} seconds")
s_email = emails[random.randint(0,email_list_size-1)]
ix, run_time = analyze_func(binary_search_iter,emails,s_email)
print(f"found email {s_email} at index {ix} in {run_time:.4f} seconds" )
