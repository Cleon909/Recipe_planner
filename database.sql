
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
    amount INTEGER NOT NULL,
    unit VARCHAR(10) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (ingredients_id) REFERENCES ingredients(id) 
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
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    prep_description VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (ingredients_id) REFERENCES ingredients(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS cuisine (
    id INTEGER NOT NULL AUTO_INCREMENT,
    cuisine_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `recipes` VALUES (1, 'Pea and Cauliflower Curry', 'Crush the chillies and ginger together with a pinch of salt to make fine masala paste. /n Heat the oil, cumin and mustard seeds. When the mustard seeds begin to pop reduce heat to low and add the asafetida /n Add the cauliflower , return heat to medium and stir in the masala paste, turmeric, ground coriander, salt and sugar. /n Cover the pan and cook for 8-10 minutes, stirring every few minutes. /n Stir in the peas and the and tomato, cover the pan and cook fro another for a further 3-5 minutes. /n Remove from the heat and sprinkle with chopped coriander. /n Leave to rest for at least 5 minutes.', 'Curry');

