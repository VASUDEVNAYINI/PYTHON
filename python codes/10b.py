import webbroweser
def open_url__in_browser(url):
    try:
        webbrowser.open(url)
    except exception as e:
        print(f"Error: {e}")
url="https://chat.openai.com/"
open_url__in_browser(url)