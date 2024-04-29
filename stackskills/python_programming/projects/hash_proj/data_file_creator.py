from email_generator import generate_emails

def create_data_file() :

    email_domains =["gmail.com","aol.com","juno.com","cs.utah.edu","eng.utah.edu","qcomm.com","waterford.edu","rxamerica.com"]
    email_usernames = ["Drew","Andrew","andrew.elegante","elegante","drew","high.priest.of.good.times","hpogt1"]
    email_list_size = 10000

    emails = generate_emails(email_list_size,email_usernames,email_domains)

    quotes = ["Hi","How are you","I'm fine, and you","I'm okay","Most days I just do until its done","Some days I hope that I get the coronavirus and die",
        "That must be hard","Yes, it can be","I don't know where the thoughts come from or why","Few people seem to care how or if I'm doing","We can only hope for a better future","Amen"]

    with open("projects/hash_proj/data.txt","w+") as f_writer :
        for e in emails :
            f_writer.write(e+":"+quotes[hash(e)%len(quotes)]+"\n")


create_data_file()
