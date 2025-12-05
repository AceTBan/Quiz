import random

questions = [
    {
        "question": "Quel est le nom complet de Iron Man dans le MCU ?",
        "choices": ["A. Howard Stark", "B. Tony Stark", "C. James Stark", "D. Steve Stark"],
        "answer": "B"
    },
{
        "question": "Quel est le nom de l’IA qui remplace J.A.R.V.I.S. dans Iron Man 3 ?",
        "choices": ["A. FRIDAY", "B. EDITH", "C. KAREN", "D. PEPPER"],
        "answer": "A"
    },
{
        "question": "Quel est le nom du scientifique qui devient le Mandarin dans Iron Man 3 ?",
        "choices": ["A. Aldrich Killian", "B. Obadiah Stane", "C. Trevor Slattery", "D. Justin Hammer"],
        "answer": "A"
    },
{
        "question": "Quel mutant est connu pour ses griffes en adamantium ?",
        "choices": ["A. Cyclope", "B. Magneto", "C. Wolverine", "D. Deadpool"],
        "answer": "C"
    },
{
        "question": "Quel personnage est capable de régénération quasi instantanée et adore briser le 4e mur ?",
        "choices": ["A. Cable", "B. Deadpool", "C. Domino", "D. Colossus"],
        "answer": "B"
    },
{
        "question": "Quel est le nom du sorcier suprême avant Doctor Strange ?",
        "choices": ["A. Wong", "B. Mordo", "C. L’Ancien", "D. Agatha"],
        "answer": "C"
    },
{
        "question": "Quel artefact permet à Doctor Strange de manipuler le temps ?",
        "choices": ["A. Le Cube Cosmique", "B. L’Œil d’Agamotto", "C. Le Sceptre de Loki", "D. Le Bâton de Watoomb"],
        "answer": "B"
    },
{
        "question": "Quel est le nom du monde miroir utilisé par les sorciers dans Doctor Strange ?",
        "choices": ["A. Mirrorverse", "B. Dimension Astrale", "C. Monde Miroir", "D. Dark Dimension"],
        "answer": "C"
    },
{
        "question": "Quel est le nom du méchant principal dans Doctor Strange (2016) ?",
        "choices": ["A. Dormammu", "B. Kaecilius", "C. Mordo", "D. Mephisto"],
        "answer": "B"
    },
{
        "question": "Quel personnage est le père de Star-Lord dans Les Gardiens de la Galaxie Vol. 2 ?",
        "choices": ["A. Yondu", "B. Ego", "C. Rocket", "D. Thanos"],
        "answer": "B"
    },
{
        "question": "Quel est le vrai nom de Star-Lord ?",
        "choices": ["A. Peter Quill", "B. Chris Pratt", "C. Jason Quill", "D. Peter Stark"],
        "answer": "A"
    },
{
        "question": "Quel membre des Gardiens est un arbre humanoïde ?",
        "choices": ["A. Drax", "B. Rocket", "C. Groot", "D. Mantis"],
        "answer": "C"
    },
{
        "question": "Quel est le nom du raton laveur génétiquement modifié dans les Gardiens ?",
        "choices": ["A. Rocket", "B. Raccoon", "C. Blaster", "D. Sniper"],
        "answer": "A"
    },
{
        "question": "Quel méchant cherche à réunir les Pierres d’Infinité ?",
        "choices": ["A. Ultron", "B. Loki", "C. Thanos", "D. Red Skull"],
        "answer": "C"
    },
{
        "question": "Combien de pierres d’infinité existe-t-il dans le MCU ?",
        "choices": ["A. 4", "B. 5", "C. 6", "D. 7"],
        "answer": "C"
    },
{
        "question": "Quel Avenger dit à Thanos : « Je suis Iron Man » avant de claquer des doigts ?",
        "choices": ["A. Thor", "B. Captain America", "C. Hulk", "D. Tony Stark"],
        "answer": "D"
    },
    # ... ajoute toutes autres questions ici ...
]

def poser_questions(questions):
    score = 0
    # Sélectionner 10 questions aléatoires
    quiz = random.sample(questions, 10)
    print("\n--- Début du quiz ---\n")

    for i, q in enumerate(quiz, 1):
        print(f"Question {i}: {q['question']}")
        for choice in q["choices"]:
            print(f"   {choice}")

        # Extraire les lettres valides (A, B, C, D...)
        valid_choices = [c[0] for c in q["choices"]]
        answer = ""
        while answer not in valid_choices:
            answer = input("Entrez la lettre de votre réponse : ").strip().upper()
            if answer not in valid_choices:
                print("Réponse invalide. Choisissez parmi :", ", ".join(valid_choices))

        if answer == q["answer"]:
            score += 1
            print("✅ Bonne réponse !\n")
        else:
            print(f"❌ Mauvaise réponse. La bonne réponse était : {q['answer']}\n")

    print("--- Fin du quiz ---\n")
    return score

def main():
    print("🎓 Bienvenue au Quiz Historique !")
    while True:
        score = poser_questions(questions)
        print(f"Votre score final est : {score}/10 ({(score/10)*100:.1f}%)")

        rejouer = input("Souhaitez-vous rejouer ? (O/N) : ").strip().upper()
        if rejouer != "O":
            print("Merci d'avoir joué ! À bientôt 👋")
            break

if __name__ == "__main__":
    main()