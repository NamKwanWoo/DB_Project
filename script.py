f = open("/Users/namnamnam/Desktop/person_List.txt", 'w')


while True:
    #addr_line = addr_list.readline()

    if not id_line: break
    data = "INSERT INTO Person (NamDB.Person.UserID, NamDB.Person.Password, NamDB.Person.Name, NamDB.Person.Email, NamDB.Person.Phone, NamDB.Person.Address)\n"
    f.write(data)
    data = "VALUES ('%s', '%s', '%s', '%s', '%s', '%s');\n\n" % (id_line , pw_line , name_line ,email_line , ph_line , addr_line)
    f.write(data)

f.close()
