import datetime


def write_log(message):

    with open("library_log.txt", "a") as file:

        file.write(
            f"{datetime.datetime.now()} - {message}\n"
        )