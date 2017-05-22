import json
import random


def generate_token():
    token = ""
    for c in range(1, 10):
        if(random.randint(0,1) == 0):   # Digit in token
            token = token + str(random.randint(0,9))
        else:                           # Letter in token
            token = token + str(random.choice("abcdefghijklmnopqrstuvwxyz"))
    print token
    return token



def login(request_handler, raw_request):
    request = raw_request.replace("Log", "", 1).split("<!>")
    if(len(request_handler.db_conn.execute(str("select * from site_users where USERNAME LIKE '" + request[0] + "' AND PASSWORD LIKE '" + request[1] + "'"))) == 0):
        raspuns=json.dumps({"Response":"Bad","Token":"0"},indent = 4, separators = (',', ': '))
    else:
        token = generate_token()
        request_handler.active_tokens[token] = request[0]
        raspuns = json.dumps({"Response": "Good", "Token": token}, indent=4, separators=(',', ': '))
    return raspuns