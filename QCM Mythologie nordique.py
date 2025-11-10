import random

questions = [
    {
        "question": "Quel est le dieu principal du panthéon nordique, associé à la sagesse et à la guerre ?",
        "choices": ["A. Thor", "B. Loki", "C. Freyr", "D. Odin"],
        "answer": "D"
    },
{
        "question": "Quel dieu nordique est connu pour son marteau Mjöllnir ?",
        "choices": ["A. Baldr", "B. Thor", "C. Tyr", "D. Heimdall"],
        "answer": "B"
    },
{
        "question": "Quel est le nom du loup géant qui dévorera Odin lors du Ragnarök ?",
        "choices": ["A. Fenrir", "B. Garm", "C. Sköll", "D. Hati"],
        "answer": "A"
    },
{
        "question": "Quel dieu nordique est connu pour ses ruses et ses métamorphoses ?",
        "choices": ["A. Freyr", "B. Loki", "C. Tyr", "D. Njörd"],
        "answer": "B"
    },
{
        "question": "Quel est le nom du pont arc-en-ciel reliant Midgard à Asgard ?",
        "choices": ["A. Gjallarbrú", "B. Yggdrasil", "C. Bifröst", "D. Vanaheim"],
        "answer": "C"
    },
{
        "question": "Quel dieu est le gardien de Bifröst et possède une ouïe exceptionnelle ?",
        "choices": ["A. Heimdall", "B. Baldr", "C. Hodr", "D. Bragi"],
        "answer": "A"
    },
{
        "question": "Quel arbre relie les neuf mondes dans la cosmologie nordique ?",
        "choices": ["A. Mímameiðr", "B. Yggdrasil", "C. Hoddmímis Holt", "D. Ask"],
        "answer": "B"
    },
{
        "question": "Quel dieu nordique a sacrifié son œil pour obtenir la sagesse ?",
        "choices": ["A. Tyr", "B. Odin", "C. Loki", "D. Freyr"],
        "answer": "B"
    },
{
        "question": "Quel dieu est tué par une flèche de gui, provoquant le début du Ragnarök ?",
        "choices": ["A. Baldr", "B. Hodr", "C. Forseti", "D. Vidar"],
        "answer": "A"
    },
{
        "question": "Quel dieu nordique est associé à la justice et au combat, et a perdu une main ?",
        "choices": ["A. Bragi", "B. Tyr", "C. Njörd", "D. Ullr"],
        "answer": "B"
    },
{
        "question": "Quel est le nom du serpent qui entoure le monde dans la mythologie nordique ?",
        "choices": ["A. Níðhöggr", "B. Fafnir", "C. Jörmungandr", "D. Garm"],
        "answer": "C"
    },
{
        "question": "Quel est le nom du royaume des morts gouverné par la déesse Hel ?",
        "choices": ["A. Niflheim", "B. Muspelheim", "C. Vanaheim", "D. Alfheim"],
        "answer": "A"
    },
{
        "question": "Quel est le nom du géant de feu qui mènera les forces du chaos au Ragnarök ?",
        "choices": ["A. Surtr", "B. Hrungnir", "C. Thrym", "D. Ymir"],
        "answer": "A"
    },
{
        "question": "Quel dieu est le père de Thor ?",
        "choices": ["A. Loki", "B. Odin", "C. Njörd", "D. Baldr"],
        "answer": "B"
    },
{
        "question": "Quel est le nom du navire géant fait d’ongles humains qui apparaîtra au Ragnarök ?",
        "choices": ["A. Skidbladnir", "B. Naglfar", "C. Hringhorni", "D. Drakkar"],
        "answer": "B"
    },
{
        "question": "Quel dieu nordique est associé à la poésie et à l’éloquence ?",
        "choices": ["A. Bragi", "B. Forseti", "C. Heimdall", "D. Hodr"],
        "answer": "A"
    },
{
        "question": "Quel est le nom du monde des elfes lumineux ?",
        "choices": ["A. Svartalfheim", "B. Alfheim", "C. Vanaheim", "D. Jotunheim"],
        "answer": "B"
    },
{
        "question": "Quel est le nom du géant primordial dont le corps a servi à créer le monde ?",
        "choices": ["A. Surtr", "B. Ymir", "C. Thrym", "D. Búri"],
        "answer": "B"
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