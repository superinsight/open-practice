import os


class Environment:
    cfr_title = os.getenv("CFR_TITLE", "38")
    cfr_chapter = os.getenv("CFR_CHAPTER", "I")
    cfr_subchapter = os.getenv("CFR_SUBCHAPTER", "4")
    crf_part = os.getenv("CFR_PART", "4")
    crf_subpart = os.getenv("CFR_SUBPART", "B")
    practice = os.getenv("PRACTICE", "va")