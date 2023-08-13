from enum import Enum


class ResumeSections(Enum):
    PERSONAL = "personal"
    EXPERIENCE = "experience"
    EDUCATION = "education"
    EXTRA = "extra"
    ALL = "all"


class Regexes(Enum):
    ENTRY = r"<entry>(.*?)<\/entry>"
    EXTRA = r"<extra>(.*)<\/extra>"
    EXTRA_SECTIONS = r"title=(?P<title>.*)\ndescription=(?P<description>.*)\nlocation=(?P<location>.*)\ntime_period=(?P<time_period>.*)\n"
    EDUCATION = r"<education>(.*)<\/education>"
    EDUCATION_SECTIONS = r"institution=(?P<institution>.*?)\nlocation=(?P<location>.*?)\ntime_period=(?P<time_period>.*?)\ndegree=(?P<degree>.*?)\n"
    EXPERIENCE = r"<experience>(.*)<\/experience>"
    EXPERIENCE_SECTIONS = r"company=(?P<company>.*)\ntitle=(?P<title>.*)\nlocation=(?P<location>.*)\ndescription=(?P<description>.*)\ntime_period=(?P<time_period>.*)\ntechnologies=(?P<technologies>.*)\n"
    PERSONAL = r"<personal>\nname=(?P<name>.*)\ntitle=(?P<title>.*)\nphone_numbers=(?P<numbers>.*)\nemail=(?P<email>.*)\nlinks=(?P<links>.*)\nsummary=(?P<summary>.*)\n<\/personal>"
