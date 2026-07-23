from pydantic import BaseModel
from typing import Dict


class WebsiteGenerateRequest(BaseModel):
    idea: str


class WebsiteGenerateResponse(BaseModel):
    files: Dict[str, str]


class DeployRequest(BaseModel):
    files: Dict[str, str]
    repo_name: str
    github_token: str  # never persisted — used once, in-memory, for this request only


class DeployResponse(BaseModel):
    repo_url: str
    vercel_deploy_url: str
