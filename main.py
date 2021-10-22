import urllib.request
import urllib.parse
import re
from collections import Counter


def ignore_html(w):
    return re.sub("'\u202f'", "",
                  re.sub("(.)*[\\\]+(.)*", "",
                  re.sub("(.)*[}]+(.)*", "",
                         re.sub("(.)+(svg|png|jpg|jpeg|gif|pdf|svg)", "",
                                re.sub("[a-zA-Z0-9]+-[a-zA-Z0-9]+-[a-zA-Z0-9]+(.)*", "",
                                       re.sub("[a-zA-Z]+-[0-9]+", "",
                                              re.sub("((.)+=\")?[\"]?", "",
                                                     re.sub("(.)*[&#]+(.)*", "",
                                                            re.sub("(//)", "https://",
                                                                   re.sub("^(?!href=\"//)(href=\"([/#]).*)", "",
                                                                          re.sub("(\"«&#160;)", "",
                                                                                 re.sub(
                                                                                     "(((>)?<.*)?(>)?(/>)?(\[)?(])?(\()?(\))?)(\|)?((.)*:)?(·)?({)?(\\)(})?)?",
                                                                                     "",
                                                                                     re.sub("^(?!href=\")((.)*\")", "",
                                                                                            re.sub("(<!?-?-?.+-?-?>)",
                                                                                                   "", w)
                                                                                            )))))))))))))


class Riwords:

    def __init__(self, url):
        self.url = url
        self.webpage = self.read()
        self.write()

    def read(self):
        with urllib.request.urlopen(self.url) as url:
            return Counter(ignore_html(w.decode("utf-8")) for l in url for w in l.split())

    def write(self):
        with open("test.txt", "w", encoding="utf-8") as f:
            for i in self.webpage.keys():
                f.write(i.strip().lower())
                f.write("\n")


if __name__ == '__main__':
    riwords = Riwords(
        "https://fr.wikipedia.org/wiki/Commissariat_%C3%A0_l%27%C3%A9nergie_atomique_et_aux_%C3%A9nergies_alternatives")
    print(len(riwords.webpage))
    print(riwords.webpage)
