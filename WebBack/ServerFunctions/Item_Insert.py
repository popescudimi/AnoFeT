import json


def insert_item(request_handler, raw_request,tok):
    raw_request = raw_request.split("<!>")

    if raw_request[1] not in tok.keys():
        response = json.dumps({'Stat' : 'Bad Token'}, indent = 4, separators = (',', ': '))

    elif raw_request[2] == 'Public':

        uid = str(request_handler.db_conn.execute("SELECT ID FROM SITE_USERS WHERE username LIKE '%" + tok[raw_request[1]] + "%'")).translate(None,'()[]",').translate(None, "'")
        print uid;
        uid=int(uid)
        request_handler.db_conn.callProcedure("ADD_ITEM", [uid, raw_request[3], raw_request[4]])
        response = json.dumps({'Stat' : 'Success!'}, indent = 4, separators = (',', ': '))

    elif raw_request[2] == 'Private':
        uid=str(request_handler.db_conn.execute("SELECT ID FROM SITE_USERS WHERE username LIKE '%" + tok[raw_request[1]] + "%'")).translate(None, '()[]",').translate(None, "'")
        #print uid;
        uid=int(uid)
        request_handler.db_conn.callProcedure("ADD_PRIVATE_ITEM", [uid, raw_request[3], raw_request[4]])

        # for every email, find the user ID if the user exists, otherwise exit
        user_ids = raw_request[5].split(",")
        #print user_ids
        for i in range(len(user_ids)):
            #print user_ids[i];
            user_id = str(request_handler.db_conn.execute("SELECT ID FROM SITE_USERS WHERE EMAIL LIKE '%" + user_ids[i] + "%'")).translate(None, '()[]",').translate(None, "'")
            print user_id
            if len(user_id) == 0:
                return json.dumps({'Stat' : 'Bad Email'}, indent=4, separators=(',', ': '))
            else:
                user_ids[i] = user_id
                print user_ids

        # add the users to the list of allowed users for the new item
        item_id = str(request_handler.db_conn.execute("SELECT ID FROM PRIVATE_ITEMS WHERE TITLE LIKE '%" + raw_request[3] + "%'")).translate(None, '()[]",').translate(None, "'")
        item_id =int(item_id)
        for user_id in user_ids:
            request_handler.db_conn.callProcedure("ADD_USER_TO_PRIVATE_ITEM", [user_id, item_id])

        response = json.dumps({'Stat': 'Success!'}, indent=4, separators=(',', ': '))

    else:
        response = json.dumps({'Stat': 'Error'}, indent=4, separators=(',', ': '))

    return response

# 'IObject<!>5c66u738l<!>Private<!>ExempluTitlu Item<!>ExempluDescriere<!>exemplu@mail.com,altexemplu@mail.com'