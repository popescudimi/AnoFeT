CREATE OR REPLACE PROCEDURE insert_site_users(ids NUMBER, num VARCHAR2, prenum VARCHAR2, mail VARCHAR2, unum VARCHAR2, pass VARCHAR2, seq VARCHAR2, sea VARCHAR2) IS
  BEGIN
    INSERT INTO SITE_USERS VALUES (ids,num,prenum,mail,TO_TIMESTAMP(SYSDATE),unum,pass,seq,sea);
    COMMIT;
  END;
CREATE OR REPLACE PROCEDURE insert_review(uid NUMBER, itid NUMBER ,content VARCHAR2) IS
 r_id NUMBER;
  BEGIN
    SELECT max(id) INTO r_id from REVIEWS;
    r_id:=r_id+1;
    INSERT INTO REVIEWS VALUES (r_id,uid,itid,content,TO_TIMESTAMP(SYSDATE));
    COMMIT;
  END;