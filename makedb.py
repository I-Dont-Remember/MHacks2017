from app import config
from app import db

def main():
    #db = main.db

    db.create_all()

if __name__ == '__main__':
    main()

