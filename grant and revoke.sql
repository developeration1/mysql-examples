CREATE USER 'test_user'@'localhost' IDENTIFIED BY '1234';

GRANT SELECT ON test.students TO 'test_user'@'localhost';

REVOKE ALL PRIVILEGES, GRANT OPTION
FROM 'test_user'@'localhost';

CREATE ROLE 'writer', 'reader';

GRANT SELECT ON test.* TO 'reader';

GRANT 'reader' TO 'test_user'@'localhost';