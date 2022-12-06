import logging as _logging
import os as _os
import sys as _sys
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
            _sys.exit()
        case 404:
            if "synchronized" in request.data.decode("utf-8"):
                _logging.critical(f"The year {year}, day {day} challenge is still locked. You must wait for it to unlock before retrieving your input.")
            else:
                _logging.critical(f"No challenge exists on year {year}, day {day}.")
            _sys.exit()
        case 500:
            _logging.critical(f"Advent of Code returned a 500 server error. Make sure your session cookie is correct.")
            _sys.exit()

    if request.status != 200:
        _logging.critical(f("An unknown error has occured, please try agian."))
        _logging.debug(f"Status: {request.status}")
        _logging.debug(f"Data: {request.data.decode('utf-8')}")
        _sys.exit()

    data = request.data.decode("utf-8")
    data = data[:-1]
    return data