from enum import Enum


class ResumeSections(Enum):
    PERSONAL = "personal"
    EXPERIENCE = "experience"
    EDUCATION = "education"
    EXTRA = "extra"
    ALL = "all"

    @classmethod
    def is_individual_section(cls, section: str) -> bool:
        return section in (
            cls.PERSONAL.value,
            cls.EXPERIENCE.value,
            cls.EDUCATION.value,
            cls.EXTRA.value,
        )
