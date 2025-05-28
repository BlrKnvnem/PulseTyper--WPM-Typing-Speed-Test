# 🖊️ WPM Typing Speed Test (Python Console App)

A beginner-friendly Python script that calculates your typing speed in **Words Per Minute (WPM)**. Great for practicing your typing and learning basic Python I/O and timing functions.

---

## 🚀 Features

- Simple and interactive CLI interface
- Real-time measurement of:
  - Words typed
  - Time taken
  - Typing speed in WPM
- Lightweight, no external libraries required

---

## 📋 Requirements

- Python 3.x

No external packages needed.

---

## 🛠️ How to Run

1. Save the code in a file called `typing_test.py`
2. Open your terminal or command prompt
3. Run the script:

```bash
python typing_test.py
```
#💻 Sample Output

```
 WPM Typing Speed Test
Type the following sentence:

Press Enter to start...

Start typing below:
the quick brown fox jumps over the lazy dog

<------ Result ------->
Time taken: 9.67 seconds
Words typed: 9
Typing speed: 55.84 WPM
```
🧠 How it Works

->Starts a timer right before you begin typing

->Takes your typed input

->Calculates elapsed time

->Counts words using .split()

Calculates WPM using:
```
WPM = (word_count / elapsed_time_in_seconds) × 60
```
📌 Future Ideas

->Add random sentences for practice

->Add accuracy and error tracking

->Make a GUI version using Tkinter or PyQt

->Add a leaderboard or history tracker

#🧑‍💻 Author

Developed by blrknvnem

Contributions welcome! Feel free to fork and improve. 🛠️
