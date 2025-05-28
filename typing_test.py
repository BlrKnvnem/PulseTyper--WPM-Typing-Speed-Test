import time

def count_words(text):
    return len(text.split())

def typing_test():
    print(" WPM Typing Speed Test")
    print("Type the following sentence:\n")

    input("Press Enter to start...")

    print("\nStart typing below:")
    start_time = time.time()

    user_input = input()

    end_time = time.time()
    elapsed_time = end_time - start_time

    word_count = count_words(user_input)
    wpm = (word_count / elapsed_time) * 60


    print("\n===== Result =====")
    print(f"Time taken: {round(elapsed_time, 2)} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {round(wpm, 2)} WPM")

if __name__ == "__main__":
    typing_test()
