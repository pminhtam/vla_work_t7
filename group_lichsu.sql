use sanpham
select DATEPART(hour,ngay_sinh) as gio,sum(num) as sum_day from lichsu
group by day(ngay_sinh),DATEPART(hour,ngay_sinh)

go 
select CAST(ngay_sinh as DATE) from lichsu

go
select CAST(ngay_sinh as DATE),DATEPART(hour,ngay_sinh) as gio,sum(num) as sum_day from lichsu
group by CAST(ngay_sinh as date) ,DATEPART(hour,ngay_sinh)
order by CAST(ngay_sinh as date),DATEPART(hour,ngay_sinh)