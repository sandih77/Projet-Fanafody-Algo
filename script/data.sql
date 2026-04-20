USE algo_fanafody;

-- Medicaments
INSERT INTO medicament (nom, prix) VALUES ('Paracetamol', 4500.00);
INSERT INTO medicament (nom, prix) VALUES ('Ibuprofene', 6000.00);
INSERT INTO medicament (nom, prix) VALUES ('Amoxicilline', 9000.00);

-- Symptomes
INSERT INTO symptome (nom) VALUES ('Kibo');
INSERT INTO symptome (nom) VALUES ('Caca');
INSERT INTO symptome (nom) VALUES ('Maux de tete');
INSERT INTO symptome (nom) VALUES ('Temperature');
INSERT INTO symptome (nom) VALUES ('Fatigue');
INSERT INTO symptome (nom) VALUES ('Lelo');

-- Prescriptions
INSERT INTO prescription (code_prescription, budget) VALUES ('P-2026-001', 10000.00);
INSERT INTO prescription (code_prescription, budget) VALUES ('P-2026-002', 6000.00);
INSERT INTO prescription (code_prescription, budget) VALUES ('P-2026-003', 4000.00);

-- Relations medicament <-> symptome
INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES (1, 1, 85.00);
INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES (1, 2, 74.50);
INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES (2, 2, 80.00);
INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES (3, 3, 76.00);

-- Relations prescription <-> symptome
INSERT INTO param_prescription (prescription_id, symptome_id, gravite) VALUES (1, 1, 8.00);
INSERT INTO param_prescription (prescription_id, symptome_id, gravite) VALUES (1, 2, 6.50);
INSERT INTO param_prescription (prescription_id, symptome_id, gravite) VALUES (2, 3, 7.00);


INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES

-- Paracetamol
(1,1,5),
(1,2,4),

-- Ibuprofene
(2,1,4),
(2,2,5),

-- Aspirine
(3,1,3),
(3,2,4),

-- Doliprane
(4,1,5),
(4,2,3),

-- Fervex
(5,1,4),
(5,3,3),

-- Actifed
(6,3,5),

-- Efferalgan
(7,1,4),
(7,2,4),

-- Spasfon
(8,2,5),

-- Codoliprane
(9,2,6),
(9,1,3),

-- Nurofen
(10,1,4),
(10,2,5);



INSERT INTO param_prescription (prescription_id, symptome_id, gravite) VALUES

-- Prescription 1
(1,1,7),
(1,3,5),
(1,2,6),

-- Prescription 2
(2,1,4),
(2,3,6),
(2,2,3),

-- Prescription 3
(3,1,5),
(3,3,2),
(3,2,7);