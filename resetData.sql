/****** Script for SelectTopNRows command from SSMS  ******/
use sanpham

delete from dinhdanh where id_sp<100
DBCC CHECKIDENT (dinhdanh, RESEED, 0)

delete from danhsach where id<10
DBCC CHECKIDENT (danhsach, RESEED, 0)

delete from lichsu where id<10
DBCC CHECKIDENT (lichsu, RESEED, 0)


ALTER TABLE dinhdanh
ADD UNIQUE (ma_dd);

ALTER TABLE lichsu
ADD UNIQUE (num_sum);

