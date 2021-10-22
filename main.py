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
                    self.next_url_list.remove(nurl)
                    break

        for i, nurl in enumerate(self.next_url_list):
            splitted_url = re.split("/", repr(nurl))
            token = re.sub("'", "", splitted_url[len(splitted_url)-1])
            nurl2 = re.sub("(\\b" + token + "\\b)(?!.*\\1)", "", nurl)
            self.next_url_list[i] = re.sub("/$", "", nurl2)



    def read(self):
        req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'})
        with urllib.request.urlopen(req) as url:
            return Counter(self.ignore_html(urllib.parse.unquote_plus(w.decode("utf-8"))) for l in url for w in l.split())

    def write(self):
        with open("test.txt", "a", encoding="utf-8") as f:
            for w in self.dict.most_common():
                if 3 < len(w[0]) <= 12:
                    # 3: pour retirer les petits mots utilisés qui ont une très grande frequence d'utilisation
                    # 12: longueur du mot maximum qui ont une frequence > 0.01 en langue francaise
                    f.write(w[0].strip())
                    f.write("\n")

    def parse_internal_url(self, nb_internal_url):
        self.filter_url_list()
        print(self.url_list)
        print(self.next_url_list)


if __name__ == '__main__':
    riwords = Riwords(
        "https://fr.wikipedia.org/wiki/Commissariat_%C3%A0_l%27%C3%A9nergie_atomique_et_aux_%C3%A9nergies_alternatives")
    riwords.parse_internal_url(1)
    riwords.write()
    # print(len(riwords.dict))
    # print(riwords.dict)
    # print(len(riwords.next_url_list))
    # print(riwords.next_url_list)
