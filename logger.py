import datetime
def write_log(message):
    with open("library_log.txt", "a") as file:
        time = datetime.datetime.now()
        file.write(
            f"{time} - {message}\n"
        )