USE test;
ALTER TABLE students
ADD CONSTRAINT area_id
FOREIGN KEY (area_id)
REFERENCES areas(id);