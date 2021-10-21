import urllib.request
import re
from collections import Counter


class Riwords:

    def __init__(self, url):
        self.url = url
        self.webpage = self.read()

    def ignore_html(self, w):
        return re.sub("^(?!href=\")((.)*\")", "",
            re.sub("(<!?-?-?.+-?-?>)", "", w)
        )


    def read(self):
        with urllib.request.urlopen(self.url) as url:
            return Counter(self.ignore_html(w.decode("utf-8")) for l in url for w in l.split())


if __name__ == '__main__':
    riwords = Riwords(
        "https://fr.wikipedia.org/wiki/Commissariat_%C3%A0_l%27%C3%A9nergie_atomique_et_aux_%C3%A9nergies_alternatives")
    print(len(riwords.webpage))
