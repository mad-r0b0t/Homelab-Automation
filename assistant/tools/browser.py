import webbrowser

def search_web(query):

    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)

    return "Browser search opened"


def open_browser(url):

    webbrowser.open(url)

    return "Browser opened"