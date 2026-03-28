solve cherche la combinaison qui peut geurir les symptomes avec un budget de façon récursive
Un patient est guéri si symptome <= 0
donc on soustrait les symptomes avec l efficacité
Exemple 
Bugdet du patient 30000
Symptome 
    - Fièvre 3
    - Maux de tete 5
  
Médicament 
    - paracétamol : 10000
    - doliprane : 15000

param_medicament
    - paracétamol -> fièvre effet 1
    - paracétamol -> maux de tête 2
    - doliprane -> fièvre 3
    - doliprane -> maux de tête 1

Exemple de Combinaison possible
    - 1 doliprane et 2 paracétamol

CREATE DATABASE algo_fanafody;
USE algo_fanafody;

-- 1. Table des médicaments (Ajout du prix)
CREATE TABLE medicament (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prix DECIMAL(10, 2) NOT NULL -- INDISPENSABLE pour le budget
);

-- 2. Table des symptômes
CREATE TABLE symptome (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

-- 3. Relation Médicament <-> Symptôme
CREATE TABLE param_medicament (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medicament_id INT,
    symptome_id INT,
    efficacite DECIMAL(5, 2) NOT NULL, -- (ex: de 0 à 100)
    FOREIGN KEY (medicament_id) REFERENCES medicament(id) ON DELETE CASCADE,
    FOREIGN KEY (symptome_id) REFERENCES symptome(id) ON DELETE CASCADE
);

-- 4. Table des prescriptions (la demande de l'utilisateur)
CREATE TABLE prescription (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code_prescription VARCHAR(255) NOT NULL,
    budget DECIMAL(10, 2) NOT NULL,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. Relation Prescription <-> Symptôme
CREATE TABLE param_prescription (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prescription_id INT,
    symptome_id INT,
    gravite DECIMAL(5, 2) NOT NULL, -- (ex: de 1 à 10)
    FOREIGN KEY (prescription_id) REFERENCES prescription(id) ON DELETE CASCADE,
    FOREIGN KEY (symptome_id) REFERENCES symptome(id) ON DELETE CASCADE
);

les budgts sont celle dans prescription
donc modifie l affichage des ordonnances pour lister les prescriptions mais pas
besoin d entrer les budgets et symptomes comme cela 
