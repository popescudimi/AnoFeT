import json
from WebBack.ServerFunctions.Items import item_support


def get_invitation(request_handler, request,tok):
    req = request.split("<!>")
    if req[1] in tok.keys():
        uid = str(request_handler.db_conn.execute("select id from site_users WHERE username LIKE '" + tok[req[1]] + "'")).translate(None, '()[]",').translate(None, "'")
        inv_id=str(request_handler.db_conn.execute("select P_ITEM_ID from (select P_ITEM_ID from P_ITEMS_ACCESS where USER_ID="+uid+" order by DBMS_RANDOM.RANDOM) where rownum<2"))
        inv_id=inv_id.translate(None, '()[]",').translate(None, "'")
        qurry_pvt=request_handler.db_conn.execute("select * from PRIVATE_ITEMS where id="+inv_id)
        return item_support(request_handler,qurry_pvt)
    else:
        return json.dumps({'item_name': "Not logged in Error",
                           'date_posted': "It's an error date :)",
                           'item_description': "Please log in or relog (maybe the server restarted) ",
                           'publisher': "Red Screen of Error"},
                          indent=4,
                          separators=(',', ': '))
