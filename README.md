# Romania County Game 🗺️

A fun and educational Python game to help you learn all 41 counties (județe) of Romania. Test your geography knowledge while racing against time!

## 📝 Description

Romania County Game is an interactive educational game built with Python's Turtle graphics library. Players need to name all 41 counties of Romania while looking at a blank map. The game features a timer and high score system to track your best performances.

## 🎮 Game Features

- Interactive map of Romania
- Real-time feedback on correct guesses
- Timer to track your progress
- High score system
- Visual feedback with county names appearing on the map
- Clean exit functionality
- Progress tracker (X/41 counties)

## 🛠️ Prerequisites

Before running the game, make sure you have the following installed:
- Python 3.x
- pandas library
- turtle module (comes with Python standard library)

```bash
pip install pandas
```

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/dbeniamin/Romania_County_Guesser.git
cd Romania_County_Guesser
```

2. Ensure you have all required files in your directory:
- `main.py` (main game file)
- `Romania-districts_map.gif` (map image)
- `counties.csv` (county data file)

## 🎯 How to Play

1. Run the game:
```bash
python main.py
```

2. Type in the names of Romanian counties when prompted
3. The game will:
   - Show correct guesses on the map
   - Track your progress (X/41)
   - Keep time
   - Save your best times

4. To exit the game, type "Exit" in the prompt field

## 📄 File Structure

```
romania-county-game/
│
├── main.py                     # Main game script
├── counties.csv                # County coordinates data
├── Romania-districts_map.gif   # Game map image
├── lowest_times.txt            # High scores file
└── README.md                   # This file
```

## 🎲 Gameplay Rules

- Type the name of a Romanian county in the prompt field
- Names can be entered in any order
- Each correct guess will appear on the map
- Timer runs until all counties are guessed or player exits
- High scores are only saved when all 41 counties are correctly guessed

## 🏆 Scoring System

- Timer tracks your completion time
- Format: MM:SS (minutes:seconds)
- Best times are saved in `lowest_times.txt`
- Only complete games (all 41 counties guessed) are saved

## ⚠️ Known Limitations

- Special characters (ș, ț, ă, â, î) are not required
- The game window must remain active while playing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

If you have any questions or suggestions, please open an issue on this repository.

---
Made with ❤️ for Romania and geography enthusiasts everywhere.
