from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..models import Response, ErrorResponse
from ..models.project import add_project, delete_project, retrieve_project, retrieve_projects, update_project, Project, UpdateProject

router = APIRouter()


@router.post("/", response_description="Project data added to database")
async def create_project(project: Project = Body(...)):
    project = jsonable_encoder(project)
    new_project = await add_project(project)
    return Response(new_project, "Project created successfully.")


@router.get("/", response_description="Projects retrieved")
async def get_projects():
    all_projects = await retrieve_projects()
    if all_projects:
        return Response(all_projects, "Projects data retrieved successfully")
    return Response(all_projects, "Empty list returned")


@router.get("/{id}", response_description="Project retrieved")
async def get_project(id):
    project = await retrieve_project(id)
    if project:
        return Response(project, "Project data retrieved successfully")
    return ErrorResponse("An error occurred.", 404, "Project doesn't exist.")


@router.put("/{id}", summary="Update project")
async def update_project_data(id: str, req: UpdateProject = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_project = await update_project(id, req)
    if updated_project:
        return Response(
            "Project with ID: {} name update is successful".format(id),
            "Project name updated successfully",
        )
    return ErrorResponse(
        "An error occurred",
        404,
        "There was an error updating the project data.",
    )


@router.delete("/{id}", summary="Delete project", response_description="Project data deleted from the database")
async def delete_project_data(id: str):
    deleted_project = await delete_project(id)
    if deleted_project:
        return Response(
            "Project with ID: {} removed".format(id), "Project deleted successfully"
        )
    return ErrorResponse(
        "An error occurred", 404, "Project with id {0} doesn't exist".format(id)
    )
