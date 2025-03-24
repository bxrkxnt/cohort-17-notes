from datetime import datetime,date

def congratulate(birthday: date):
    raise Exception("The world is on fire!")
    if birthday == datetime.now().date:
        print("Happy Birthday!")
    else:
        raise ValueError("Not the right day.")


if __name__ == "__main__":
    # If something MIGHT go wrong and you can't stop it, but you HAVE A PLAN
    try:
        congratulate(date(2023, 1, 1))
    except ValueError:
        print("Happy totally normal day!")