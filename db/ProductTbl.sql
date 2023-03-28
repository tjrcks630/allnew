--------------------------------------------------------
--  파일이 생성됨 - 화요일-3월-28-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table PRODUCTTBL
--------------------------------------------------------

  CREATE TABLE "HR"."PRODUCTTBL" 
   (	"PRODUCTNAME" NCHAR(4), 
	"COST" NUMBER, 
	"MAKEDATE" DATE, 
	"COMPANY" NCHAR(5), 
	"AMOUNT" NUMBER(3,0)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into HR.PRODUCTTBL
SET DEFINE OFF;
Insert into HR.PRODUCTTBL (PRODUCTNAME,COST,MAKEDATE,COMPANY,AMOUNT) values ('컴퓨터 ',10,to_date('17/01/01','RR/MM/DD'),'삼성   ',17);
Insert into HR.PRODUCTTBL (PRODUCTNAME,COST,MAKEDATE,COMPANY,AMOUNT) values ('세탁기 ',20,to_date('18/09/01','RR/MM/DD'),'LG   ',3);
Insert into HR.PRODUCTTBL (PRODUCTNAME,COST,MAKEDATE,COMPANY,AMOUNT) values ('냉장고 ',5,to_date('19/02/01','RR/MM/DD'),'대우   ',22);
--------------------------------------------------------
--  DDL for Index PRODUCTTBL_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."PRODUCTTBL_PK" ON "HR"."PRODUCTTBL" ("PRODUCTNAME") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  Constraints for Table PRODUCTTBL
--------------------------------------------------------

  ALTER TABLE "HR"."PRODUCTTBL" ADD CONSTRAINT "PRODUCTTBL_PK" PRIMARY KEY ("PRODUCTNAME")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HR"."PRODUCTTBL" MODIFY ("AMOUNT" NOT NULL ENABLE);
  ALTER TABLE "HR"."PRODUCTTBL" MODIFY ("COST" NOT NULL ENABLE);
  ALTER TABLE "HR"."PRODUCTTBL" MODIFY ("PRODUCTNAME" NOT NULL ENABLE);
