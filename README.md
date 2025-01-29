# 🎮 Dodge It

A simple arcade-style game where you dodge falling obstacles to achieve the highest score possible.

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/WailDebz/Dodge-it/
cd Dodge-It
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🕹️ Playing the Game

Run the game using:
```bash
python src/main.py
```

### 🎯 Controls
- Arrow keys to move
- Close window to quit

## 📁 Project Structure

```
Dodge-It/
├── src/
│   └── main.py
├── assets/
│   ├── audio/
│   ├── fonts/
│   │   └── Acme-Regular.ttf
│   └── images/
├── requirements.txt
├── dodge-it.spec
└── README.md
```

## 📦 Building Executable

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller dodge-it.spec
```

The executable will be created in the `dist` directory.

## 🌟 Features

-   Simple and addictive gameplay
-   Score system

## 🤝 Contributing

Contributions are welcome! Feel free to:

-   Report bugs
-   Suggest new features
-   Submit pull requests