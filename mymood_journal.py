import datetime

MOOD_LOG_FILE = "mood_log.txt"
MOODS = ["happy", "sad", "angry", "calm", "anxious", "excited"]

def main(predefined_inputs=None):
    print("Welcome to MyMood Journal 💛")
    input_iterator = iter(predefined_inputs) if predefined_inputs else None

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new mood entry")
        print("2. View mood history")
        print("3. Analyze mood statistics")
        print("4. Exit")

        try:
            if input_iterator:
                choice = next(input_iterator).strip()
            else:
                choice = input("Your choice: ").strip()
        except (EOFError, OSError, StopIteration):
            print("\nNo input provided. Exiting.")
            break

        if choice == "1":
            log_mood(input_iterator)
        elif choice == "2":
            view_history()
        elif choice == "3":
            analyze_moods()
        elif choice == "4":
            print("Goodbye! Stay emotionally aware 💛")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")

def log_mood(input_iterator=None):
    print("\nAvailable moods: " + ", ".join(MOODS))
    try:
        if input_iterator:
            mood = next(input_iterator).lower().strip()
        else:
            mood = input("How are you feeling today? ").lower().strip()
    except (EOFError, OSError, StopIteration):
        print("No input provided for mood. Canceling.")
        return

    if mood not in MOODS:
        print("That's not a recognized mood. Try again.")
        return

    try:
        if input_iterator:
            reason = next(input_iterator)
        else:
            reason = input("Why do you feel that way? ")
    except (EOFError, OSError, StopIteration):
        print("No input provided for reason. Canceling.")
        return

    date_str = str(datetime.date.today())
    entry = f"{date_str}|{mood}|{reason}\n"

    with open(MOOD_LOG_FILE, "a") as f:
        f.write(entry)
    print("Your mood has been recorded 📂")

def view_history():
    print("\nMood History:")
    try:
        with open(MOOD_LOG_FILE, "r") as f:
            for line in f:
                date, mood, reason = line.strip().split("|")
                print(f"{date}: {mood} - \"{reason}\"")
    except FileNotFoundError:
        print("No history yet. Try logging your mood first.")

def analyze_moods():
    print("\nMood Analysis:")
    mood_counts = {}
    try:
        with open(MOOD_LOG_FILE, "r") as f:
            for line in f:
                _, mood, _ = line.strip().split("|")
                if mood in mood_counts:
                    mood_counts[mood] += 1
                else:
                    mood_counts[mood] = 1

        if not mood_counts:
            print("No mood data to analyze.")
            return

        most_common = max(mood_counts, key=mood_counts.get)
        print(f"Most common mood: {most_common} ({mood_counts[most_common]} times)")
        print("Mood counts:")
        for mood in sorted(mood_counts):
            print(f"{mood}: {mood_counts[mood]}")
    except FileNotFoundError:
        print("No data file found. Try logging a mood first.")

if __name__ == '__main__':
    # To run interactively, pass no arguments.
    main()
    # For testing with predefined inputs, you can run: main(["1", "happy", "Had a great day!", "4"])
