import json
from Items import convert_todate, item_support


def public_getter(request_handler, request,tok):
    req=request.split("<!>")
    if req[1] in tok.keys():
        uid = str(request_handler.db_conn.execute("select id from site_users WHERE username LIKE '" + tok[req[1]] + "'")).translate(None,'()[]",').translate(None, "'")
        querry=request_handler.db_conn.execute("select * from (select * from items where user_id="+uid+" order by DBMS_RANDOM.RANDOM) where rownum<2")
        return item_support(request_handler,querry)
    else:
        return json.dumps({'item_name'       : "Not logged in Error",
                           'date_posted'     : "It's an error date :)",
                           'item_description': "Please log in or relog (maybe the server restarted) ",
                           'publisher'       : "Red Screen of Error"},
                            indent=4,
                            separators=(',', ': '))