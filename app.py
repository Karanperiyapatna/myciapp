# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD to EC2!, updated CD/CI pipeline. Final check"

if __name__ == "__main__":
    app.run()



# def main():git 
#     print("Hello from CI/CD to EC2!")
#     print("checking for updates...")
#     print("Successfully tested CD/CI pipeline")

# if __name__ == "__main__":
#     main()
