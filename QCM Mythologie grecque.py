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

    # ... ajoute ici toutes tes autres questions ...
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