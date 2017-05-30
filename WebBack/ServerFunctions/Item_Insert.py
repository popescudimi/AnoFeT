import json


def insert_item(request_handler, raw_request):
    raw_request = raw_request.split("<!>")

    if raw_request[1] not in request_handler.active_tokens.keys():
        response = json.dumps({'result' : 'bad_token'}, indent = 4, separators = (',', ': '))
    else:
        if raw_request[2] == 'N': # Public item(not private)
            request_handler.db_conn.callProcedure("ADD_ITEM", [request_handler.db_conn.execute("SELECT ID FROM SITE_USERS WHERE EMAIL LIKE '%" + request_handler.active_tokens[raw_request[1]] + "%'")[0][0], raw_request[3], raw_request[4]])
            response = json.dumps({'result' : 'success'}, indent = 4, separators = (',', ': '))
        else:
            # TODO Need to add the "private" column to the DB
            print "Private item"
            response = json.dumps({'result': 'success'}, indent=4, separators=(',', ': '))

    return response