
import os, json
import requests
from environment import Environment

def get_sections(title,chapter,part,subpart):
    url = "https://www.ecfr.gov/api/versioner/v1/versions/title-{title}.json?chapter={chapter}&part={part}&subpart={subpart}".format(title = title, chapter=chapter, part=part, subpart = subpart)
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

def save_section(date, xml, practice, title, chapter, part, subpart, section):
    current_dir = os.path.dirname(__file__)
    grandparent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
    xml_file_path = os.path.join(grandparent_dir, "data/{practice}/cfr/title-{title}/chapter-{chapter}/part-{part}/subpart-{subpart}/section-{section}/source.xml".format(
        practice=practice,
        title=title,
        chapter=chapter,
        part=part,
        subpart=subpart,
        section=section
        ))
    os.makedirs(os.path.dirname(xml_file_path), exist_ok=True)
    with open(xml_file_path, 'w') as xml_file:
        xml_file.write(xml)
    metadata = {"date": date, "data": { "title": title, "chapter": chapter, "part": part, "subpart": subpart, "section": section }}
    json_file_path = xml_file_path.replace("source.xml","metadata.json")
    with open(json_file_path, 'w') as json_file:
        json_file.write(json.dumps(metadata))
    return xml_file_path

def main():
    sections = get_sections(title = Environment.cfr_title, chapter=Environment.cfr_chapter, part=Environment.crf_part, subpart = Environment.crf_subpart)
    for section in sections:
        print(section)
        xml = get_section(date=section["date"], title=section["title"], subpart=section["subpart"], identifier=section["identifier"])
        xml_file_path = save_section(date=section["date"], xml=xml, practice=Environment.practice, title=section["title"], chapter=Environment.cfr_chapter, part=section["part"], subpart=section["subpart"], section=section["identifier"])
        print(xml_file_path)
if __name__ == "__main__":
    main()