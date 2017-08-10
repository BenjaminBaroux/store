CREATE TABLE categories (
    ID int auto_increment,
   NAME varchar(30) unique,
    PRIMARY KEY(id)
  );

CREATE TABLE Products (
id int auto_increment,
category int,
description varchar (50),
price double,
title varchar(50),
favorite boolean,
img_url varchar(50),
PRIMARY KEY(id)
);


insert into categories (name) values("Instruments"), ("Records"), ("Books");

-- select * from Categories;

insert into Products (category, description, price, title, favorite, img_url) values 
(1, 'Great Piano Steinway and sons', 35000, 'Great Piano', false, '/images/steinway.jpg'),
(1, 'Great Piano Boston', 25000, 'Great Piano', false, './images/boston.jpg'),
(1, 'Great Piano Pleyel', 15000, 'Great Piano', false, './images/pleyel.jpg'),
(2, 'Symphony Beethoven', 35.0, 'Records', false, './images/beethoven.jpg'),
(2, 'Requiem Mozart', 25.0, 'Records', false, './images/requiem.jpg'),
(2, 'Waltz Chopin', 15.0, 'Records', false, './images/waltz.jpg'),
(3, 'Nocturne Chopin', 35.0, 'Books', false, './images/chopin.jpg'),
(3, 'Prelude Rachmaninoff', 25.0, 'Books', false, './images/rachmaninoff.jpg'),
(3, 'Sonate Mozart', 15.0, 'Books', false, './images/mozart.jpg');


select * from categories;
UPDATE Products SET category=3, description='caca', price= 15, favorite=False, img_url= 'image', WHERE title='beethoven'
select * from Products;

SELECT * from Products WHERE category = 1;
drop table categories
drop table Products;

SET SQL_SAFE_UPDATES = 0;