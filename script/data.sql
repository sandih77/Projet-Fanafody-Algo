USE algo_fanafody;

-- Medicaments
INSERT INTO medicament (nom, prix) VALUES ('Paracetamol', 4500.00);
INSERT INTO medicament (nom, prix) VALUES ('Ibuprofene', 6000.00);
INSERT INTO medicament (nom, prix) VALUES ('Amoxicilline', 9000.00);

-- Symptomes
INSERT INTO symptome (nom) VALUES ('Fievre');
INSERT INTO symptome (nom) VALUES ('Maux de tete');
INSERT INTO symptome (nom) VALUES ('Toux');

-- Prescriptions
INSERT INTO prescription (code_prescription, budget) VALUES ('P-2026-001', 25000.00);
INSERT INTO prescription (code_prescription, budget) VALUES ('P-2026-002', 32000.00);

-- Relations medicament <-> symptome
INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES (1, 1, 85.00);
INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES (1, 2, 74.50);
INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES (2, 2, 80.00);
INSERT INTO param_medicament (medicament_id, symptome_id, efficacite) VALUES (3, 3, 76.00);

-- Relations prescription <-> symptome
INSERT INTO param_prescription (prescription_id, symptome_id, gravite) VALUES (1, 1, 8.00);
INSERT INTO param_prescription (prescription_id, symptome_id, gravite) VALUES (1, 2, 6.50);
INSERT INTO param_prescription (prescription_id, symptome_id, gravite) VALUES (2, 3, 7.00);