## What is ECFR?

ECFR is the digital repository for Code of Federal Regulations availalbe for API, XML, and PDF format.


## How it works
The main.py will take a setup of input paramenter from env variables such as title, chapter, part, subpart and and call the ecfr api to read all xml for each sections and save the xml file into [folder](/src/data).

## Example on calling the ECRF API and saving xml

Getting all sections base on title, chapter and subchapter
```
curl -X GET "https://www.ecfr.gov/api/versioner/v1/versions/title-38.json?chapter=I&subchapter=4" -H "accept: application/json"
```

Getting xml content base on title, subpart and section
```
curl -X GET "https://www.ecfr.gov/api/versioner/v1/full/2016-12-14/title-38.xml?subpart=B&section=4.40" -H "accept: application/xml"
```

The xml will be saved to [source.xml](/src/data/va/cfr/title-38/chapter-I/part-4/subpart-B/section-4.40/source.xml).
