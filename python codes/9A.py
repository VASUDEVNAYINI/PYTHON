import webbroweser
def open_url__in_browser(url):
    try:
        webbrowser.open(url)
    except exception as e:
        print(f"error: {e}")
url="https://apollouniversity.edu.in/"
open_url__in_browser(url)
