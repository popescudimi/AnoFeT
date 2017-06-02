import json
from Item_Search import convert_todate


def review_getter(request_handler, request):
    itmw = request.split(">")[1]
    querry = request_handler.db_conn.execute("select * from (select * from items where title LIKE '%" + itmw + "%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    prearranged_querry = str(querry).split(',')
    it_id = str(prearranged_querry[0]).translate(None, '()[]",').translate(None, "'")

    querry = request_handler.db_conn.execute("select * from (select * from REVIEWS where ITEM_ID="+it_id+" order by DBMS_RANDOM.RANDOM) where rownum<2")
    querry = str(querry).split(',')
    username_querry = request_handler.db_conn.execute("select username from site_users where id=" + querry[1])
    username = str(username_querry).translate(None, '()[]",').translate(None, "'")
    content = querry[3]
    dat_left = convert_todate(querry[4],querry[5],querry[6])
    return json.dumps({'item_name'       : "Review by "+username,
                       'date_posted'     : dat_left,
                       'item_description': content,
                       'publisher'       : username},
                        indent = 4,
                        separators = (',', ': '))


def review_inserter(request_handler, request, tok):
    processed_request = request.split("<!>")
    if processed_request[1] in tok.keys():
        uid  = str(request_handler.db_conn.execute("select id from site_users WHERE username LIKE '"+tok[processed_request[1]]+"'")).translate(None, '()[]",').translate(None, "'")
        itid = str(request_handler.db_conn.execute("select id from items WHERE title LIKE '%"+processed_request[2]+"%'")).translate(None, '()[]",').translate(None, "'")
        uid  = int(uid)
        itid = int(itid)
        request_handler.db_conn.callProcedure("insert_review",[uid,itid,processed_request[3]])
        return json.dumps({'Ack' : "Success!"},indent = 4,separators = (',', ': '))
    else:
        return json.dumps({'Ack' : "Bad Token"},indent = 4,separators = (',', ': '))



