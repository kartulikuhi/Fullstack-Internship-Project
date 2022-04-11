create table categories(id int NOT NULL AUTO_INCREMENT, categoryname varchar(15), PRIMARY KEY (id));

create table posts(id int NOT NULL AUTO_INCREMENT, blogPost varchar(140), PRIMARY KEY (id));

create table connections(id AUTO_INCREMENT PRIMARY KEY, blogID int, categoryID int)