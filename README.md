# inphinity
script and documents associate to INPHINITY project

To activate python 2 or 3
https://conda.io/docs/user-guide/tasks/manage-environments.html#activate-env

Duplicate DB

COPY DB command:  
mysqldump -u root -p inphinityDB_2 | mysql -u root -p inphinityDB_2_cp

mysqldump -u root -p inphinityDB_proj | mysql -u root -p inphinityDB_proj_cp


mysql -u root -pMiguel1
delete database inphinityDB_proj_cp
create database inphinityDB_proj_cp
After start the copy