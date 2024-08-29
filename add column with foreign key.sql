USE game_store;
ALTER TABLE companies
ADD COLUMN director_id INT,
ADD FOREIGN KEY (director_id) REFERENCES persons(person_id);