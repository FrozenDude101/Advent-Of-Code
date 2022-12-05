import logging as _logging
import os as _os
import urllib3 as _urllib3


_HTTP = _urllib3.PoolManager()
_INPUT_URL = "https://adventofcode.com/{year}/day/{day}/input"

_USER_AGENT = _os.getenv("USER_AGENT")
_SESSION_COOKIE = _os.getenv("SESSION_COOKIE")


def getInput(year, day):

    _logging.info(f"Requesting data for {year}/{day} from adventofcode.com")
    
    headers = {
        "Cookie": f"session={_os.getenv('SESSION_COOKIE')}",
    }

    if _USER_AGENT == "<USER_AGENT>" or _USER_AGENT is None:
        _logging.warning(f"A custom user agent is going to be required in the near future. You can set one in the .env file. See reddit.com/z9dhtd for more details.")
    else:
        headers["User-Agent"] = _USER_AGENT

    if _SESSION_COOKIE is None:
        _logging.critical(f"You have to set your session cookie in the .env file to retrieve your specific input.")
        raise ValueError("Missing SESSION-COOKIE variable in environment. You can set it in the .env file.")

    request = _HTTP.request(
        "GET",
        _INPUT_URL.format(year = year, day = day),
        headers = headers,
    )

    match (request.status):
        case 400:
            _logging.critical(f"You have to set your session cookie in the .env file to retrieve your specific input.")
            raise ValueError("Missing SESSION-COOKIE variable in environment. You can set it in the .env file.")
        case 404:
            if "locked" in request.data.decode("utf-8"):
                _logging.critical(f"The year {year}, day {day} challenge is still locked. You must wait for it to unlock before retrieving your input.")
                raise ValueError("Invalid year/day combination, the challenge is still locked.")
            else:
                _logging.critical(f"No challenge exists on year {year}, day {day}.")
                raise ValueError("Invalid year/day combination, the challenge does not exist.")
        case 500:
            _logging.critical(f"Advent of Code returned a 500 server error. Make sure your session cookie is correct.")
            raise ValueError("Missing SESSION-COOKIE variable in environment. You can set it in the .env file.")

    if request.status != 200:
        _logging.critical(f("An unknown error has occured, please try agia."))
        raise ValueError("Advent of Code did not return a 200 success code.")

    data = request.data.decode("utf-8")
    data = data[:-1]
    return data