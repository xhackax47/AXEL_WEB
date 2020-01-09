INSERT INTO public."WebAXEL_document" (
    titre,
    date_ajout,
    auteur,
    description,
	document,
	nb_vues
)
VALUES
    (
        'Introduction à la robotique',
        NOW(),
        'Laëtitia Matignon',
        'Cours sur Introduction à la robotique - Licence 1ère Année 2011/2012, GREYC-CNRS à l''Université de Caen',
    	'static/docs/coursL1robotique.pdf',
		0
	),
    (
        'Réseaux de Neurones',
        NOW(),
        'Cecile Capponi',
        'Cours sur l''historique et utilisation des réseaux de neurones - Master 1 Informatique à l''Université Aix-Marseille',
    	'static/docs/cours-reseaux-de-neurones.pdf',
		0
	),
    (
        'Perceptron simple et multi-couches',
        NOW(),
        'Nicolas P. Rougier',
        'Cours sur les perceptrons - Master 2 en Sciences Cognitives à l''Université de Bordeaux',
    	'static/docs/Perceptron.pdf',
		0
	),
	(
        'Machine Learning 1',
        NOW(),
        'Christian Wolf',
        'Cours Machine Learning sur les Méthodes avancées en Image et Vidéo - Master 2 Ingénieur Génie Industriel à l''INSA-LYON avec le CNRS',
    	'static/docs/m2r-igi-machinelearning1.pdf',
		0
	),
	(
        'Robotique',
        NOW(),
        'Jean-Louis Boimond',
        'Cours sur la robotique générale - Master 2 Systèmes Automatisés et Génie Informatique à l''ISTIA, Polytech Angers',
    	'static/docs/mastersds_cours_robot_boimond.pdf',
		0
	),
	(
        'Deep Learning et Intelligence Artificielle : mythes et réalités',
        NOW(),
        'Christian Wolf',
        'Cours Deep Learning sur les Méthodes avancées en Image et Vidéo - Master 2 Ingénieur Génie Industriel à l''INSA-LYON avec le CNRS',
    	'static/docs/pres-codeurs-161124.pdf',
		0
	),
	(
        'Robotique Industrielle',
        NOW(),
        'Stäubli Robotics',
        'Documentation des robots Stäubli',
    	'static/docs/robotique_industrielle.pdf',
		0
	),
	(
        'Introduction à l’Intelligence Artificielle',
        NOW(),
        'Marie Lefevre',
        'Cours d''introduction à l''intelligence artificielle - Master 2 Ingénieur Génie Industriel à l''Université Claude Bernard Lyon 1 avec le CNRS',
    	'static/docs/SUR2017-CM-IA.pdf',
		0
	),
	(
        'Premiers pas avec TensorFlow',
        NOW(),
        'Christophe Tilmant',
        'Présentation du deep learning & Mise en oeuvre sur un cas concret - Master 2 Informatique à l''ISIMA - Clermont-Ferrand',
    	'static/docs/Tensorflow_deep_learning.pdf',
		0
	),
	(
        'Deep Learning avec Tensorflow / Keras',
        NOW(),
        'Tanagra Data Mining',
        'Cours Découverte des librairies de Deep Learning Tensorflow / Keras pour Python. Implémentation de perceptrons simples et multicouches dans des problèmes de classement (apprentissage supervisé).',
    	'static/docs/Tensorflow_Keras_Python.pdf',
		0
	),
	(
        'A.X.E.L. / Assistant personnel IA',
        NOW(),
        'Samy Chaabi',
        'Documentation du projet intelligence artificielle A.X.E.L.',
    	'static/docs/Projet_A.X.E.L.docx',
		0
	);