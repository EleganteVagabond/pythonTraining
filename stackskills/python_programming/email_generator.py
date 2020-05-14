import random

def generate_emails(num_emails,prefixes,domains) :
    emails = []
    for i in range(num_emails):
        domain = domains[random.randint(0,len(domains)-1)]
        prefix = prefixes[random.randint(0,len(prefixes)-1)]
        emails.append(prefix+"@"+domain)

    return emails
