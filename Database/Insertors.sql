CREATE OR REPLACE PROCEDURE insert_site_users(ids NUMBER,num VARCHAR2,prenum VARCHAR2,mail VARCHAR2,unum VARCHAR2,pass VARCHAR2,seq VARCHAR2,sea VARCHAR2) IS
  BEGIN
    INSERT INTO SITE_USERS VALUES (ids,num,prenum,mail,TO_TIMESTAMP(SYSDATE),unum,pass,seq,sea);
    COMMIT ;
  END;