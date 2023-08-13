from typing import Union

import click
from flask import Flask, request

from constants import ResumeSections as Sections
from resume_services import get_section

app = Flask("resume")


@app.route("/personal")
def get_resume_personal() -> Union[dict, int]:
    """Retrieve the `Personal` section of a resume.

    Receives `resume` as an URL parameter, but it defaults to
    "sorin_sirghe.txt" for simplicity.
    """

    resume = request.args.get("resume", "sorin_sirghe.txt")

    response, status_code = get_section(Sections.PERSONAL.value, resume)

    return response, status_code, {"Content-Type": "application/json"}


@app.route("/experience")
def get_resume_experience() -> Union[dict, int]:
    """Retrieve the `Experience` section of a resume.

    Receives `resume` as an URL parameter, but it defaults to
    "sorin_sirghe.txt" for simplicity.
    """

    resume = request.args.get("resume", "sorin_sirghe.txt")

    response, status_code = get_section(Sections.EXPERIENCE.value, resume)

    return response, status_code, {"Content-Type": "application/json"}


@app.route("/education")
def get_resume_education() -> Union[dict, int]:
    """Retrieve the `Education` section of a resume.

    Receives `resume` as an URL parameter, but it defaults to
    "sorin_sirghe.txt" for simplicity.
    """

    resume = request.args.get("resume", "sorin_sirghe.txt")

    response, status_code = get_section(Sections.EDUCATION.value, resume)

    return response, status_code, {"Content-Type": "application/json"}


@app.route("/extra")
def get_resume_extra() -> Union[dict, int]:
    """Retrieve the `Extra` section of a resume.

    Receives `resume` as an URL parameter, but it defaults to
    "sorin_sirghe.txt" for simplicity.
    """

    resume = request.args.get("resume", "sorin_sirghe.txt")

    response, status_code = get_section(Sections.EXTRA.value, resume)

    return response, status_code, {"Content-Type": "application/json"}


@app.route("/all")
def get_resume_all() -> Union[dict, int]:
    """Retrieve the the entire resume.

    Receives `resume` as an URL parameter, but it defaults to
    "sorin_sirghe.txt" for simplicity.
    """

    resume = request.args.get("resume", "sorin_sirghe.txt")

    response, status_code = get_section(Sections.ALL.value, resume)

    return response, status_code, {"Content-Type": "application/json"}


@app.cli.command("get_resume")
@click.option(
    "--section",
    default="all",
    type=str,
    help="The resume section you wish to see. Default is 'all'.",
)
@click.option(
    "--resume",
    default="sorin_sirghe.txt",
    type=str,
    help="The filename of the resume. Default is 'sorin_sirghe.txt'.",
)
def get_cli_resume(section: str, resume: str) -> None:
    """Retrieve a section of a given resume.

    Options:

    - Section: Defaults to `all`.
    - Resume: Defaults to `sorin_sirghe.txt`.
    """

    response, status_code = get_section(section, resume)

    print(f"Status code: {status_code}\nResume: {response}")
