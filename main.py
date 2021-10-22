import urllib.request
import urllib.parse
import re
from collections import Counter


class Riwords:

    def __init__(self, url):
        self.url = url
        self.url_list = []
        self.next_url_list = []
        self.dict = self.read()  # external dict

        # self.write()
        # self.parse_internal_url()

    def ignore_html(self, w):
        w = re.sub("/$", "",
                   re.sub("«\xa0", "",
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
                                                                                                re.sub("(.)*[&#]+(.)*",
                                                                                                       "",
                                                                                                       re.sub("(//)",
                                                                                                              "https://",
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
                                                                                                                          ))))))))))))))))))

        if "http" not in w:
            return w
        else:
            self.url_list.append(w)
            return ""

    def get_most_common_words(self):
        return self.dict.most_common(70)

    def filter_url_list(self):
        ignore_words = ["wikimedia", "Privacy_policy", "favicon", "js", "css", "min", "php", "wp", "wp-includes", "paie"]

        for url in self.url_list:
            for mcw in self.get_most_common_words():
                splitted_url = re.split("[.-]", repr(url))
                if repr(mcw[0]).strip().lower() in repr(splitted_url).strip().lower() and url not in self.next_url_list:
                    self.next_url_list.append(url)  # add url
                    self.url_list.remove(url)
                    break

        for iw in ignore_words:
            for nurl in self.next_url_list:
                if iw in nurl:
                    print(iw + " == " + nurl)
                    self.next_url_list.remove(nurl)
                    break

    def read(self):
        with urllib.request.urlopen(self.url) as url:
            return Counter(
                self.ignore_html(urllib.parse.unquote_plus(w.decode("utf-8"))) for l in url for w in l.split())

    def write(self):
        with open("test.txt", "a", encoding="utf-8") as f:
            for w in self.dict.most_common():
                if 3 < len(w[0]) <= 12:
                    # 3: pour retirer les petits mots utilisés qui ont une très grande frequence d'utilisation
                    # 12: longueur du mot maximum qui ont une frequence > 0.01 en langue francaise
                    f.write(w[0].strip().lower())
                    f.write("\n")

    def parse_internal_url(self, nb_internal_url):
        self.filter_url_list()
        print(self.url_list)
        print(self.next_url_list)


if __name__ == '__main__':
    riwords = Riwords(
        "https://fr.wikipedia.org/wiki/League_of_Legends:_Wild_Rift")
    riwords.parse_internal_url(1)
    riwords.write()
    # print(len(riwords.dict))
    # print(riwords.dict)
    # print(len(riwords.next_url_list))
    # print(riwords.next_url_list)
