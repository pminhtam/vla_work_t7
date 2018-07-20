/****** Script for SelectTopNRows command from SSMS  ******/
use sanpham

delete from dinhdanh where id_sp<10000
DBCC CHECKIDENT (dinhdanh, RESEED, 0)
delete from lichsu where id<1000000
DBCC CHECKIDENT (lichsu, RESEED, 0)

delete from danhsach where id<10000
DBCC CHECKIDENT (danhsach, RESEED, 0)

ALTER TABLE dinhdanh
ADD UNIQUE (ma_dd);

ALTER TABLE lichsu
ADD UNIQUE (num_sum);

