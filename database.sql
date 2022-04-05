
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    method VARCHAR(1000) NOT NULL,
    cuisine VARCHAR(50) DEFAULT 'unkown',
    ingredient_amount INT,
    calories INT,
    fat INT,
    protein INT,
    carbs INT,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; 

CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE,
    unit VARCHAR(5),
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS junction (
    id INTEGER NOT NULL AUTO_INCREMENT,
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (ingredients_id) REFERENCES ingredients(id) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `recipes` VALUES (1, 'Pea and Cauliflower Curry', 'Crush the chillies and ginger together with a pinch of salt to make fine masala paste. /n Heat the oil, cumin and mustard seeds. When the mustard seeds begin to pop reduce heat to low and add the asafetida /n Add the cauliflower , return heat to medium and stir in the masala paste, turmeric, ground coriander, salt and sugar. /n Cover the pan and cook for 8-10 minutes, stirring every few minutes. /n Stir in the peas and the and tomato, cover the pan and cook fro another for a further 3-5 minutes. /n Remove from the heat and sprinkle with chopped coriander. /n Leave to rest for at least 5 minutes.', 'Curry');

INSERT INTO `papers` VALUES 
(1, 'Nihilism and dialectic appropriation', 1985, 'Advanced Semiotics'), (2, 'Marxist capitalism in the works of Gaiman', 2020, 'The Occult'),  (3, 'Bob Diamond and Metasemiotics in Finance', 2010, 'Computer Science and Etymology'),(4, 'Postpatriarchial libertarianism in the works of Glass', 1999, 'Music and the Movement of the Spheres'),
 (5, 'Reinventing Constructivism: Modernism in the works of Eco', 2018, 'Semiotics and history of Evolution'),  (6, 'A Biography of Eric "Eazy-E" Wright', 1998, 'Biography as the Expression of Power'),(7, 'The Principle Knowledge That God Is Omniscience', 2022, 'Mathematics of the Celestial Heavens'),
 (8, 'An Introduction to the Analysis of Theological Task', 2020, 'Ancient Astronauts'),  (9, 'Precapitalist constructivist theory and postdeconstructive appropriation', 2006, 'Creationist Cosmologies'),(10, 'Precapitalist dematerialism and constructivism', 1970, 'The Occult'),
(11, 'Sartreist absurdity in the works of Gaiman', 1696, 'Advanced Semiotics'),(12, 'Examining the QCD Law in Models of Monopoles: Firewalls', 1066, 'Creationist Cosmologies'),(13, 'Reflexive tactics for algebra, revisited', 1453, 'Ancient Astronauts'),(14, 'Evolution of SASyLF 2008-2021', 453, 'Biography as the Expression of Power'),
(15, 'Bunched Fuzz: Sensitivity for Vector Metrics', 2001, 'Biography as the Expression of Power'),(16, 'Worlds of the Phaedo and the Term', 1875, 'Biography as the Expression of Power'),(17, 'Dark Spirituality as a Symbol Female', 1930, 'Creationist Cosmologies'),
(18, 'Which can Jump Highe, a Car Flea of a Dog Flea?', 2010, 'Music and the Movement of the Spheres'),(19, 'Do Woodpeckers get Headaches?', 2006, 'Mathematics of the Celestial Heavens'),(20, 'The propulsion Paramters of Penguin Poop', 2008, 'Ancient Astronauts');

INSERT INTO `authors` VALUES (1, 1, 7), (2, 2, 7), (3, 3, 5), (4, 4, 3), (5, 5, 19), (6, 6, 9), (7, 7, 8), (8, 8, 4), (9, 9, 20), (10, 10, 19), (11, 11, 18), (12, 12, 17), (13, 13, 16), (14, 14, 15), (15, 15, 14),
(16, 16, 13), (17, 17, 12), (18, 12, 11), (19, 19, 10), (20, 20, 9), (21, 2, 8), (22, 18, 7), (23, 4, 6), (24, 7, 5), (25, 12, 4), (26, 20, 3), (27, 1, 2), (28, 4, 1);
