# Progress

## Goal
Build skills for an IT career (cloud engineering path) and prepare for
the PhilNITS FE exam (April 2027).

## Done

### Day 1 (Oct 18)
- Set up WSL2 + Ubuntu, connected VS Code to Linux
- Linux: pwd, ls, cd, mkdir, cp, mv, rm, echo, cat
- Python: loops, wrote find_largest with an empty-list check

### Day 2 (Oct 19)
- Python: find_smallest, find_sum, count_evens
- Git: init, add, commit, push; created GitHub repo and README

### Day 3 (Oct 20)
- Recalled find_largest from memory
- count_vowels (the `in` operator, `.lower()`)
- Linux: nano basics

### Day 4 (Oct 21)
- Recalled count_vowels from memory
- reverse_text (loop version and `[::-1]`)

### Day 5 (Oct 22)
- Recalled find_smallest from memory
- is_palindrome; how True/False values work
- Linux permissions: ls -l, chmod with letters and numbers (755, 644, 600)

### Day 6 (Oct 23)
- Recalled count_evens from memory
- count_words (`.split()` turns text into a list)

### Day 7 (Oct 24)
- Recalled find_sum from memory
- FizzBuzz: `range()`, `elif`, `.append()`, returning a list
- Made fizzbuzz take a list or range as input

### Day 8 (Oct 25)
- Recalled count_vowels again (fixed the `in` direction and the missing loop)
- remove_duplicates (`not in`, checking against the new list)
- Linux: seq, head, tail, less, and my first pipe (`head | tail`)

### Day 9 (Oct 26)
- First Linux recall (forgot cp, rm, chmod, then re-learned them)
- Recalled reverse_text from memory
- second_largest (three-loop version; also learned `sorted(numbers)[-2]`)
- Linux: grep (`-i`, `-n`, `-c`) and using it with a pipe on a pretend log file

## Lessons learned
- Indentation decides what is inside a loop or `if`; `return` goes after the loop
- `=` stores a value, `==` compares; `print` shows, `return` gives back
- `return` exits the function immediately, so collect results in a list first
- A loop variable is one item, the list is the whole thing
- In `x in y`, the single item goes on the left and the group on the right
- Starting values should come from the same collection you're about to loop over
- Put the most specific check first in an `if`/`elif` chain
- A calculation needs `=`, `+=`, or `.append()` to save its result
- One passing test isn't enough, so test start, middle, end, and empty cases
- Methods need parentheses: `.lower()`, not `.lower`
- `chmod MODE FILE`: the mode is one word with no spaces
- A pipe `|` sends one command's output into the next command
- `grep` finds the lines that matter; a pipe lets me do more with them

## Daily rhythm
- Python: 45-60 min (one recall exercise + one new problem)
- Linux: 20-30 min (start with a 5-min recall from memory, then one new topic)
- Rotating through the week: SQL, job listings
- Review the balance weekly; shift toward Linux/networking once writing
  Python feels comfortable

## Next
- Recall exercises without peeking, rotating through older functions
- Linux cheat sheet (linux-notes.md) in my own words
- Linux, in order: more pipes, networking (ping, ip addr, DNS), apt and ps/top
- New Python problems: count how often each word appears, find the longest word
- SQL basics (SQLBolt, 20-30 min a few days a week)
- PhilNITS FE past paper: around mid-November, just 10 questions to see which topics need work
- Around week 4: JavaScript taste test (one small web page)
- Later: AWS Cloud Practitioner