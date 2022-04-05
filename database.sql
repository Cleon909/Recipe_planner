
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER NOT NULL AUTO_INCREMENT,
    recipe_name VARCHAR(100) NOT NULL,
    recipe_description VARCHAR(500), -- this is for calories macros, comments etc
    cuisine_id INT,
    PRIMARY KEY (id)
    FOREIGN KEY (cuisine_id) REFERNCES cuisine(id),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 

CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER NOT NULL AUTO_INCREMENT,
    ingredient_name VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS quantity (
    id INTEGER NOT NULL AUTO_INCREMENT,
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    ingredient_prep_id INTEGER NOT,
    amount INTEGER NOT NULL,
    unit VARCHAR(10) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (ingredients_id) REFERENCES ingredients(id)
    FOREIGN KEY (ingredient_prep_id) REFERENCES ingredient_prep(id), 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS method (
    id INTEGER NOT NULL AUTO_INCREMENT,
    recipe_id INT NOT NULL,
    step_num INT NOT NULL,
    step VARCHAR(200) NOT NULL,  
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS ingredient_prep (
    id INTEGER NOT NULL AUTO_INCREMENT,
    prep_description VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS cuisine (
    id INTEGER NOT NULL AUTO_INCREMENT,
    cuisine_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `recipes` VALUES (1, 'Pea and Cauliflower Curry',1);
INSERT INTO 'ingredients' VALUES (1, 'sunflower oil'), (2, 'cuin seeds'), (3, 'bown mustard seeds'), (4, 'asafetida'), (5, 'cauliflower'), (6, 'turmeric'), (7, 'ground coriander'), (8, 'salt'), (9, 'sugar'), (10, 'frozen peas'), (11, 'medium tomato'), (12, 'fresh coriander') (13, 'fresh green chillies'), (14, 'root ginger');
INSERT INTO 'method' VALUES (1, 1, 1, 'Crush the chillies and ginger together with a pinch of salt to make a fine masala paste'), (2, 1, 2, 'Heat the oil in non-stick pan over a medium heat for 30s, then add the cumin and mustard seeds. When the mustard seeds start to pop reduce the heat and stir in teh asafetida '), (3, 1, 3, 'Add the cauliflower and return the heat to medium. Stir in the masala paste, turmeric, ground coriander, salt, and sugar. Cover the pan and leave to cook for 8-10 minutes, stirring every few minutes.'), (4,1,4, 'stir in the peas and tomato and cook for a further 3-5 minutes'), (5,1,5, 'Remove from the heat and sprinkle with the chopped coriander. Leave for 5 minutes to let flavours develop');
INSERT INTO 'ingredient_prep' VALUES (1, 'chopped'), (2, 'finely chopped'), (3, 'roughly chopped');
INSERT INTO 'cuisine' VALUES (1, 'curry'), (2, 'Salad');
INSERT INTO 'quantity' VALUES () 
