use sanpham

CREATE TABLE danhsach (
	id int NOT NULL,
	ten nvarchar(50) NOT NULL,
	gia numeric(18,0) NOT NULL,
  CONSTRAINT PK_DANHSACH PRIMARY KEY CLUSTERED
  (
  id ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE dinhdanh (
	id bigint NOT NULL,
	id_sp int NOT NULL,
	ma_dd nvarchar(12) NOT NULL UNIQUE,
  CONSTRAINT PK_DINHDANH PRIMARY KEY CLUSTERED
  (
  id ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE lichsu (
	id int NOT NULL,
	num decimal NOT NULL,
	num_sum decimal NOT NULL,
	ngay_sinh datetime,
  CONSTRAINT PK_LICHSU PRIMARY KEY CLUSTERED
  (
  id ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO

ALTER TABLE dinhdanh WITH CHECK ADD CONSTRAINT dinhdanh_fk0 FOREIGN KEY (id_sp) REFERENCES danhsach(id)
ON UPDATE CASCADE
GO
ALTER TABLE dinhdanh CHECK CONSTRAINT dinhdanh_fk0
GO
ALTER TABLE lichsu
ADD UNIQUE (num_sum);
