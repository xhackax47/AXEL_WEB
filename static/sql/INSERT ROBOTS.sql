INSERT INTO public."WebAXEL_robot" (
    nom,
    model,
    utilisation,
    date_ajout,
	description,
	doc,
	image,
	nb_vues
)
VALUES
    (
        'Softbank Robotics : NAO',
        'AL-05.b',
        'Educative / Ludique',
        NOW(),
		'NAO est un robot humanoïde français, autonome et programmable, initialement développé par la société Aldebaran Robotics2, une start-up française située à Paris, rachetée par le groupe japonais SoftBank Group en 2015 qui la renomme en SoftBank Robotics3.
Le 15 août 2007, Nao remplace le chien robot Aibo de Sony en tant que robot utilisé dans la RoboCup Standard Platform League (SPL), une compétition internationale de robots joueurs de football4. Nao a été utilisé dans la RoboCup 2008 et 2009, et le NaoV3R a été choisi comme plate-forme pour le SPL à la RoboCup 20105.
Plusieurs versions du robot ont été déployées depuis 2008. Le Nao Academics Edition a été développé pour les universités et les laboratoires à des fins de recherche et d''éducation. Il a été mis à la disposition des institutions en 2008 et du grand public en 2011. Diverses mises à jour de la plate-forme Nao ont été publiées depuis, notamment la Nao Next Gen 2011 et la Nao Evolution 20146,7.
Les robots Nao ont été utilisés à des fins de recherche et d''éducation dans de nombreuses institutions académiques du monde entier. En 2015, plus de 5 000 unités Nao sont utilisées dans plus de 50 pays.',
		'static/robots/NAO.pdf',
		'/static/img/robots/nao.jpg',
		0
    ),
    (
        'Cyberdyne Systems : T-801',
        'Model 101',
		'Militaire',
        NOW(),
        'Le T-800 est un Cyborg pour CYBernétique micro ORGanisme. Il a officiellement été créé par l''ordinateur Skynet en 2029 pour lutter contre la résistance humaine croissante. Sa déclinaison dans le Cyberdyne Systems est série T-800 / T-850. Prototype à l''origine créé par l’intelligence artificielle militaire Skynet (l''ordinateur central du réseau de défense des États-Unis, qui crée et contrôle les machines après la guerre nucléaire), il est utilisé en 2029 dans un monde futuriste post-apocalyptique dans les missions d''infiltration et d''élimination de la résistance humaine en lutte contre Skynet.\r\n\r\nLe Terminator, ou ses groupements d''escouades, sont déployés sur le terrain en tant que cyborgs androïdes. Cette unité entièrement autonome est programmée pour s''infiltrer et tuer. Ces principales cibles sont les membres de la résistance humaine dirigée par John Connor et les survivants de la population civile dans la guerre d''extermination de l''humanité qui a suivi la prise de pouvoir de Skynet.\r\n\r\nDans Terminator, Skynet, acculé sur la défensive et n''arrivant pas à éliminer définitivement la résistance humaine menée par John Connor en 2029, renvoie à travers le temps en mai 1984, le modèle 001 au moyen d''une arme temporelle tactique. Celui ci a alors pour mission d''éliminer la mère de John, Sarah Connor avant qu''elle ne l''ait conçu, afin d''« effacer » la présence de John Connor en 2029 par un avortement rétroactif.\r\n\r\nAu départ, machine conçue pour terminer l''humain, le personnage interprété par Schwarzenegger évoluera à partir du film Terminator 2 : Le Jugement dernier (1991) en devenant le protecteur de John Connor ou de Sarah Connor, reprogrammé depuis le futur pour les défendre à chaque fois contre d''autres types de Terminators plus sophistiqués.',
		'static/robots/T-800.pdf',
		'/static/img/robots/t-801.jfif',
		0
    ),
    (
        'Boston Dynamics : Atlas',
        'Model 2019',
		'Militaire, Recherche et Secours',
        NOW(),
        'Atlas est un robot de type androïde principalement développé par Boston Dynamics, sous financement et surveillance de la Defense Advanced Research Projects Agency (DARPA). Il mesure 1,50 m et est conçu pour diverses tâches de recherche et sauvetage, il a été dévoilé au public le 11 juillet 20131. Le développement d''Atlas fait partie du Darpa Robotics Challenge.
En 2016, une vidéo présentant une évolution du robot est diffusée par Boston Dynamics. Ce modèle d'' 1,50 m et 75 kg peut porter des paquets, ouvrir des portes mais aussi se relever quand on le pousse ou qu''il est déséquilibré.
Le 16 novembre 2017, une vidéo mise en ligne par Boston Dynamics sur leur chaîne YouTube démontre l''agilité du robot Atlas : celui-ci exécute une série de sauts à pieds joints ainsi qu''un salto arrière.',
		'/static/robots/Atlas.pdf',
		'/static/img/robots/atlas.jpg',
		0
    );