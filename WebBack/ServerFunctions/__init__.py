from Login        import login
from Register     import register
from SessionCheck import validate_token
import json
import calendar

#=================================pt transformarea unei date primite din SQL in ceva calumea
def convert_todate(an, luna, zi):
    an_bun=an.split('(')
    zi_num=calendar.weekday(int(an_bun[1]),int(luna),int(zi))
    zi_name=calendar.day_name[zi_num]
    good_date=calendar.month_name[int(luna)]+' '+an_bun[1]+' '+zi_name+zi
    return good_date

#==========================================================================
#pt general use (category items) -folosita in functii care iau iteme direct, nu folosi la altceva!
def item_support(request_handler, querry):
    prearranged_querry = str(querry).split(',')
    username_querry = request_handler.db_conn.execute("select username from site_users where id=" + prearranged_querry[1])
    username = str(username_querry).translate(None, '()[]",').translate(None, "'")
    itemname = prearranged_querry[2].translate(None, "'")
    return json.dumps({'item_name': itemname, 'date_posted': convert_todate(prearranged_querry[4], prearranged_querry[5],prearranged_querry[6]), 'item_description': prearranged_querry[3],'publisher': username}, indent = 4, separators = (',', ': '))
     #===============JSON POWAH!!!================================
    #un fisier json e un fisier k=cheie valoare dupa cum probabil se si observa
    #un fisier json poate fi si vector de vectori de chei valori (lista ar fi un cuv mai bun) , but let's keep things simple


#============================================================================
#============================================================================

#=====pt pg de iteme======
def item_category(request_handler, category):
    if category == "item":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Item%' order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "festival":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Festival%' or title LIKE '%Contest%' order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "ceremony":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Ceremony%' or title LIKE '%Gathering%'order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "pub":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Pub%' or title LIKE '%Cafe%' order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "restaurant":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Restaurant%' order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "hotel":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Hotel%' order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "party":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Party%' order by DBMS_RANDOM.RANDOM) where rownum<2"))
    if category == "title":
        return item_support(request_handler, request_handler.db_conn.execute("select * from (select * from items where title LIKE '%Title%' order by DBMS_RANDOM.RANDOM) where rownum<2"))


#=========================
#=====pt Search======
def search_item(selfie,msg):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%"+msg+"%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    print "aici"
    print msg;
    print querry;
    if str(querry)!="[]":
        itmw=item_support(selfie, querry)
    else:
        itmw=json.dumps({'item_name': "Void Error",
                               'date_posted': "Search Harder!",
                               'item_description': "This is not an Error ", 'publisher': "Red Screen of Error"}, indent=4,
                              separators=(',', ': '))

    return itmw
