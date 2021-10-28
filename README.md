# RiWords

Website parser in order to get a wordlist.

## Author

[![Linkedin: Thierry Khamphousone](https://img.shields.io/badge/-Thierry_Khamphousone-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tkhamphousone/)](https://www.linkedin.com/in/tkhamphousone)

---

<br/>

## Setup

```bash
$ git clone https://github.com/Yulypso/RiWords.git
$ cd RiWords
```

---

<br/>

## Start RiWords

```bash
$ python3 Riwords.py [--help] --url <url> --output <output file name> [--deep <value>] [--verbose]
```

```bash
-- Riwords arguments--

  -h, --help                        show this help message and exit
  --url, -u <url>                   source url to parse and retrieves words from the web page
  --output, -o <output file name>   file name which contains output words
  --deep, _d <value>                search deep level under source url
  --verbose, -v                     get more information
```

---

<br/>

## Examples

```bash
$ python3 Riwords.py -u https://fr.wikipedia.org/wiki/Commissariat_%C3%A0_l%27%C3%A9nergie_atomique_et_aux_%C3%A9nergies_alternatives -o Riwords.txt -d 1
```
