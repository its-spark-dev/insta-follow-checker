# 📊 Insta Follow Checker

A minimal yet powerful Python tool to check **who doesn't follow you back on Instagram**. Login is securely handled using Instaloader sessions (supports 2FA), and the results are exported to a timestamped CSV file.

---

## 🌐 Project Structure

```
insta-follow-checker/
├── out/                         # Output directory for CSV result files
├── utils/                       # Utility functions
│   ├── csv_utils.py             # CSV export helper
│   └── instagram_utils.py       # Instagram data fetcher and login handler
├── .env                         # User-specific environment variables (excluded from git)
├── .env.example                 # Example .env template
├── .gitignore                   # Ignore session, output, and IDE files
├── justfile                     # Justfile for command automation
├── LICENSE                      # MIT License
├── main.py                      # Main script
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---

## ✨ Features

* 🔐 Secure login via `.session` file (2FA supported)
* 🗓️ Fetch followers and followees
* ❌ Identify who doesn't follow you back
* 📄 Export to timestamped `.csv` in `out/` folder
* 📦 Environment variables managed via `.env`
* ⚙️ Fully automatable with `justfile`

---

## ⚙️ Requirements

* Python >= 3.8
* [`instaloader`](https://instaloader.github.io/)
* [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🔒 Setup

### 1. Clone the repository:

```bash
git clone https://github.com/your_username/insta-follow-checker.git
cd insta-follow-checker
```

### 2. Create `.env` file:

```bash
cp .env.example .env
```

Then edit `.env` and fill in your Instagram username:

```env
INSTA_USERNAME=your_instagram_username
```

> Do NOT put your password here. Session login is more secure and recommended.

### 3. Login with Instaloader (generates session file):

```bash
instaloader --login your_instagram_username
```

You will be prompted to enter:

* your password
* a 2FA code if 2FA is enabled on your account

This will generate a session file in:

```
~/.config/instaloader/session-your_instagram_username
```

---

## 🚀 Usage

To run the checker:

```bash
python main.py
```

Sample output:

```
🔑 Logged in using session file.
📥 Fetching followers and followees...
❌ 42 users do not follow you back.
📄 Saved to out/not_following_back_2025-07-18_11-25-00.csv
```

> Instagram may rate-limit requests. If you see a block warning, wait 30–60 minutes.

---

## 📝 Output Format

The result CSV file is saved in `out/` with a filename like:

```bash
not_following_back_2025-07-18_11-25-00.csv
```

Contents:

```
Username
user123
another_user
...
```

---

## 🚪 Automate with `just`

This project supports [`just`](https://github.com/casey/just) task runner.

### Install `just`:

```bash
brew install just   # macOS
sudo apt install just   # Ubuntu
```

### Available Tasks

```bash
just run         # Run the script
just install     # Install dependencies
just init-env    # Copy .env.example to .env
just login       # Trigger session login via instaloader
```

---

## 🛡️ Security Tips

* `.session` files **should NOT be committed**. They're excluded via `.gitignore`
* `.env` is also excluded to protect your credentials
* Do not share your `.env` or `.session` files publicly

---

## 🌐 Example `.env.example`

```env
# Put your Instagram username here
INSTA_USERNAME=your_username
```

---

## 🛫 License

MIT License © 2025 Sang Park

---

## 🙌 Acknowledgments

Built using:

* [Instaloader](https://instaloader.github.io/)
* [python-dotenv](https://github.com/theskumar/python-dotenv/)
* [just](https://github.com/casey/just) for automation
