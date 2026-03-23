from tools.browser import search_web, open_browser
from tools.email import read_latest_emails

def execute(command):

    if command.startswith("search_web"):

        query = command.split("(",1)[1].rstrip(")")

        return search_web(query)

    if command.startswith("open_browser"):

        url = command.split("(",1)[1].rstrip(")")

        return open_browser(url)
    
    if command.startswith("read_emails"):

        return read_latest_emails()

    return "Unknown command"