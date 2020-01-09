INSERT INTO public."WebAXEL_dataset" (
    nom,
    date_ajout,
    description,
	dataset,
	source
)
VALUES
    (
        'Airport database',
        NOW(),
        'En janvier 2017, la base de données des aéroports OpenFlights contient plus de 10 000 aéroports, gares ferroviaires et terminaux de ferry dans le monde entier, comme le montre la carte ci-dessus. Chaque entrée contient les informations suivantes :

ID de l''aéroport Identificateur unique d''OpenFlights pour cet aéroport.
Nom Nom de l''aéroport. Peut ou non contenir le nom de la ville.
Ville Ville principale desservie par l''aéroport. Peut être épelé différemment du nom.
Pays Pays ou territoire où l''aéroport est situé. Voir countries.dat pour le renvoi aux codes de l''ISO 3166-1.
Code IATA à 3 lettres. Nul si non attribué/inconnu.
OACI Code OACI à 4 lettres.
Nul s''il n''est pas assigné.
Latitude Degrés décimaux, généralement à six chiffres significatifs. Négatif est le Sud, positif est le Nord.
Longitude Degrés décimaux, habituellement jusqu''à six chiffres significatifs. Négatif est l''ouest, positif est l''est.
Altitude En pieds.
Fuseau horaire Heures décalées par rapport à UTC. Les heures fractionnaires sont exprimées en décimales, par exemple, l''Inde est à 5,5.
DST Heure d''été. L''une des valeurs suivantes : E (Europe), A (US/Canada), S (Amérique du Sud), O (Australie), Z (Nouvelle-Zélande), N (aucune) ou U (inconnue). Voir aussi : Aide : Temps
Fuseau horaire de la base de données Tz Fuseau horaire au format "tz" (Olson), par exemple "America/Los_Angeles".
Type Type de l''aéroport. Valeur "airport" pour les aérogares, "station" pour les gares ferroviaires, "port" pour les gares maritimes et "unknown" si non connu. Dans airports.csv, seul le type=aéroport est inclus.
Source Source de ces données. " OurAirports " pour les données provenant de OurAirports, " Legacy " pour les anciennes données non appariées à OurAirports (surtout DAFIF), " User " pour les contributions des utilisateurs non vérifiées. Dans airports.csv, seule la source = NosAéroports est incluse.
Les données sont encodées en UTF-8.

Note : Les règles relatives à l''heure d''été changent d''une année à l''autre et d''un pays à l''autre. Les données actuelles sont une approximation pour 2009, construite au niveau du pays. La plupart des aéroports des régions sans DST dans les pays qui observent généralement le DST (p. ex. AL, HI aux États-Unis, NT, QL en Australie, certaines parties du Canada) sont marqués de façon incorrecte.',
    	'static/datasets/airports-extended.dat',
		'https://openflights.org/data.html'
	),
	(
        'Base officielle des codes postaux',
        NOW(),
        'Fichier de correspondance entre les codes communes (INSEE) et les codes postaux au format csv.

Ce fichier comprend :

Le code commune INSEE
Le nom de la commune
Le code postal
Le libellé d’acheminement
La ligne 5 de l''adresse (précision de l''ancienne commune ou du lieu-dit)
Il correspond aux codes postaux de France (métropole et DOM), ceux des TOM, ainsi que MONACO.

Note aux réutilisateurs: les contours géographiques des communes, à partir de leurs codes INSEE, sont aussi disponibles sur https://www.data.gouv.fr/fr/.

Vous découvrirez des formats de fichiers supplémentaires, des outils de visualisation et des API sur https://datanova.legroupe.laposte.fr.',
    	'static/datasets/laposte_hexasmal.csv',
		'https://www.data.gouv.fr/en/datasets/base-officielle-des-codes-postaux/'
	),
	(
        'Titanic : Apprendre du désastre par la machine',
        NOW(),
        'Le naufrage du Titanic est l''un des naufrages les plus tristement célèbres de l''histoire.

Le 15 avril 1912, lors de son premier voyage, le RMS Titanic, considéré comme " insubmersible ", a coulé après avoir heurté un iceberg. Malheureusement, il n''y avait pas assez de canots de sauvetage pour tout le monde à bord, ce qui a entraîné la mort de 1502 des 2224 passagers et membres d''équipage.

Bien qu''il y ait eu une certaine part de chance pour survivre, il semble que certains groupes de personnes aient eu plus de chances de survivre que d''autres.

Dans le cadre de ce défi, nous vous demandons de construire un modèle prédictif qui répond à la question : "À l''aide des données sur les passagers (nom, âge, sexe, classe socio-économique, etc.), vous devez construire un modèle prédictif qui répond à la question suivante : " Quelles sortes de personnes étaient plus susceptibles de survivre ?',
    	'static/datasets/titanic.csv',
		'https://www.kaggle.com/c/titanic/data'
	);