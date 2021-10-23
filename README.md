# RiWords

## Author

[![Linkedin: Thierry Khamphousone](https://img.shields.io/badge/-Thierry_Khamphousone-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tkhamphousone/)](https://www.linkedin.com/in/tkhamphousone)

---

<br/>

## Setup

```bash
$ git clone https://github.com/Yulypso/RiMaze.git
$ cd Rimaze
```

---

<br/>

## Start RiWords 

```bash
$ python3 main.py [--help] --url <url> --output <output file name> [--deep <value>] [--verbose]
```

```bash
-- Riwords arguments--

  -h, --help                    show this help message and exit
  --url <url>                   source url to parse and retrieves words from the web page
  --output <output file name>   file name which contains output words
  --deep <value>                search deep level under source url
  --verbose                     get more information
```

## Example

```bash
$ python3 main.py --url https://fr.wikipedia.org/wiki/Commissariat_%C3%A0_l%27%C3%A9nergie_atomique_et_aux_%C3%A9nergies_alternatives --output RiWords.txt --deep 2
```