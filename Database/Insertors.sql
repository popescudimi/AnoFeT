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
CREATE OR REPLACE PROCEDURE ADD_ITEM(U_USER_ID     IN ITEMS.USER_ID%TYPE,
                                     U_TITLE       IN ITEMS.TITLE%TYPE,
                                     U_DESCRIPTION IN ITEMS.DESCRIPTION%TYPE) AS
    NEW_ID ITEMS.ID%TYPE;
BEGIN
    SELECT MAX(ID) INTO NEW_ID FROM ITEMS;
    NEW_ID := NEW_ID + 1;
    INSERT INTO ITEMS VALUES (NEW_ID,
                              U_USER_ID,
                              U_TITLE,
                              U_DESCRIPTION,
                              TO_TIMESTAMP(SYSDATE),
                              0);
END;
CREATE OR REPLACE PROCEDURE ADD_PRIVATE_ITEM(U_USER_ID     IN PRIVATE_ITEMS.USER_ID%TYPE,
                                             U_TITLE       IN PRIVATE_ITEMS.TITLE%TYPE,
                                             U_DESCRIPTION IN PRIVATE_ITEMS.DESCRIPTION%TYPE) AS
    NEW_ID PRIVATE_ITEMS.ID%TYPE;
BEGIN
    SELECT MAX(ID) INTO NEW_ID FROM PRIVATE_ITEMS;
    NEW_ID := NEW_ID + 1;
    INSERT INTO PRIVATE_ITEMS VALUES (NEW_ID,
                                      U_USER_ID,
                                      U_TITLE,
                                      U_DESCRIPTION,
                                      SYSDATE,
                                      0);
    COMMIT;
END;
CREATE OR REPLACE PROCEDURE ADD_USER_TO_PRIVATE_ITEM(U_ID IN SITE_USERS.ID%TYPE,
                                                     I_ID IN PRIVATE_ITEMS.ID%TYPE) AS
    NEW_ID PRIVATE_ITEMS.ID%TYPE;
BEGIN
    SELECT (MAX(ID)+1) INTO NEW_ID FROM P_ITEMS_ACCESS;
    INSERT INTO P_ITEMS_ACCESS VALUES (NEW_ID, U_ID, I_ID);
    COMMIT;
END;