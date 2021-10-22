import urllib.request
import urllib.parse
import re
from collections import Counter


class Riwords:

    def __init__(self, url):
        self.url = url
        self.url_list = []
        self.next_url_list = []
        self.webpage = self.read()
        self.write()
        self.parse_internal_url()

    def ignore_html(self, w):
        w = re.sub("«\xa0", "",
                   re.sub("^([0-9]+).([0-9]+)(%)?", "",
                   re.sub(",", "",
                          re.sub("(.)*?[;]", "",
                                 re.sub("'\u202f'", "",
                                        re.sub("(.)*[\\\]+(.)*", "",
                                               re.sub("(.)*[}]+(.)*", "",
                                                      re.sub("(.)+(svg|png|jpg|jpeg|gif|pdf|svg)", "",
                                                             re.sub("[\.-]*$", "",
                                                                    re.sub("[a-zA-Z]+-[0-9]+", "",
                                                                           re.sub("((.)+=\")?[\"]?", "",
                                                                                  re.sub("(.)*[&#]+(.)*", "",
                                                                                         re.sub("(//)", "https://",
                                                                                                re.sub(
                                                                                                    "^(?!href=\"//)(href=\"([/#]).*)",
                                                                                                    "",
                                                                                                    re.sub(
                                                                                                        "(\"«&#160;)",
                                                                                                        "",
                                                                                                        re.sub(
                                                                                                            "(((>)?<.*)?(>)?(/>)?(\[)?(])?(\()?(\))?)(\|)?((.)*:)?(·)?({)?(\\)(})?)?",
                                                                                                            "",
                                                                                                            re.sub(
                                                                                                                "^(?!href=\")((.)*\")",
                                                                                                                "",
                                                                                                                re.sub(
                                                                                                                    "(<!?-?-?.+-?-?>)",
                                                                                                                    "",
                                                                                                                    w)
                                                                                                            )))))))))))))))))

        if "http" not in w:
            return w
        else:
            self.url_list.append(w)
            return ""

    def get_most_common_words(self):
        return self.webpage.most_common(70)

    def filter_url_list(self):
        ignore_words = ["wikimedia", "Privacy_policy"]

        for url in self.url_list:
            for mcw in self.get_most_common_words():
                splitted_url = re.split("[.-]", repr(url))
                if repr(mcw[0]).strip().lower() in repr(splitted_url).strip().lower():
                    self.next_url_list.append(url)  # add url
                    self.url_list.remove(url)
                    break

        for nurl in self.next_url_list:
            for iw in ignore_words:
                if iw in nurl:
                    self.next_url_list.remove(nurl)
        print("done comparaison")

    def parse_internal_url(self):
        self.filter_url_list()
        print(self.url_list)

    def read(self):
        with urllib.request.urlopen(self.url) as url:
            return Counter(
                self.ignore_html(urllib.parse.unquote_plus(w.decode("utf-8"))) for l in url for w in l.split())

    def write(self):
        with open("test.txt", "a", encoding="utf-8") as f:
            for w in self.webpage.most_common():
                if 3 < len(w[0]) <= 12:
                    # 3: pour retirer les petits mots utilisés qui ont une très grande frequence d'utilisation
                    # 12: longueur du mot maximum qui ont une frequence > 0.01 en langue francaise
                    f.write(w[0].strip().lower())
                    f.write("\n")


if __name__ == '__main__':
    riwords = Riwords(
        "https://stackoverflow.com/questions/39744543/regex-for-detecting-repeating-symbols")
    print(len(riwords.webpage))
    print(riwords.webpage)
    print(len(riwords.next_url_list))
    print(riwords.next_url_list)
