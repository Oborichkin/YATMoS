from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from ..database import projects


class Project(BaseModel):
    title: str = Field(...)
    desc: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "YATMoS Backend",
                "desc": "YATMoS backend tests"
            }
        }

class UpdateProject(BaseModel):
    title: Optional[str]
    desc: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "YATMoS Backend",
                "desc": "YATMoS backend API tests"
            }
        }


def project_helper(project) -> dict:
    return {
        "id": str(project["_id"]),
        "title": project["title"],
        "desc": project.get("desc")
    }


# Retrieve all projects present in the database
async def retrieve_projects():
    all_projects = []
    async for project in projects.find():
        all_projects.append(project_helper(project))
    return all_projects


# Add a new project into to the database
async def add_project(project_data: dict) -> dict:
    project = await projects.insert_one(project_data)
    new_project = await projects.find_one({"_id": project.inserted_id})
    return project_helper(new_project)


# Retrieve a project with a matching ID
async def retrieve_project(id: str) -> dict:
    project = await projects.find_one({"_id": ObjectId(id)})
    if project:
        return project_helper(project)


# Update a project with a matching ID
async def update_project(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    project = await projects.find_one({"_id": ObjectId(id)})
    if project:
        updated_project = await projects.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_project:
            return True
        return False


# Delete a project from the database
async def delete_project(id: str):
    project = await projects.find_one({"_id": ObjectId(id)})
    if project:
        await projects.delete_one({"_id": ObjectId(id)})
        return True
