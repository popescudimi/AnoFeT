#==========================Verifiers=====================================
#informatiile pt inregistrare sunt verificate sa fie bune
def verify_corect_register_info(request):
    if len(request[0])>3 and len(request[1])>5 and request[1]==request[2] and '@' in request[3] and '.' in request[3] and len(request[3])>8 and len(request[4])>3 and len(request[5])>3:
        return True
    return False


#verifica daca nu este deja un utilizator cu un username asemanator sau cu email la fel
def verify_database_for_duplicates(request_handler, request):
    if(len(request_handler.db_conn.execute("select * from site_users where USERNAME LIKE '%"+request[0]+"%'")) == 0 and len(request_handler.db_conn.execute("select * from site_users where EMAIL LIKE '%"+request[3]+"%'"))== 0):
        return True
    return False


def process_register_data(register_request):
    vect_info = []
    for f in register_request.replace('%40', '@').split('&'):
        vect_info.append(f.split('=')[1])
    return vect_info


def inregistrare(request_handler, raw_request):
    processed_request = process_register_data(raw_request)
    if verify_corect_register_info(processed_request) == True and verify_database_for_duplicates(request_handler, processed_request) == True:
            id = int(request_handler.db_conn.execute("select max(id) from site_users")) + 1
            print id
            request_handler.db_conn.callProcedure("insert_site_users",(id,processed_request[5],processed_request[4],processed_request[3],processed_request[0],processed_request[1],"A Question?","Maybye"))
            print "Register successful"

            #insertop="insert into site_users VALUES ("+str(number)+","+"'"+processed_request[5]+"'"+","+"'"+processed_request[4]+"'"+","+"'"+processed_request[3]+"'"+","+"TO_TIMESTAMP(SYSDATE)"+","+"'"+processed_request[0]+"'"+","+"'"+processed_request[1]+"'"+","+"'"+"A Question?"+"'"+","+"'"+"Maybye"+"'"+")"
            #str(insertop);
            #print insertop
            #selfie.connection.comit()
            #to be continued