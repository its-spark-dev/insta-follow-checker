# 📦 Insta Follow Checker - Justfile
# Automate common tasks like running, setting up environment, and logging in.

# Automatically load variables from `.env`
set dotenv-load

# 👟 Default task: run the app
default:
    just run

# ▶️ Run the main script and create the output directory if needed
run:
    @mkdir -p out
    python main.py

# 🛠️ Install dependencies from requirements.txt
install:
    pip install -r requirements.txt

# 🧪 Create a new .env file from the example
init-env:
    cp .env.example .env

# 🔐 Log in to Instagram and generate a session file
login:
    instaloader --login $INSTA_USERNAME
