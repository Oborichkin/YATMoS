import argparse
from datetime import datetime
from junitparser import JUnitXml
from yatmos.database import SessionLocal
from yatmos.project.crud import get_project_by_name

PROJECT_NAME = "yatmos"

parser = argparse.ArgumentParser()
parser.add_argument("filename")
# args = parser.parse_args()


# This should be a single transaction!
def main():
    db = SessionLocal()
    xml = JUnitXml.fromfile("report.xml")
    project = get_project_by_name(db, PROJECT_NAME, or_create=True)
    run = project.make_run(db, title=str(datetime.now()), desc="junit import test", make_suites=False)

    for suite in xml:
        project_suite = project.get_suite(db, suite.name, or_create=True)
        suite_result = project_suite.make_result(db, run.id, make_cases=False)
        for case in suite:
            suite_case = project_suite.get_case(db, f"{case.name}", or_create=True)
            suite_case.make_result(db, run.id, suite_result.id, make_steps=False)
