CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER NOT NULL AUTO_INCREMENT,
    ingredient_name VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS cuisine (
    id INTEGER NOT NULL AUTO_INCREMENT,
    cuisine_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER NOT NULL AUTO_INCREMENT,
    recipe_name VARCHAR(100) NOT NULL,
    recipe_description VARCHAR(500), -- this is for calories macros, comments etc
    cuisine_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (cuisine_id) REFERENCES cuisine(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 

CREATE TABLE IF NOT EXISTS quantity (
    id INTEGER NOT NULL AUTO_INCREMENT,
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    ingredient_prep VARCHAR(100),
    amount FLOAT NOT NULL,
    unit VARCHAR(10) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS method (
    id INTEGER NOT NULL AUTO_INCREMENT,
    recipe_id INT NOT NULL,
    step_num INT NOT NULL,
    step VARCHAR(200) NOT NULL,  
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO ingredients VALUES (1, 'sunflower oil'), (2, 'cumin seeds'), (3, 'brown mustard seeds'), (4, 'asafetida'), (5, 'cauliflower'), (6, 'turmeric'), (7, 'ground coriander'), (8, 'salt'), (9, 'sugar'), (10, 'frozen peas'), (11, 'medium tomato'), (12, 'fresh coriander'), (13, 'fresh green chillies'), (14, 'root ginger');
INSERT INTO cuisine VALUES (1, 'curry'), (2, 'Salad');
INSERT INTO recipes VALUES (1, 'Pea and Cauliflower Curry', 'quick and easy curry, no calorie details', 1);
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (1, 1, 1, 100.0, 'ml');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (2, 1, 2, 1.0, 'tsp');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (3, 1, 3, 1.0, 'tsp');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (4, 1, 4, 0.5, 'tsp');
INSERT INTO quantity (id, recipe_id, ingredient_id, ingredient_prep, amount, unit) VALUES (5, 1, 5,'cut into 1cm pieces', 1.0, 'medium');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (6, 1, 6, 1.0, 'tsp');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (7, 1, 7, 1.0, 'tbp');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (8, 1, 8, 1.5, 'tsp');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (9, 1, 9, 1.0, 'tsp');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (10, 1, 10, 400.0, 'grams');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (11, 1, 11, 1.0, 'medium');
INSERT INTO quantity (id, recipe_id, ingredient_id, ingredient_prep, amount, unit) VALUES (12, 1, 12, 'roughly chopped', 1.0, 'handful');
INSERT INTO quantity (id, recipe_id, ingredient_id, amount, unit) VALUES (13, 1, 13, 4.0, 'whole');
INSERT INTO quantity (id, recipe_id, ingredient_id, ingredient_prep, amount, unit) VALUES (14, 1, 14, 'peeled and roughly chopped', 4.0, 'cm');

INSERT INTO method VALUES (1, 1, 1, 'Crush the chillies and ginger together with a pinch of salt to make a fine masala paste'), (2, 1, 2, 'Heat the oil in non-stick pan over a medium heat for 30s, then add the cumin and mustard seeds. When the mustard seeds start to pop reduce the heat and stir in teh asafetida '), (3, 1, 3, 'Add the cauliflower and return the heat to medium. Stir in the masala paste, turmeric, ground coriander, salt, and sugar. Cover the pan and leave to cook for 8-10 minutes, stirring every few minutes.'), (4,1,4, 'stir in the peas and tomato and cook for a further 3-5 minutes'), (5,1,5, 'Remove from the heat and sprinkle with the chopped coriander. Leave for 5 minutes to let flavours develop');
