CREATE OR REPLACE FUNCTION is_arhivable(v_item ITEMS.ID%TYPE,v_date ITEMS.START_DATE%TYPE) RETURN NUMBER IS
v_last_review REVIEWS.DATE_LEFT%TYPE;
v_last_rating RATINGS.DATE_LEFT%TYPE;
v_avg_rate NUMBER;
BEGIN
  if(EXTRACT(DAY FROM (SYSDATE-v_date))<731) THEN
    RETURN 0;
  END IF;
  BEGIN
    SELECT max(DATE_LEFT) into v_last_review FROM REVIEWS where ITEM_ID=v_item;
    EXCEPTION
    WHEN NO_DATA_FOUND THEN
    --insert here error code if you want
    v_avg_rate:=0;
    v_last_review:=TO_DATE('1000-01-01');
  END;
  BEGIN
    SELECT max(DATE_LEFT) into v_last_rating FROM RATINGS where ITEM_ID=v_item;
        EXCEPTION
    WHEN NO_DATA_FOUND THEN
    --insert here error code if you want
    v_avg_rate:=0;
    v_last_review:=TO_DATE('1000-01-01');
  END;
  if (EXTRACT(DAY FROM (SYSDATE-v_last_review))>731)THEN
    v_avg_rate:=0;
    ELSE
    v_avg_rate:=-1;
  END IF;
  if (EXTRACT(DAY FROM(SYSDATE-v_last_rating))>731)THEN
    -- ar trebui normal returnat float dar asta inseamna sa schimbi
    -- si campul AVG RATING din Archived items
    -- daca schimbi campul , modifica tipul de return al functiei
    -- si scapa de round
    SELECT ROUND(avg(SCORE)) INTO v_avg_rate FROM RATINGS WHERE ITEM_ID=v_item;
    RETURN v_avg_rate;
  END IF;
  RETURN v_avg_rate;
  /* Note: -1 inseamna ca are review recent dar nu si rating (nu arhiva)
           0 inseamna nu arhiva
           >0 arhiveaza (valoarea returnata e ratingul avg)
   */

END;

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