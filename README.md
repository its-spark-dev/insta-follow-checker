# 📊 Insta Follow Checker

A simple Python utility that checks **who doesn't follow you back** on Instagram and exports the list to a CSV file.

---

## ✨ Features

* 🔐 **Secure login** via `.session` file (2FA supported)
* 📅 Fetch your **followers** and **followees**
* 📁 Identify users who **don’t follow you back**
* 📄 Save results as a **timestamped CSV** file in the `out/` directory
* 📦 Environment variables managed via `.env`

---

## ⚙️ Requirements

* Python 3.8+
* `instaloader`
* `python-dotenv`

Install dependencies:

```
bash
pip install -r requirements.txt
```

---

## 🔐 Setup

1. Clone the repo:

```
bash
git clone https://github.com/your_username/insta-follow-checker.git
cd insta-follow-checker
```

2. Create a `.env` file:

```
env
INSTA_USERNAME=your_instagram_username
```

👉 Don't include your password if you're using a `.session` file (recommended).

3. Login using Instaloader (for 2FA accounts):

```
bash
instaloader --login your_instagram_username
```

Enter your password and 2FA code. This will generate a `.session` file you can reuse without exposing your password.

---

## 🚀 Usage

Run the script:

```
bash
python main.py
```

You’ll see output like:

```
✅ Logged in using session file.
📥 Fetching followers and followees...
❌ 42 users do not follow you back.
📄 Saved to out/not_following_back_2025-07-18_10-30-00.csv
```

---

## 📁 Output

The CSV file will be saved in the `out/` directory and look like:

```
Username
some_user
another_user
...
```

---

## 📟 Example `.env.example`

```
env
# Put your Instagram username here
INSTA_USERNAME=your_username
```

---

## 🛡️ Security Notes

* `.session` files contain your login session – **do not commit them to GitHub!**
* `.gitignore` already excludes `.env` and `*.session` by default.

---

## 🪪 License

MIT License © 2025 Sang Park

---

## 🙌 Acknowledgments

* Built with [Instaloader](https://instaloader.github.io/)
