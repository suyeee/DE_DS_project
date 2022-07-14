USE wildfire;
select database();

SHOW VARIABLES LIKE "character_set_database";

# 데이터 삽입하기
create table latitude(
	stnld int(3) PRIMARY KEY,
    stnNm varchar(9),
    mngdp varchar(21),
    lat decimal(7,5),
    lgt decimal(8,5)
);

select * from latitude;

# 글자수 확인
SELECT mngdp, octet_length(mngdp) FROM latitude;
SELECT mngdp, char_length(mngdp) FROM latitude;

# 버전 확인
SELECT version();

# 한글 바이트 수정
# MySQL 버전 4 이후부터는 varchar(n) 에서 n은 글자수로 넣으면 된다고함.
# 글자수로 수정했음.
ALTER TABLE latitude MODIFY COLUMN stnNm varchar(3);
ALTER TABLE latitude MODIFY COLUMN mngdp varchar(7);