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
    DBMS_OUTPUT.PUT_LINE('Exception! No data found!');
    v_avg_rate:=0;
    v_last_review:=TO_DATE('1000-01-01');
  END;
  BEGIN
    SELECT max(DATE_LEFT) into v_last_rating FROM RATINGS where ITEM_ID=v_item;
        EXCEPTION
    WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('Exception! No data found!');
    v_avg_rate:=0;
    v_last_review:=TO_DATE('1000-01-01');
  END;
  if (EXTRACT(DAY FROM (SYSDATE-v_last_review))>731)THEN
    v_avg_rate:=0; -- nu avem arhiva
    ELSE
    v_avg_rate:=-1; -- are review recent dar nu si rating 
  END IF;
  if (EXTRACT(DAY FROM(SYSDATE-v_last_rating))>731)THEN
    SELECT ROUND(avg(SCORE)) INTO v_avg_rate FROM RATINGS WHERE ITEM_ID=v_item;
    RETURN v_avg_rate;
  END IF;
  RETURN v_avg_rate; -- > 0 si returnam ratingul avg
END;