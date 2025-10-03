import random

questions = [
    {
        "question": "Quel est le roi des dieux dans la mythologie grecque ?",
        "choices": ["A. Poséidon", "B. Hadès", "C. Apollon", "D. Zeus"],
        "answer": "D"
    },
{
        "question": "Qui est la déesse de la sagesse et de la guerre stratégique ?",
        "choices": ["A. Héra", "B. Artémis", "C. Athéna", "D. Aphrodite"],
        "answer": "C"
    },
{
        "question": "Quel héros a tué le Minotaure dans le labyrinthe de Crète ?",
        "choices": ["A. Héraclès", "B. Thésée", "C. Persée", "D. Jason"],
        "answer": "B"
    },
{
        "question": "Quel dieu est associé au soleil, à la musique et à la divination ?",
        "choices": ["A. Dionysos", "B. Hermès", "C. Apollon", "D. Arès"],
        "answer": "C"
    },
{
        "question": "Quelle créature mythologique possède un corps de lion, une tête humaine et des ailes ?",
        "choices": ["A. Chimère", "B. Sphinx", "C. Griffon", "D. Harpie"],
        "answer": "B"
    },
{
        "question": "Qui est le dieu des enfers dans la mythologie grecque ?",
        "choices": ["A. Hadès", "B. Chronos", "C. Pan", "D. Héphaïstos"],
        "answer": "A"
    },
{
        "question": "Quel héros a accompli douze travaux imposés par Eurysthée ?",
        "choices": ["A. Achille", "B. Ulysse", "C. Héraclès", "D. Orphée"],
        "answer": "C"
    },
{
        "question": "Qui est la déesse de l’amour et de la beauté ?",
        "choices": ["A. Hestia", "B. Déméter", "C. Athéna", "D. Aphrodite"],
        "answer": "D"
    },
{
        "question": "Quel titan est le père de Zeus, Poséidon et Hadès ?",
        "choices": ["A. Ouranos", "B. Chronos", "C. Prométhée", "D. Océan"],
        "answer": "B"
    },
{
        "question": "Quel héros grec est connu pour son voyage semé d’embûches après la guerre de Troie ?",
        "choices": ["A. Ulysse", "B. Hector", "C. Achille", "D. Agamemnon"],
        "answer": "A"
    },
{
        "question": "Qui est le dieu grec du sommeil, souvent représenté avec des ailes sur les tempes ?",
        "choices": ["A. Hypnos", "B. Thanatos", "C. Morpheus", "D. Phobos"],
        "answer": "A"
    },
{
        "question": "Quel dieu est le jumeau de Hypnos et incarne la mort paisible ?",
        "choices": ["A. Chronos", "B. Thanatos", "C. Erebus", "D. Hélios"],
        "answer": "B"
    },
{
        "question": "Quel dieu mineur est le père des rêves et des illusions ?",
        "choices": ["A. Morpheus", "B. Oneiros", "C. Phantasos", "D. Somnus"],
        "answer": "A"
    },
{
        "question": "Quel dieu grec est associé aux portes et aux transitions, souvent invoqué au seuil des maisons ?",
        "choices": ["A. Janus", "B. Hécate", "C. Hermès", "D. Aucun, Janus est romain"],
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