
# Importation des bibliothèques nécessaires
import random

# Définition des questions et des réponses
questions = [
    {
        "question": "Qui était le premier empereur romain ?",
        "choices": ["A. César", "B. Auguste", "C. Néron", "D. Trajan"],
        "answer": "B"
    },
    {
        "question": "En quelle année a commencé la Première Guerre mondiale ?",
        "choices": ["A. 1912", "B. 1914", "C. 1916", "D. 1918"],
        "answer": "B"
    },

    # Questions sur Toyohisa Shimazu
   {
        "question": "Toyohisa Shimazu a participé à quelle célèbre bataille en 1600 ?",
        "choices": ["A. Bataille de Sekigahara", "B. Bataille de Nagashino", "C. Bataille de Kawanakajima", "D. Bataille de Dan-no-ura"],
        "answer": "A"
    },
   {
        "question": "Toyohisa Shimazu était membre de quel clan japonais ?",
        "choices": ["A. Clan Tokugawa", "B. Clan Shimazu", "C. Clan Oda", "D. Clan Date"],
        "answer": "B"
    },
		{
        "question": "En quelle année Toyohisa Shimazu est-il né ?",
        "choices": ["A. 1560", "B. 1570", "C. 1580", "D. 1590"],
        "answer": "B"
    },
		{
        "question": "Toyohisa Shimazu était le fils de quel seigneur féodal ?",
        "choices": ["A. Shimazu Yohihisa", "B. Shimazu Iehisa", "C. Shimazu Takahisa", "D. Shimazu Tadatsune"],
        "answer": "A"
    },
		{
        "question": "Toyohisa Shimazu a combattu pour quel camp durant la bataille de Sekigahara?",
        "choices": ["A. Camp de l'est", "B. Camp de l'ouest", "C. Camp neutre", "D. Camp étranger"],
        "answer": "B"
    },
		{
        "question": "Quel est le surnom de Toyohisa Shimazu en raison de sa bravoure ?",
        "choices": ["A. Le lion de Tosa", "B. Le tigre de Tosa", "C. Le dragon de kyushu", "D. Le serpent de Shimazu"],
        "answer": "A"
    },
		{
        "question": "Toyohisa Shimazu est mort à quel âge ?",
        "choices": ["A. 30", "B. 40", "C. 50", "D. 50"],
        "answer": "A"
    },
		{
        "question": "Quel était le rôle principal de Toyohisa Shimazu au sein de son clan ?",
        "choices": ["A. Stratége", "B. Archer", "C. Général", "D. Diplomate"],
        "answer": "C"
    },

		# Questions sur Oda Nobunaga
		{
        "question": "Quel clan Oda Nobunaga a-t-il dirigé au cours de sa vie ?",
        "choices": ["A. Clan Takeda", "B. Clan Oda", "C. Clan Tokugawa", "D. Clan Date  "],
        "answer": "B"
    },
    {
        "question": "En quelle année Oda Nobunaga a-t-il pris le contrôle de Kyoto ?",
        "choices": ["A. 1568", "B. 1572", "C. 1580", "D. 1582"],
        "answer": "A"
    },
		{
         "question": "Quel est le célèbre château construit par Oda Nobunaga qui symbolise sa puissance ?",
         "choices": ["A. Château d’Himeji", "B. Château d’Azuchi", "C. Château de Nagoya", "D. Château de Matsumoto"],
         "answer": "B"
	  },
		{
          "question": "Oda Nobunaga est souvent associé à quelle période historique japonaise ?",
          "choices": ["A. Période Heian", "B. Période Sengoku", "C. Période Kamakura", "D. Période Edo"],
          "answer": "B"
    },
		{
          "question": "Quel célèbre général et vassal a continué l'unification du Japon après la mort d'Oda Nobunaga ?",
          "choices": ["A. Tokugawa Ieyasu", "B. Takeda Shingen", "C. Toyotomi Hideyoshi", "D. Uesugi Kenshin"],
          "answer": "C"
    },
		{
          "question": "Oda Nobunaga a utilisé une nouvelle technologie militaire décisive lors de la bataille de Nagashino en 1575. Laquelle ?",
          "choices": ["A. Les arquebuses", "B. Les canons", "C. Les arcs à longue portée", "D. Les navires blindés"],
          "answer": "A"
    },
		{
          "question": "Quel était le surnom souvent attribué à Oda Nobunaga pour son style de leadership ?",
          "choices": ["A. Le Tigre de Kai", "B. Le Démon de la guerre", "C. Le Roi démon du sixième ciel", "D. Le Dragon de Yamato"],
          "answer": "C"
    },
		{
          "question": "Quelle rébellion religieuse Oda Nobunaga a-t-il écrasé pour asseoir son pouvoir ?",
          "choices": ["A. Rébellion Ikko-Ikki", "B. Rébellion Meiji", "C. Rébellion Boshin", "D. Rébellion Genpei"],
          "answer": "A"
    },
		{
          "question": "Qui a trahi et forcé Oda Nobunaga à se suicider au temple Honnō-ji en 1582 ?",
          "choices": ["A. Akechi Mitsuhide", "B. Tokugawa Ieyasu", "C. Takeda Katsuyori", "D. Uesugi Kenshin"],
          "answer": "A"
    },
		{
          "question": "Quel proverbe célèbre Oda Nobunaga représente-t-il dans l'histoire japonaise, lié à sa détermination ?",
          "choices": ["A. “Celui qui plante une graine récolte son fruit.”", "B. “Si l’oiseau ne chante pas, force-le à chanter.”", "C. “L’unité est la clé du succès.”", "D. “Le temps attend les courageux.”"],
          "answer": "B"
    },

		# Questions sur Nasu Yoichi Suketaka
		{
            "question": "Nasu Yoichi  Suketaka est célèbre pour avoir abattu une cible exceptionnelle lors de quelle bataille ?",
            "choices": ["A. Bataille de Dan-no-ura", "B. Bataille de Uji", "C. Bataille de Yashima", "D. Bataille de Kawanakajima"],
            "answer": "C"
    },
		{
            "question": "Quelle était la cible légendaire que Nasu Yoichi Suketaka a abattue lors de la bataille de Yashima ?",
            "choices": ["A. Un cerf", "B. Un drapeau", "C. Un éventail", "D. Un bateau"],
            "answer": "C"
    },
		{
            "question": "À quel clan Nasu Yoichi Suketaka était-il affilié ?",
            "choices": ["A. Clan Taira", "B. Clan Minamoto", "C. Clan Fujiwara", "D. Clan Hojo"],
            "answer": "B"
    },
		{
            "question": "En quelle année s'est déroulée la bataille de Yashima ?",
            "choices": ["A. 1180", "B. 1182", "C. 1185", "D. 1187"],
            "answer": "C"
    },
		{
            "question": "Quel était le rôle principal de Nasu Yoichi Suketaka dans la guerre de Genpei ?",
            "choices": ["A. Stratège", "B. Archer", "C. Cavalier", "D. Diplomate"],
            "answer": "B"
    },
		{
            "question": "Quel texte historique raconte les exploits de Nasu Yoichi Suketaka ?",
            "choices": ["A. Kojiki", "B. Nihon Shoki", "C. Heike Monogatari", "D. Genji Monogatari"],
            "answer": "C"
    },
		{
            "question": "Quel âge avait Nasu Yoichi Suketaka lorsqu'il a accompli son exploit légendaire ?",
            "choices": ["A. 16 ans", "B. 18 ans", "C. 20 ans", "D. 22 ans"],
            "answer": "A"
    },
		{
            "question": "Après la guerre de Genpei, quel titre a été accordé à Nasu Yoichi Suketaka ?",
            "choices": ["A. Daimyo de Tottori", "B. Shogun", "C. Gouverneur de Kyoto", "D. Moine bouddhiste"],
            "answer": "A"
    },
		{
            "question": "Quel était le but de l'éventail placé par les Taira lors de la bataille de Yashima ?",
            "choices": ["A. Provoquer les Minamoto", "B. Protéger les navires", "C. Signaler une trêve", "D. Décorer les bateaux"],
            "answer": "A"
        },
				{
            "question": "Où Nasu Yoichi Suketaka est-il supposé être mort ?",
            "choices": ["A. Kyoto", "B. Kobe", "C. Tokyo", "D. Osaka"],
            "answer": "B"
        },

#Hannibal Barca 
				{
    "questions": [
        {
            "question": "Hannibal Barca est célèbre pour avoir traversé quelle chaîne de montagnes avec ses éléphants ?",
            "choices": ["A. Les Andes", "B. Les Pyrénées", "C. Les Alpes", "D. Les Apennins"],
            "answer": "C"
        },
				{
            "question": "Quel empire Hannibal Barca a-t-il combattu durant les guerres puniques ?",
            "choices": ["A. L'Égypte", "B. La Grèce", "C. La Perse", "D. Rome"],
            "answer": "D"
        },
{
            "question": "Quelle bataille célèbre Hannibal a-t-il remportée contre les Romains en 216 avant J.-C. ?",
            "choices": ["A. Bataille du Lac Trasimène", "B. Bataille de Zama", "C. Bataille de Cannes", "D. Bataille d'Agrigente"],
            "answer": "C"
        },
{
            "question": "À quel âge Hannibal Barca est-il devenu commandant en chef de l'armée carthaginoise ?",
            "choices": ["A. 18 ans", "B. 21 ans", "C. 25 ans", "D. 30 ans"],
            "answer": "B"
        },
{
            "question": "Dans quel pays Hannibal Barca a-t-il trouvé refuge après la chute de Carthage ?",
            "choices": ["A. Égypte", "B. Perse", "C. Syrie", "D. Arménie"],
            "answer": "C"
        },
{
            "question": "Combien d'éléphants Hannibal aurait-il amenés lors de sa traversée des Alpes ?",
            "choices": ["A. 37", "B. 100", "C. 50", "D. 23"],
            "answer": "A"
        },
{
            "question": "Quel est le nom du père de Hannibal qui lui a inculqué la haine envers Rome ?",
            "choices": ["A. Hamilcar Barca", "B. Hasdrubal le Beau", "C. Himilcon", "D. Magon Barca"],
            "answer": "A"
        },
{
            "question": "Quelle bataille a marqué la défaite finale de Hannibal contre Rome ?",
            "choices": ["A. Bataille de Cannes", "B. Bataille de Zama", "C. Bataille du Lac Trasimène", "D. Bataille de Metaurus"],
            "answer": "B"
        },
{
            "question": "Quel général romain a vaincu Hannibal lors de la bataille de Zama ?",
            "choices": ["A. Fabius Maximus", "B. Marcus Agrippa", "C. Publius Scipion l'Africain", "D. Lucius Cornelius Sulla"],
            "answer": "C"
        },
{
            "question": "Hannibal Barca appartient à quelle civilisation antique ?",
            "choices": ["A. Les Étrusques", "B. Les Grecs", "C. Les Phéniciens", "D. Les Carthaginois"],
            "answer": "D"
        },
#Sundance kid 

{
    "questions": [
        {
            "question": "Quel était le vrai nom de Sundance Kid ?",
            "choices": ["A. Harry Alonzo Longabaugh", "B. Robert Leroy Parker", "C. Harvey Logan", "D. Ben Kilpatrick"],
            "answer": "A"
        },
{
            "question": "Dans quel gang Sundance Kid était-il membre ?",
            "choices": ["A. Dalton Gang", "B. James-Younger Gang", "C. Wild Bunch", "D. Hole-in-the-Wall Gang"],
            "answer": "C"
        },
{
            "question": "Sundance Kid a été emprisonné pour la première fois pour quel crime ?",
            "choices": ["A. Braquage de banque", "B. Vol de train", "C. Vol de cheval", "D. Meurtre"],
            "answer": "C"
        },
{
            "question": "Avec qui Sundance Kid a-t-il formé un duo célèbre ?",
            "choices": ["A. Jesse James", "B. Billy the Kid", "C. Butch Cassidy", "D. Kid Curry"],
            "answer": "C"
        },
{
            "question": "Où Sundance Kid et Butch Cassidy se sont-ils réfugiés pour échapper aux détectives Pinkerton ?",
            "choices": ["A. Argentine", "B. Mexique", "C. Canada", "D. Bolivie"],
            "answer": "D"
        },
{
            "question": "Quelle était la spécialité de Sundance Kid au sein du gang Wild Bunch ?",
            "choices": ["A. Stratège", "B. Tireur d'élite", "C. Cavalier", "D. Dynamiteur"],
            "answer": "B"
        },
{
            "question": "En quelle année Sundance Kid est-il présumé mort ?",
            "choices": ["A. 1906", "B. 1907", "C. 1908", "D. 1909"],
            "answer": "C"
        },
{
            "question": "Quel était le surnom de Sundance Kid avant de rejoindre le gang Wild Bunch ?",
            "choices": ["A. The Tall Texan", "B. The Kid", "C. The Sundance Wrangler", "D. Aucun surnom"],
            "answer": "D"
        },
{
            "question": "Quel détective célèbre a poursuivi Sundance Kid et son gang ?",
            "choices": ["A. Allan Pinkerton", "B. Wyatt Earp", "C. Bat Masterson", "D. Pat Garrett"],
            "answer": "A"
        },
{
            "question": "Quel film célèbre raconte l'histoire de Sundance Kid et Butch Cassidy ?",
            "choices": ["A. The Wild Bunch", "B. Butch Cassidy and the Sundance Kid", "C. True Grit", "D. Unforgiven"],
            "answer": "B"
        },
# Jeanne d'Arc 
{
    "questions": [
        {
            "question": "En quelle année Jeanne d'Arc est-elle née ?",
            "choices": ["A. 1402", "B. 1412", "C. 1422", "D. 1432"],
            "answer": "B"
        },
{
            "question": "Quel surnom est souvent attribué à Jeanne d'Arc ?",
            "choices": ["A. La Guerrière de France", "B. La Sainte de Domrémy", "C. La Pucelle d'Orléans", "D. La Dame de Reims"],
            "answer": "C"
        },
{
            "question": "Quel roi Jeanne d'Arc a-t-elle aidé à monter sur le trône ?",
            "choices": ["A. Charles VI", "B. Louis XI", "C. Charles VII", "D. Philippe le Bon"],
            "answer": "C"
        },
{
            "question": "Quelle bataille Jeanne d'Arc a-t-elle remportée en 1429, changeant le cours de la guerre de Cent Ans ?",
            "choices": ["A. Bataille de Patay", "B. Bataille de Crécy", "C. Bataille d'Azincourt", "D. Bataille de Poitiers"],
            "answer": "A"
        },
{
            "question": "Dans quelle ville Jeanne d'Arc a-t-elle été capturée en 1430 ?",
            "choices": ["A. Paris", "B. Compiègne", "C. Rouen", "D. Orléans"],
            "answer": "B"
        },
{
            "question": "Quel tribunal a condamné Jeanne d'Arc à mort ?",
            "choices": ["A. Tribunal royal", "B. Tribunal militaire", "C. Tribunal ecclésiastique", "D. Tribunal populaire"],
            "answer": "C"
        },
{
            "question": "Quel était le principal chef militaire anglais contre lequel Jeanne d'Arc a combattu ?",
            "choices": ["A. Richard III", "B. Henri VI", "C. John Talbot", "D. Édouard IV"],
            "answer": "C"
        },
{
            "question": "Quel était le motif officiel de la condamnation de Jeanne d'Arc ?",
            "choices": ["A. Trahison", "B. Sorcellerie", "C. Hérésie", "D. Espionnage"],
            "answer": "C"
        },
{
            "question": "En quelle année Jeanne d'Arc a-t-elle été canonisée ?",
            "choices": ["A. 1804", "B. 1909", "C. 1920", "D. 1945"],
            "answer": "C"
        },
{
            "question": "Dans quelle ville Jeanne d'Arc a-t-elle été brûlée vive ?",
            "choices": ["A. Paris", "B. Reims", "C. Rouen", "D. Orléans"],
            "answer": "C"
        },
# gilles de rais 
{
    "questions": [
        {
            "question": "Quel était le titre de noblesse de Gilles de Rais ?",
            "choices": ["A. Duc de Bretagne", "B. Baron de Retz", "C. Comte d'Anjou", "D. Prince de Poitiers"],
            "answer": "B"
        },
{
            "question": "Gilles de Rais était un compagnon d'armes de quelle figure historique ?",
            "choices": ["A. Charles VII", "B. Jeanne d'Arc", "C. Louis XI", "D. Bertrand du Guesclin"],
            "answer": "B"
        },
{
            "question": "Dans quelle guerre Gilles de Rais a-t-il combattu ?",
            "choices": ["A. Guerre de Cent Ans", "B. Guerre des Deux Roses", "C. Guerre de Succession de Bretagne", "D. Guerre de Cent Jours"],
            "answer": "A"
        },
{
            "question": "Quel roi de France a nommé Gilles de Rais maréchal de France ?",
            "choices": ["A. Charles VI", "B. Charles VII", "C. Louis XI", "D. Philippe le Bon"],
            "answer": "B"
        },
{
            "question": "Quel château était l'une des principales résidences de Gilles de Rais ?",
            "choices": ["A. Château de Chambord", "B. Château de Tiffauges", "C. Château de Vincennes", "D. Château de Blois"],
            "answer": "B"
        },
{
            "question": "Quel célèbre conte est inspiré des crimes de Gilles de Rais ?",
            "choices": ["A. Le Petit Chaperon Rouge", "B. La Belle au bois dormant", "C. Barbe Bleue", "D. Le Chat Botté"],
            "answer": "C"
        },
{
            "question": "En quelle année Gilles de Rais a-t-il été exécuté ?",
            "choices": ["A. 1435", "B. 1440", "C. 1450", "D. 1465"],
            "answer": "B"
        },
{
            "question": "Quel type de crime Gilles de Rais a-t-il été accusé d'avoir commis ?",
            "choices": ["A. Trahison", "B. Sorcellerie", "C. Meurtres et abus d'enfants", "D. Espionnage"],
            "answer": "C"
        },
{
            "question": "Quel tribunal a jugé Gilles de Rais ?",
            "choices": ["A. Tribunal royal", "B. Tribunal militaire", "C. Tribunal ecclésiastique", "D. Tribunal populaire"],
            "answer": "C"
        },
{
            "question": "Dans quelle ville Gilles de Rais a-t-il été exécuté ?",
            "choices": ["A. Paris", "B. Nantes", "C. Orléans", "D. Bordeaux"],
            "answer": "B"
        }
# Akechi Mitsubishi 
{
    "questions": [
        {
            "question": "Akechi Mitsuhide est célèbre pour avoir trahi quel daimyo japonais ?",
            "choices": ["A. Tokugawa Ieyasu", "B. Takeda Shingen", "C. Oda Nobunaga", "D. Uesugi Kenshin"],
            "answer": "C"
        },
{
            "question": "Quelle bataille a marqué la fin du règne d'Akechi Mitsuhide ?",
            "choices": ["A. Bataille de Sekigahara", "B. Bataille de Nagashino", "C. Bataille de Kawanakajima", "D. Bataille de Yamazaki"],
            "answer": "D"
        },
{
            "question": "Quel était le surnom donné à Akechi Mitsuhide après sa courte prise de pouvoir ?",
            "choices": ["A. Le traître de Kyoto", "B. Le shogun de treize jours", "C. Le renégat du Kansai", "D. Le fantôme de Yamazaki"],
            "answer": "B"
        },
{
            "question": "En quelle année Akechi Mitsuhide a-t-il orchestré l'attaque du temple Honnō-ji ?",
            "choices": ["A. 1575", "B. 1580", "C. 1582", "D. 1585"],
            "answer": "C"
        },
{
            "question": "Quel célèbre général a vengé Oda Nobunaga en battant Akechi Mitsuhide ?",
            "choices": ["A. Tokugawa Ieyasu", "B. Toyotomi Hideyoshi", "C. Takeda Katsuyori", "D. Minamoto no Yoshitsune"],
            "answer": "B"
        },
{
            "question": "Quel était le rôle d'Akechi Mitsuhide avant de trahir Oda Nobunaga ?",
            "choices": ["A. Conseiller militaire", "B. Gouverneur de Kyoto", "C. Diplomate impérial", "D. Chef des armées"],
            "answer": "B"
        },
{
            "question": "Quelle province Akechi Mitsuhide a-t-il gouvernée sous Oda Nobunaga ?",
            "choices": ["A. Province de Mino", "B. Province de Tamba", "C. Province de Kai", "D. Province de Satsuma"],
            "answer": "B"
        },
{
            "question": "Comment Akechi Mitsuhide est-il mort après sa défaite à Yamazaki ?",
            "choices": ["A. Seppuku", "B. Assassiné par des paysans", "C. Exécuté par Toyotomi Hideyoshi", "D. Mort en exil"],
            "answer": "B"
        },
{
            "question": "Quel était le lien entre Akechi Mitsuhide et la cérémonie du thé japonaise ?",
            "choices": ["A. Il était un grand amateur de thé", "B. Il a interdit la cérémonie du thé", "C. Il a fondé une école de thé", "D. Il a utilisé le thé comme poison politique"],
            "answer": "A"
        },
{
            "question": "Quel château Akechi Mitsuhide a-t-il contrôlé avant sa trahison ?",
            "choices": ["A. Château de Himeji", "B. Château de Sakamoto", "C. Château de Nagoya", "D. Château de Matsumoto"],
            "answer": "B"
        },
# li Naomasa 
{
    "questions": [
        {
            "question": "Ii Naomasa était un général sous quel shogun japonais ?",
            "choices": ["A. Oda Nobunaga", "B. Toyotomi Hideyoshi", "C. Tokugawa Ieyasu", "D. Takeda Shingen"],
            "answer": "C"
        },
{
            "question": "À quelle célèbre bataille Ii Naomasa a-t-il joué un rôle clé en 1600 ?",
            "choices": ["A. Bataille de Nagashino", "B. Bataille de Kawanakajima", "C. Bataille de Sekigahara", "D. Bataille de Yamazaki"],
            "answer": "C"
        },
{
            "question": "Quel était le surnom donné aux troupes de Ii Naomasa en raison de leur armure rouge ?",
            "choices": ["A. Les Loups Rouges", "B. Les Dragons de Kyoto", "C. Les Diables Rouges", "D. Les Ombres Sanglantes"],
            "answer": "C"
        },
{
            "question": "Quel était le rôle de Ii Naomasa après la victoire de Tokugawa Ieyasu ?",
            "choices": ["A. Gouverneur de Kyoto", "B. Daimyo de Hikone", "C. Conseiller impérial", "D. Shogun"],
            "answer": "B"
        },
{
            "question": "Quelle blessure Ii Naomasa a-t-il reçue à Sekigahara qui a conduit à sa mort prématurée ?",
            "choices": ["A. Coup d'épée", "B. Flèche empoisonnée", "C. Balle d'arquebuse", "D. Chute de cheval"],
            "answer": "C"
        },
{
            "question": "Quel clan Ii Naomasa a-t-il dirigé après la mort de son prédécesseur ?",
            "choices": ["A. Clan Takeda", "B. Clan Oda", "C. Clan Ii", "D. Clan Tokugawa"],
            "answer": "C"
        },
{
            "question": "Quel célèbre général japonais a inspiré Ii Naomasa à utiliser des armures rouges pour ses troupes ?",
            "choices": ["A. Uesugi Kenshin", "B. Takeda Shingen", "C. Minamoto no Yoshitsune", "D. Ashikaga Yoshimitsu"],
            "answer": "B"
        },
{
            "question": "Quel était le lien familial entre Ii Naomasa et Tokugawa Ieyasu ?",
            "choices": ["A. Frère", "B. Gendre", "C. Fils adoptif", "D. Aucun lien direct"],
            "answer": "B"
        },
{
            "question": "Dans quelle province Ii Naomasa a-t-il établi son domaine après Sekigahara ?",
            "choices": ["A. Province de Kai", "B. Province de Tamba", "C. Province d'Ōmi", "D. Province de Satsuma"],
            "answer": "C"
        },
{
            "question": "Quel était le surnom personnel de Ii Naomasa en raison de son style de combat impitoyable ?",
            "choices": ["A. Aka-oni (Démon Rouge)", "B. Tora no Kenshi (Épée du Tigre)", "C. Kage no Bushi (Guerrier de l'Ombre)", "D. Kaminari no Samurai (Samouraï du Tonnerre)"],
            "answer": "A"
        },
# Minamoto no yoshitsune
{
    "questions": [
        {
            "question": "Minamoto no Yoshitsune était le demi-frère de quel célèbre shogun ?",
            "choices": ["A. Minamoto no Yoritomo", "B. Ashikaga Takauji", "C. Tokugawa Ieyasu", "D. Oda Nobunaga"],
            "answer": "A"
        },
{
            "question": "Quel moine-guerrier légendaire est devenu le fidèle compagnon de Yoshitsune ?",
            "choices": ["A. Musashibō Benkei", "B. Taira no Kiyomori", "C. Kusunoki Masashige", "D. Saitō Musashibō"],
            "answer": "A"
        },
{
            "question": "Dans quelle guerre Minamoto no Yoshitsune s'est-il illustré ?",
            "choices": ["A. Guerre de Genpei", "B. Guerre de Boshin", "C. Guerre d'Onin", "D. Guerre de Sekigahara"],
            "answer": "A"
        },
{
            "question": "Quelle célèbre bataille Yoshitsune a-t-il remportée contre le clan Taira en 1185 ?",
            "choices": ["A. Bataille d'Ichi-no-Tani", "B. Bataille de Yashima", "C. Bataille de Dan-no-ura", "D. Bataille de Nagashino"],
            "answer": "C"
        },
{
            "question": "Quel était le surnom de Yoshitsune dans son enfance ?",
            "choices": ["A. Hachiman", "B. Ushiwakamaru", "C. Taira no Kojiro", "D. Kamakura no Kenshi"],
            "answer": "B"
        },
{
            "question": "Pourquoi Yoshitsune a-t-il été pourchassé par son propre frère Yoritomo ?",
            "choices": ["A. Il a tenté de renverser Yoritomo", "B. Il était trop populaire et considéré comme une menace", "C. Il a rejoint le clan Taira", "D. Il a refusé de devenir shogun"],
            "answer": "B"
        },
{
            "question": "Dans quelle province Yoshitsune s'est-il réfugié avant sa mort ?",
            "choices": ["A. Province de Kai", "B. Province de Mutsu", "C. Province de Tamba", "D. Province de Satsuma"],
            "answer": "B"
        },
{
            "question": "Comment Yoshitsune est-il mort en 1189 ?",
            "choices": ["A. Seppuku", "B. Assassiné par des soldats de Yoritomo", "C. Mort au combat", "D. Exécuté publiquement"],
            "answer": "A"
        },
{
            "question": "Quel gouverneur a protégé Yoshitsune avant sa chute ?",
            "choices": ["A. Fujiwara no Hidehira", "B. Ashikaga Yoshimitsu", "C. Tokugawa Hidetada", "D. Taira no Tomomori"],
            "answer": "A"
        },
{
            "question": "Quel art martial Yoshitsune aurait-il appris auprès d'un tengu selon la légende ?",
            "choices": ["A. Kenjutsu", "B. Kyujutsu", "C. Ninjutsu", "D. Tessenjutsu"],
            "answer": "A"
        },
# naoshi kanno
{
    "questions": [
        {
            "question": "Naoshi Kanno était un pilote de chasse pour quelle branche militaire japonaise ?",
            "choices": ["A. Armée impériale japonaise", "B. Marine impériale japonaise", "C. Force aérienne impériale", "D. Garde impériale"],
            "answer": "B"
        },
{
            "question": "Combien de victoires aériennes confirmées Naoshi Kanno a-t-il obtenues ?",
            "choices": ["A. 15", "B. 25", "C. 35", "D. 50"],
            "answer": "B"
        },
{
            "question": "Quel avion de chasse Naoshi Kanno pilotait-il principalement ?",
            "choices": ["A. Mitsubishi A6M Zero", "B. Nakajima Ki-43", "C. Kawanishi N1K", "D. Yokosuka D4Y"],
            "answer": "C"
        },
{
            "question": "Quel était le surnom de Naoshi Kanno en raison de son style de combat agressif ?",
            "choices": ["A. Le Faucon de Kyushu", "B. Le Tigre du Pacifique", "C. Bulldog Yellow Fighter", "D. Le Spectre du ciel"],
            "answer": "C"
        },
{
            "question": "Dans quelle unité aérienne Naoshi Kanno a-t-il servi en 1945 ?",
            "choices": ["A. 343rd Naval Air Group", "B. 201st Naval Air Group", "C. 306th Squadron", "D. 501st Air Division"],
            "answer": "A"
        },
{
            "question": "Quel événement a marqué la dernière mission de Naoshi Kanno ?",
            "choices": ["A. Une attaque sur Pearl Harbor", "B. Une interception de B-24 près de Yakushima", "C. Une bataille aérienne au-dessus de Tokyo", "D. Une mission kamikaze refusée"],
            "answer": "B"
        },
{
            "question": "Pourquoi Naoshi Kanno n'a-t-il pas été autorisé à rejoindre une unité kamikaze ?",
            "choices": ["A. Il était trop jeune", "B. Il était considéré comme un pilote trop précieux", "C. Il refusait de se sacrifier", "D. Il était blessé"],
            "answer": "B"
        },
{
            "question": "Quel était le destin final de Naoshi Kanno après sa dernière mission ?",
            "choices": ["A. Il a été capturé", "B. Il a survécu et vécu en exil", "C. Il a disparu en mission et présumé mort", "D. Il a été exécuté par les forces américaines"],
            "answer": "C"
        },
{
            "question": "Où Naoshi Kanno a-t-il été honoré après sa mort ?",
            "choices": ["A. Temple Honnō-ji", "B. Sanctuaire Yasukuni", "C. Musée de l'aviation de Tokyo", "D. Mémorial de Hiroshima"],
            "answer": "B"
        },
{
            "question": "Dans quel anime Naoshi Kanno apparaît-il comme un personnage ?",
            "choices": ["A. Attack on Titan", "B. Drifters", "C. Code Geass", "D. Samurai Champloo"],
            "answer": "B"
        },
# butch Cassidy 
{
    "questions": [
        {
            "question": "Quel était le vrai nom de Butch Cassidy ?",
            "choices": ["A. Harry Alonzo Longabaugh", "B. Robert Leroy Parker", "C. Jesse James", "D. William H. Bonney"],
            "answer": "B"
        },
{
            "question": "Quel gang Butch Cassidy a-t-il dirigé ?",
            "choices": ["A. Dalton Gang", "B. James-Younger Gang", "C. Wild Bunch", "D. Hole-in-the-Wall Gang"],
            "answer": "C"
        },
{
            "question": "Pourquoi Butch Cassidy a-t-il choisi le nom 'Cassidy' ?",
            "choices": ["A. En hommage à un ami voleur de chevaux", "B. Parce qu'il aimait le nom", "C. Pour cacher son identité", "D. Parce qu'il était un boucher"],
            "answer": "A"
        },
{
            "question": "Dans quel pays Butch Cassidy et Sundance Kid se sont-ils réfugiés pour échapper aux détectives Pinkerton ?",
            "choices": ["A. Argentine", "B. Mexique", "C. Canada", "D. Bolivie"],
            "answer": "D"
        },
{
            "question": "Quel était le principal crime commis par Butch Cassidy et son gang ?",
            "choices": ["A. Vol de chevaux", "B. Braquage de banques et de trains", "C. Contrebande d'alcool", "D. Assassinat"],
            "answer": "B"
        },
{
            "question": "En quelle année Butch Cassidy est-il présumé mort ?",
            "choices": ["A. 1906", "B. 1907", "C. 1908", "D. 1909"],
            "answer": "C"
        },
{
            "question": "Quel célèbre film raconte l'histoire de Butch Cassidy et Sundance Kid ?",
            "choices": ["A. The Wild Bunch", "B. Butch Cassidy and the Sundance Kid", "C. True Grit", "D. Unforgiven"],
            "answer": "B"
        },
{
            "question": "Quel détective célèbre a poursuivi Butch Cassidy et son gang ?",
            "choices": ["A. Allan Pinkerton", "B. Wyatt Earp", "C. Bat Masterson", "D. Pat Garrett"],
            "answer": "A"
        },
{
            "question": "Quel était le premier grand braquage de Butch Cassidy ?",
            "choices": ["A. Une banque à Telluride", "B. Un train à Wilcox", "C. Une diligence au Texas", "D. Une mine d'or au Nevada"],
            "answer": "A"
        },
{
            "question": "Quel était le surnom de Butch Cassidy avant de devenir un célèbre hors-la-loi ?",
            "choices": ["A. The Tall Texan", "B. The Kid", "C. The Sundance Wrangler", "D. Aucun surnom"],
            "answer": "D"
        },
# Raspoutine 
{
    "questions": [
        {
            "question": "Quelle était la profession principale de Grigori Raspoutine avant d'acquérir de l'influence à la cour impériale russe ?",
            "choices": ["A. Moine", "B. Paysan", "C. Médecin", "D. Militaire"],
            "answer": "B"
        },
{
            "question": "Dans quelle ville Raspoutine a-t-il été assassiné en 1916 ?",
            "choices": ["A. Moscou", "B. Saint-Pétersbourg", "C. Kiev", "D. Vladivostok"],
            "answer": "B"
        },
{
            "question": "Quel tsar russe Raspoutine conseillait-il ?",
            "choices": ["A. Alexandre III", "B. Nicolas II", "C. Pierre le Grand", "D. Ivan IV"],
            "answer": "B"
        },
{
            "question": "Quel était le principal rôle de Raspoutine auprès de la famille impériale ?",
            "choices": ["A. Conseiller militaire", "B. Guérisseur", "C. Diplomate", "D. Ministre des Finances"],
            "answer": "B"
        },
{
            "question": "Quel était le nom de l'épouse du tsar Nicolas II, qui était particulièrement influencée par Raspoutine ?",
            "choices": ["A. Catherine la Grande", "B. Alexandra Feodorovna", "C. Maria Romanova", "D. Olga Nikolaevna"],
            "answer": "B"
        },
{
            "question": "Quel était le principal problème de santé du fils du tsar Nicolas II, que Raspoutine prétendait pouvoir soigner ?",
            "choices": ["A. Tuberculose", "B. Hémophilie", "C. Épilepsie", "D. Maladie de Parkinson"],
            "answer": "B"
        },
{
            "question": "Quel groupe de nobles russes a organisé l'assassinat de Raspoutine ?",
            "choices": ["A. Les bolcheviks", "B. Les Romanov", "C. Les aristocrates conservateurs", "D. Les cosaques"],
            "answer": "C"
        },
{
            "question": "Quelle méthode a été utilisée pour assassiner Raspoutine ?",
            "choices": ["A. Empoisonnement", "B. Fusillade", "C. Noyade", "D. Toutes ces réponses"],
            "answer": "D"
        },
{
            "question": "Quel mythe entoure la mort de Raspoutine ?",
            "choices": ["A. Il aurait survécu à plusieurs tentatives d'assassinat", "B. Il aurait été enterré vivant", "C. Il aurait été exécuté publiquement", "D. Il aurait disparu mystérieusement"],
            "answer": "A"
        },
{
            "question": "Quel impact l'influence de Raspoutine a-t-elle eu sur la réputation de la famille impériale russe ?",
            "choices": ["A. Elle a renforcé leur pouvoir", "B. Elle a contribué à leur chute", "C. Elle a amélioré leur image auprès du peuple", "D. Elle a permis une alliance avec l'Allemagne"],
            "answer": "B"
        }
    ]
}
    # Ajoutez plus de questions ici
]

# Fonction pour poser les questions
def poser_questions():
    score = 0
    for q in questions:
        print(q["question"])
        for choice in q["choices"]:
            print(choice)
        answer = input("Entrez la lettre de votre réponse : ").upper()
        if answer == q["answer"]:
            score += 1
            print("Bonne réponse !\n")
        else:
            print("Mauvaise réponse.\n")
    return score

# Fonction principale
def main():
    print("Bienvenue au Quiz Historique !")
    score = poser_questions()
    print(f"Votre score final est : {score}/{len(questions)}")

if __name__ == "__main__":
    main()