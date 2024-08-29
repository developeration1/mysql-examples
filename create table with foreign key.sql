USE game_store;
CREATE TABLE games (
	game_id INT PRIMARY KEY auto_increment,
    game_title varchar(50),
    price FLOAT(4, 2),
    language_id INT NOT NULL,
    os_id INT NOT NULL,
    company_id INT NOT NULL,
    genre_id INT NOT NULL,
    director_id INT NOT NULL,
    FOREIGN KEY (language_id) REFERENCES languages(language_id),
    FOREIGN KEY (os_id) REFERENCES os(os_id),
    FOREIGN KEY (company_id) REFERENCES companies(company_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id),
    FOREIGN KEY (director_id) REFERENCES persons(person_id)
);