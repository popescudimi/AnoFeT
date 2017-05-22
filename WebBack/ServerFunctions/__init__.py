from Login        import login
from Register     import register
from Items        import item_category
from SessionCheck import validate_token
import json



#==========================================================================



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
