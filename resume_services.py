import json
from http import HTTPStatus
from typing import Union

from constants import ResumeSections as Sections


def read_resume(resume: str) -> dict:
    """Attempt to read the contents of the specified resume.

    Arguments:
      - resume str: the name of the resume to be read.

    Raises:
      - FileNotFoundError: when the file does not exist.
      - JSONDecodeError: when the file is empty
    """

    resumes_dir = "./resumes/"

    with open(f"{resumes_dir}{resume}", "r") as f:
        return json.load(f)


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
    except json.decoder.JSONDecodeError:
        return {"message": "Requested resume is empty."}, HTTPStatus.BAD_REQUEST

    resume_section = resume
    if Sections.is_individual_section(section):
        resume_section = resume.get(section)

    if resume_section is None:
        return {"message": "Requested resume section is empty."}, HTTPStatus.BAD_REQUEST

    return resume_section, HTTPStatus.OK
