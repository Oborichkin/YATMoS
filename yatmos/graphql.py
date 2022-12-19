from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper, StrawberrySQLAlchemyLoader

from yatmos.dependencies import get_db
from yatmos.project.model import Project as ProjectModel  # noqa: F401
from yatmos.suite.model import Suite as SuiteModel, SuiteResult  # noqa: F401
from yatmos.case.model import Case, CaseResult  # noqa: F401
from yatmos.step.model import Step, StepResult  # noqa: F401

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


@strawberry_sqlalchemy_mapper.type(ProjectModel)
class Project:
    pass


@strawberry_sqlalchemy_mapper.type(SuiteModel)
class Suite:
    pass


async def get_context(db: Session = Depends(get_db)):
    return {"db": db, "sqlalchemy_loader": StrawberrySQLAlchemyLoader(bind=db)}


@strawberry.type
class Query:
    @strawberry.field
    def projects(self, info: Info) -> List[Project]:
        return info.context["db"].query(ProjectModel).all()

    @strawberry.field
    def suites(self, info: Info) -> List[Suite]:
        return info.context["db"].query(SuiteModel).all()


# call finalize() before using the schema:
# (note that models that are related to models that are in the schema
# are automatically mapped at this stage -- e.g., Department is mapped
# because employee.department is a relationshp to Department)
strawberry_sqlalchemy_mapper.finalize()
# only needed if you have polymorphic types
additional_types = list(strawberry_sqlalchemy_mapper.mapped_types.values())
schema = strawberry.Schema(Query, types=additional_types)
graphql_app = GraphQLRouter(schema, context_getter=get_context)
