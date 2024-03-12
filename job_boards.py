"""
Job Boards scraping details for
each job board: Indeed, OCC
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class BoardScrapper:
    job_title: str
    job_type: str | None
    keywords: Optional[str] | Optional[List[str]]


class IndeedScrapper(BoardScrapper):

    def __repr__(self):
        return f"IndeedScrapper(job_title={self.job_title}, job_type={
        self.job_type}, keywords={self.keywords})"


if __name__ == "__main__":
    indeed = IndeedScrapper(job_title="Fullstack Developer",
                            job_type="Remote", keywords=None)
    print(repr(indeed))
