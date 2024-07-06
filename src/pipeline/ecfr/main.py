
import requests
from environment import Environment

def get_sections():
    url = "https://www.ecfr.gov/api/versioner/v1/versions/title-{title}.json?chapter={chapter}&part={part}&subpart={subpart}".format(title = Environment.cfr_title, chapter=Environment.cfr_chapter, part=Environment.crf_part, subpart = Environment.crf_subpart)
    payload = {}
    headers = {
    'accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    sections = response.json()["content_versions"]
    return sections


def get_section(date, title, subpart, identifier):
    url = "https://www.ecfr.gov/api/versioner/v1/full/{date}/title-{title}.xml?subpart={subpart}&section={identifier}".format(date= date, title=title, subpart=subpart, identifier=identifier)
    payload = {}
    headers = {
    'accept': 'application/xml'
    }
    xml = requests.request("GET", url, headers=headers, data=payload).text
    return xml 


def main():
    sections = get_sections()
    for section in sections:
        print(section)
        xml = get_section(date=section["date"], title=section["title"], subpart=section["subpart"], identifier=section["identifier"])
        print(xml)

if __name__ == "__main__":
    main()