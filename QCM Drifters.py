
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