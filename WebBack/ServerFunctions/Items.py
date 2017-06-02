import json
import calendar


def convert_todate(year, month, day):
    year = year.split('(')[1]
    return calendar.month_name[int(month)] + ' ' + year + ' ' + calendar.day_name[calendar.weekday(int(year), int(month), int(day))] + day
    # transformarea unei date primite din SQL in ceva calumea


def item_support(request_handler, querry):
    prearranged_querry = str(querry).split(',')
    username_querry = request_handler.db_conn.execute("select username from site_users where id=" + prearranged_querry[1])
    username = str(username_querry).translate(None, '()[]",').translate(None, "'")
    itemname = prearranged_querry[2].translate(None, "'")
    return json.dumps({'item_name'       : itemname,
                       'date_posted'     : convert_todate(prearranged_querry[4], prearranged_querry[5],prearranged_querry[6]),
                       'item_description': prearranged_querry[3],
                       'publisher'       : username},
                        indent = 4,
                        separators = (',', ': '))
    # un fisier json e un fisier k=cheie valoare sau vector de vectori de chei valori (lista ar fi un cuv mai bun) , but let's keep things simple
    # general use (category items) -folosita in functii care iau iteme direct, nu folosi la altceva!


def item_category(request_handler, category):
    if category == "item":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Item%'                                order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "festival":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Festival%' or title LIKE '%Contest%'  order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "ceremony":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Ceremony%' or title LIKE '%Gathering%'order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "pub":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Pub%' or title LIKE '%Cafe%'          order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "restaurant":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Restaurant%'                          order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "hotel":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Hotel%'                               order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "party":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Party%'                               order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "title":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Title%'                               order by DBMS_RANDOM.RANDOM) where rownum<2"))


def search_item(request_handler, msg):
    querry = request_handler.db_conn.execute("select * from (select * from items where title LIKE '%"+msg+"%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    if len(querry) != 0:
        return item_support(request_handler, querry)
    else:
        return json.dumps({'item_name'       : "Void Error",
                           'date_posted'     : "Search Harder!",
                           'item_description': "This is not an Error ",
                           'publisher'       : "Red Screen of Error"},
                            indent=4,
                            separators=(',', ': '))
