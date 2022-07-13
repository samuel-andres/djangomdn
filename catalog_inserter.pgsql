DELETE FROM catalog_author;

INSERT INTO 
    catalog_author (first_name, last_name, date_of_birth, date_of_death)
VALUES
    ('Stephen', 'King', '1947-09-21', NULL);

INSERT INTO 
    catalog_author (first_name, last_name, date_of_birth, date_of_death)
VALUES
    ('Agatha', 'Christie', '1890-09-15', '1976-01-12');

INSERT INTO 
    catalog_author (first_name, last_name, date_of_birth, date_of_death)
VALUES
    ('Jorge Luis', 'Borges', '1989-08-24', '1986-06-14');

INSERT INTO 
    catalog_author (first_name, last_name, date_of_birth, date_of_death)
VALUES
    ('Mario', 'Benedetti', '1920-09-14', '2009-05-17');


DELETE FROM catalog_language;

INSERT INTO 
    catalog_language (name)
VALUES
    ('English');

INSERT INTO 
    catalog_language (name)
VALUES
    ('Spanish');

INSERT INTO 
    catalog_language (name)
VALUES
    ('Polish');

DELETE FROM catalog_book;

INSERT INTO
    catalog_book (title, summary, pubdate, isbn, author_id, language_id)
VALUES
    ('Carrie', 'Set primarily in the then-future year of 1979, it revolves around the eponymous Carrie White, a friendless, bullied high-school girl from an abusive religious household who uses her newly discovered telekinetic powers to exact revenge on those who torment her.', '1974-04-05','9789871138999',1,1)





