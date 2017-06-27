f = open("/Users/namnamnam/Desktop/person_List.txt", 'w')

id_list = open("/Users/namnamnam/Desktop/ID.txt", 'r')
name_list = open("/Users/namnamnam/Desktop/listOfName.txt", 'r')
pw_list = open("/Users/namnamnam/Desktop/password_List.txt", 'r')
email_list = open("/Users/namnamnam/Desktop/email.txt", 'r')
ph_list = open("/Users/namnamnam/Desktop/phoneNumber.txt", 'r')
addr_list = open("/Users/namnamnam/Desktop/Address.txt", 'r')

while True:
    id_line = id_list.readline()
    name_line = name_list.readline()
    pw_line = pw_list.readline()
    email_line = email_list.readline()
    ph_line = ph_list.readline()
    addr_line = addr_list.readline()

    if not id_line: break
    data = "INSERT INTO Person (NamDB.Person.UserID, NamDB.Person.Password, NamDB.Person.Name, NamDB.Person.Email, NamDB.Person.Phone, NamDB.Person.Address)\n"
    f.write(data)
    data = "VALUES ('%s', '%s', '%s', '%s', '%s', '%s');\n\n" % (id_line , pw_line , name_line ,email_line , ph_line , addr_line)
    f.write(data)

f.close()
