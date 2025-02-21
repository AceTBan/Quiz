
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
   {
        "question": Toyohisa Shimazu a participé à quelle célèbre bataille en 1600 ?",
        "choices": ["A. Bataille de Sekigahara", "B. Bataille de Nagashino", "C. Bataille de Kawanakajima", "D. Bataille de Dan-no-ura"],
        "answer": "A"
    },
   {
        "question": "Toyohisa Shimazu était membre de quel clan japonais ?",
        "choices": ["A. Clan Tokugawa", "B. Clan Shimazu", "C. Clan Oda", "D. Clan Date"],
        "answer": "B"
    },

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