

DELIMITER $$
CREATE DEFINER=`bmanager`@`%` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(45),
    IN p_username VARCHAR(45),
    IN p_password VARCHAR(150)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
        select 'Username Exists !!';
    ELSE
        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;

use qbank;

insert into tbl_catBig values ("B1", "Network");
insert into tbl_catBig values ("B3", "Windows");
insert into tbl_catBig values ("B2", "Linux");

insert into tbl_catMid values ("M1_N", "DNS");
insert into tbl_catMid values ("M2_N", "HTTP");
insert into tbl_catMid values ("M3_N", "FTP");