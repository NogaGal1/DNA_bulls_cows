# DNA Bulls and Cows

An interactive guessing game based on the classic Bulls and Cows game. The program generates a random four-letter DNA sequence using `A`, `C`, `T`, and `G`.

## Requirements

- Python 3

## Run the game

From the project root, run:

```powershell
python scripts/bulls_cows.py
```

Enter a four-letter DNA combination when prompted. The game reports:

- **Bulls**: correct letters in the correct positions
- **Cows**: correct letters in the wrong positions

The guesses and final attempt count are written to `results/results.txt`.