from fastapi import APIRouter, HTTPException

from ..schemas.website import (
    WebsiteGenerateRequest,
    WebsiteGenerateResponse,
    DeployRequest,
    DeployResponse,
)
from ..services.codegen import generate_website
from ..services.github_deploy import create_repo, push_files, build_vercel_deploy_url

router = APIRouter()


@router.post("/generate", response_model=WebsiteGenerateResponse)
async def generate(request: WebsiteGenerateRequest):
    try:
        files = await generate_website(request.idea)
        return WebsiteGenerateResponse(files=files)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/deploy", response_model=DeployResponse)
async def deploy(request: DeployRequest):
    try:
        repo = await create_repo(request.github_token, request.repo_name)
        await push_files(
            request.github_token, repo["owner"]["login"], repo["name"], request.files
        )
        return DeployResponse(
            repo_url=repo["html_url"],
            vercel_deploy_url=build_vercel_deploy_url(repo["html_url"]),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
