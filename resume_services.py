import re
from http import HTTPStatus
from typing import Union

from constants import Regexes
from constants import ResumeSections as Sections


def read_resume(resume: str) -> str:
    """Attempt to read the contents of the specified resume.

    Arguments:
      - resume str: the name of the resume to be read.

    Raises:
      - FileNotFoundError: when the file does not exist.
    """

    resumes_dir = "./resumes/"

    with open(f"{resumes_dir}{resume}", "r") as f:
        return f.read()


def get_section(section: str, resume_file_name: str) -> Union[dict, int]:
    """Retrieve a section of a resume.

    Arguments:
      - section str: the section of the resume to retrieve.
      - resume_file_name str: the name of the resume file to be read.

      Returns:
      - (dict, int) - A tuple containing a dictionary that represents
                      the data or an error message and an integer that
                      represents the status code.
    """

    if section not in {section.value for section in Sections}:
        return {"message": "Invalid resume section requested"}, HTTPStatus.BAD_REQUEST

    try:
        resume = read_resume(resume_file_name)
    except FileNotFoundError:
        return {"message": "Requested resume not found."}, HTTPStatus.NOT_FOUND

    try:
        data, status = build_resume(section, resume)

        return data, status
    except Exception:
        # TODO log the error
        return {"message": "An error has occurred."}, HTTPStatus.INTERNAL_SERVER_ERROR


def build_resume(section: str, resume: str) -> Union[dict, int]:
    """Build the resume and return the requested section.

    Arguments:
      - section str: the section of the resume to retrieve.
      - resume str: the name of the resume file to be read.

      Returns:
      - (dict, int) - A tuple containing a dictionary and an integer.
    """

    complete_resume = {"personal": {}, "experience": [], "education": [], "extra": []}

    personal_section = re.search(Regexes.PERSONAL.value, resume, re.S)
    experience_section = re.search(Regexes.EXPERIENCE.value, resume, re.S)
    education_section = re.search(Regexes.EDUCATION.value, resume, re.S)
    extra_section = re.search(Regexes.EXTRA.value, resume, re.S)

    complete_resume["personal"] = personal_section.groupdict()

    experience_entries = re.findall(
        Regexes.ENTRY.value, experience_section.group(), re.S
    )
    for entry in experience_entries:
        exp_entry = re.search(Regexes.EXPERIENCE_SECTIONS.value, entry, re.S)
        complete_resume["experience"].append(exp_entry.groupdict())

    education_entries = re.findall(Regexes.ENTRY.value, education_section.group(), re.S)
    for entry in education_entries:
        edu_entry = re.search(Regexes.EDUCATION_SECTIONS.value, entry, re.S)
        complete_resume["education"].append(edu_entry.groupdict())

    extra_entries = re.findall(Regexes.ENTRY.value, extra_section.group(), re.S)
    for entry in extra_entries:
        extra_entry = re.search(Regexes.EXTRA_SECTIONS.value, entry, re.S)
        complete_resume["extra"].append(extra_entry.groupdict())

    return_content = complete_resume
    if section == Sections.PERSONAL.value:
        return_content = complete_resume[section]

    elif section == Sections.EXPERIENCE.value:
        return_content = complete_resume[section]

    elif section == Sections.EDUCATION.value:
        return_content = complete_resume[section]

    elif section == Sections.EXTRA.value:
        return_content = complete_resume[section]

    return return_content, HTTPStatus.OK
