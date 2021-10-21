import urllib.request
import re
from collections import Counter


class Riwords:

    def __init__(self, url):
        self.url = url
        self.webpage = self.read()
        self.count = self.occurs()

    def ignore_html(self, w):
        return re.sub("[\(\)]?", "",
            re.sub("^(?!href=\"|js|images)((.)*\")", "",
            re.sub("<(.)*$", "",
            re.sub("(.)*\">", "",
            re.sub("<(.)*>", "",
            re.sub("^style=\"\">", "",
            re.sub("(<(.)*/>)", "",
            re.sub("^(<)(!--)?(.)*(--)?(>)$", "", w)
        )))))))

    def occurs(self):
        return Counter(w for w in self.webpage)

    def read(self):
        with urllib.request.urlopen(self.url) as url:
            return set(self.ignore_html(w.decode("utf-8")) for l in url for w in l.split())


if __name__ == '__main__':
    riwords = Riwords(
        "https://fr.wikipedia.org/wiki/Commissariat_%C3%A0_l%27%C3%A9nergie_atomique_et_aux_%C3%A9nergies_alternatives")
    print(riwords.count)
