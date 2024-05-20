from faker import Faker

from yatmos.database import engine, SessionLocal, Base

from yatmos.project.crud import create_project
from yatmos.project.schema import ProjectCreate

from yatmos.suite.crud import create_suite
from yatmos.suite.schema import SuiteCreate

from yatmos.case.crud import create_case
from yatmos.case.schema import CaseCreate

from yatmos.step.crud import add_step
from yatmos.step.schema import StepCreate


fake = Faker()

PROJECTS_COUNT = 10
RUNS_PER_PROJECT = 2
SUITES_PER_PROJECT = 5
CASES_PER_SUITE = 5
STEPS_PER_CASE = 3

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

for _ in range(PROJECTS_COUNT):
    project = create_project(db, ProjectCreate(title=fake.company(), desc=fake.catch_phrase()))

    for _ in range(SUITES_PER_PROJECT):
        # TODO add subsuites
        suite = create_suite(db, SuiteCreate(title=fake.company(), desc=fake.text()), project.id)

        for _ in range(CASES_PER_SUITE):
            case = create_case(db, CaseCreate(title=fake.sentence(), desc=fake.text()), suite.id)

            for _ in range(STEPS_PER_CASE):
                step = add_step(db, StepCreate(title=fake.sentence(), desc=fake.text()), case.id)

    for _ in range(RUNS_PER_PROJECT):
        project.make_run(db, title=fake.date_this_year().isoformat(), desc=fake.sentence())
