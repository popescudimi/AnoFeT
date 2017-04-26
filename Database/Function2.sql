CREATE OR REPLACE PROCEDURE archive_old_things IS
  v_avg_rating NUMBER;
  v_desc ARCHIVED_ITEMS.DESCRIPTION%TYPE;
  v_title ARCHIVED_ITEMS.TITLE%TYPE;
  v_itid NUMBER;
  v_st_d ARCHIVED_ITEMS.START_DATE%TYPE;
  v_usd NUMBER;
  v_nr NUMBER;
  CURSOR Farc IS
    SELECT id,USER_ID,TITLE,DESCRIPTION,START_DATE FROM ITEMS FOR UPDATE;
  BEGIN
    SELECT count(*)+1 INTO v_nr FROM ARCHIVED_ITEMS;
    OPEN Farc;
    LOOP
      FETCH Farc INTO v_itid,v_usd,v_title,v_desc,v_st_d;
      EXIT WHEN Farc%NOTFOUND;
     v_avg_rating:=IS_ARHIVABLE(v_itid,v_st_d);
      if(v_avg_rating>0) THEN
        INSERT INTO ARCHIVED_ITEMS VALUES (v_nr,v_itid,v_usd,v_title,v_desc,v_st_d,TO_TIMESTAMP(SYSDATE),v_avg_rating);
        /*DELETE FROM ITEMS
              WHERE CURRENT OF Farc;*/
        --COMMIT;
        v_nr:=v_nr+1;
      END IF;
    END LOOP;
    CLOSE Farc;
  END;