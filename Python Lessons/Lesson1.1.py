import random

def run_quiz():
    questions = [
        {"question": "What is the chemical symbol for water?", "options": ["A) O2", "B) CO2", "C) H2O", "D) NaCl"], "answer": "C"},
        {"question": "What planet is known as the Red Planet?", "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"], "answer": "B"},
        {"question": "What gas do plants absorb from the atmosphere?", "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"], "answer": "B"},
        {"question": "Which part of the human body contains the most bones?", "options": ["A) Skull", "B) Hand", "C) Foot", "D) Spine"], "answer": "C"},
        {"question": "What is the powerhouse of the cell?", "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Cytoplasm"], "answer": "C"},
        {"question": "What is the speed of light?", "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 500,000 km/s", "D) 100,000 km/s"], "answer": "A"},
        {"question": "Which element is found in all organic compounds?", "options": ["A) Oxygen", "B) Carbon", "C) Hydrogen", "D) Nitrogen"], "answer": "B"},
        {"question": "What is the hardest natural substance on Earth?", "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"], "answer": "C"},
        {"question": "Which blood type is the universal donor?", "options": ["A) A", "B) B", "C) AB", "D) O"], "answer": "D"},
        {"question": "What gas do humans breathe out?", "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"], "answer": "C"},
        {"question": "What is the main gas in Earth's atmosphere?", "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"], "answer": "B"},
        {"question": "How many teeth does an adult human have?", "options": ["A) 24", "B) 28", "C) 30", "D) 32"], "answer": "D"},
        {"question": "What is the smallest planet in our solar system?", "options": ["A) Mars", "B) Mercury", "C) Venus", "D) Pluto"], "answer": "B"},
        {"question": "What part of the plant conducts photosynthesis?", "options": ["A) Root", "B) Stem", "C) Leaf", "D) Flower"], "answer": "C"},
        {"question": "How many chambers does the human heart have?", "options": ["A) 2", "B) 4", "C) 6", "D) 8"], "answer": "B"},
        {"question": "Which gas makes up most of the sun?", "options": ["A) Oxygen", "B) Hydrogen", "C) Helium", "D) Nitrogen"], "answer": "B"},
        {"question": "What is the boiling point of water at sea level?", "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"], "answer": "B"},
        {"question": "What is the largest organ in the human body?", "options": ["A) Brain", "B) Heart", "C) Skin", "D) Liver"], "answer": "C"},
        {"question": "What is the basic unit of life?", "options": ["A) Atom", "B) Cell", "C) Tissue", "D) Organ"], "answer": "B"},
        {"question": "What is the most abundant element in the universe?", "options": ["A) Oxygen", "B) Hydrogen", "C) Carbon", "D) Helium"], "answer": "B"},
        {"question": "Which scientist proposed the theory of relativity?", "options": ["A) Newton", "B) Einstein", "C) Galileo", "D) Tesla"], "answer": "B"},
        {"question": "What do bees collect and use to make honey?", "options": ["A) Nectar", "B) Pollen", "C) Water", "D) Sugar"], "answer": "A"},
        {"question": "Which organ is responsible for pumping blood?", "options": ["A) Brain", "B) Liver", "C) Heart", "D) Kidney"], "answer": "C"},
        {"question": "What metal is liquid at room temperature?", "options": ["A) Mercury", "B) Iron", "C) Gold", "D) Silver"], "answer": "A"},
        {"question": "What type of energy is produced by moving water?", "options": ["A) Solar", "B) Wind", "C) Hydro", "D) Nuclear"], "answer": "C"},
        {"question": "Which vitamin is produced by sunlight exposure?", "options": ["A) Vitamin A", "B) Vitamin B", "C) Vitamin C", "D) Vitamin D"], "answer": "D"},
        {"question": "What is the main component of Earth's core?", "options": ["A) Iron", "B) Nickel", "C) Magnesium", "D) Silicon"], "answer": "A"},
        {"question": "Which gas do humans need to survive?", "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Helium", "D) Hydrogen"], "answer": "A"},
        {"question": "How many legs does a spider have?", "options": ["A) 6", "B) 8", "C) 10", "D) 12"], "answer": "B"}
    ]

    selected_questions = random.sample(questions, 10)  # Randomly select 10 questions
    score = 0

    for q in selected_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🏆 You scored {score}/10!")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        run_quiz()
    else:
        print("Thanks for playing! 🎉")

# Start the quiz
run_quiz()
