"""
Given a DOI, generate a YAML block for data/publications/publications.yaml

Review that the results are accurate before submitting!
"""

import requests
import yaml
from string import ascii_lowercase

_seen_keys = set()


def request_doi(doi):
    r = requests.get(
        f"http://dx.doi.org/{doi}", headers={"Accept": "application/vnd.citationstyles.csl+json"},
    )
    r.raise_for_status()
    return r.json()


def citation_to_dict(data):
    authors = []
    key = ""
    for author in data["author"]:
        if author["sequence"] == "first":
            key += "".join(author["family"].lower().split())
        if (author["given"], author["family"]) == ("Andrea", "Volkamer"):
            authors.append("andrea.volkamer")
        else:
            authors.append(f'{author["given"]} {author["family"]}')
    try:
        date = data["published-online"]["date-parts"][0]
    except KeyError:
        date = data["published-print"]["date-parts"][0]
    year = date[0]

    ## Create unique key
    key += str(year)
    keyprobe = f"{key}"
    letters = iter(ascii_lowercase)
    while keyprobe in _seen_keys:
        keyprobe = f"{key}{next(letters)}"
    key = keyprobe
    _seen_keys.add(key)

    return {
        key: {
            "key": key,
            "title": data["title"],
            "authors": authors,
            "journal": data["container-title"],
            "volume": data["volume"],
            "issue": data["issue"],
            "pages": data["page"],
            "year": year,
            "date": "-".join(map(str, date)),
            "doi": data["DOI"],
            "image": "",
            "pdf": "",
            "kind": "article",
        }
    }


if __name__ == "__main__":
    import sys

    for arg in sys.argv[1:]:
        try:
            data = request_doi(arg)
            print(yaml.dump(citation_to_dict(data)))
            print()
        except Exception as e:
            print(f"# ERROR with doi {arg}: {e}. Payload:", file=sys.stderr)
