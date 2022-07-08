from sqlalchemy.orm import Session
from .model import Project
from .schema import ProjectCreate, ProjectUpdate


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Project).offset(skip).limit(limit).all()


def create_project(db: Session, project: ProjectCreate):
    new_project = Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def delete_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id)
    project.delete()
    db.commit()


def update_project(db: Session, project_id: int, project: ProjectUpdate):
    upd_project = db.query(Project).filter(Project.id == project_id)
    upd_project.update(project.dict(exclude_unset=True))
    db.commit()
    upd_project = upd_project.first()
    db.refresh(upd_project)
    return upd_project
