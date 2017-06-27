f = open("/Users/namnamnam/Desktop/person_List.txt", 'w')
name_list = open("/Users/namnamnam/Desktop/listOfName.txt", 'r')



while True:
    line = name_list.readline()
    if not line: break
    data = "INSERT INTO Person (NamDB.Person.UserID, NamDB.Person.Password, NamDB.Person.Name, NamDB.Person.Email, NamDB.Person.Phone, NamDB.Person.Address)\n"
    f.write(data)
    data = "VALUES ('%s', 'skarhksdn', 'NamKwanWoo', 'namkwanwoo94@gmail.com', '01063649614', 'Seoul Seonbukgu');\n" % line
    f.write(data)
    print(line)

f.close()



