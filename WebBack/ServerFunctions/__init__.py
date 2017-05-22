from Login      import login
from Register   import register
import json
import string
import random
import calendar



#global
token_vector={}
#=================================pt transformarea unei date primite din SQL in ceva calumea
def convert_todate(an, luna, zi):
    an_bun=an.split('(')
    zi_num=calendar.weekday(int(an_bun[1]),int(luna),int(zi))
    zi_name=calendar.day_name[zi_num]
    good_date=calendar.month_name[int(luna)]+' '+an_bun[1]+' '+zi_name+zi
    return good_date

#==========================================================================
#pt general use (category items) -folosita in functii care iau iteme direct
#nu folosi la altceva!
def item_like_support(selfie,querry):
    prearanged_querry = str(querry).split(',')
    uname_querry = selfie.db_conn.execute("select username from site_users where id=" + prearanged_querry[1])
    uname_rdy = str(uname_querry).translate(None, '()[]",')
    uname_rdy = uname_rdy.translate(None, "'")
    iname_rdy = prearanged_querry[2].translate(None, "'")
    #print uname_querry
    #print str(prearanged_querry)
     #===============JSON POWAH!!!================================
    #un fisier json e un fisier k=cheie valoare dupa cum probabil se si observa
    #un fisier json poate fi si vector de vectori de chei valori (lista ar fi un cuv mai bun) , but let's keep things simple
    raspuns_json=json.dumps({'item_name': iname_rdy,'date_posted':convert_todate(prearanged_querry[4],prearanged_querry[5],prearanged_querry[6]), 'item_description': prearanged_querry[3],'publisher':uname_rdy},indent = 4, separators = (',', ': '))
    return raspuns_json

#============================================================================
#============================================================================

#=====pt pg de iteme======
def item_item(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Item%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de festivals======
def item_festival(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Festival%' or title LIKE '%Contest%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Ceremonii======
def item_ceremony(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Ceremony%' or title LIKE '%Gathering%'order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Restaurants======
def item_restaurant(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Restaurant%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Pubs======
def item_pub(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Pub%' or title LIKE '%Cafe%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Hotels======
def item_hotel(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Hotel%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Party======
def item_party(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Party%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Titles======
def item_title(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Title%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt Search======
def search_item(selfie,msg):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%"+msg+"%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    print "aici"
    print msg;
    print querry;
    if str(querry)!="[]":
        itmw=item_like_support(selfie,querry)
    else:
        itmw=json.dumps({'item_name': "Void Error",
                               'date_posted': "Search Harder!",
                               'item_description': "This is not an Error ", 'publisher': "Red Screen of Error"}, indent=4,
                              separators=(',', ': '))

    return itmw

#===============================================================================================================================================

#===============================================================================================================================================
#The Tokenizer


#===============================================================================================================================================

def validare_token(selfie,raw_request):
    request=raw_request.split(',');
    global token_vector
    if request[1] in token_vector.keys() :
        raspuns=json.dumps({"verify":"Ok"},indent=4,separators=(',', ': '))
        return raspuns
    else:
        raspuns = json.dumps({"verify": "No"}, indent=4, separators=(',', ': '))
        return raspuns




