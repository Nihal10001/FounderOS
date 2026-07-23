import base64
import httpx

GITHUB_API = "https://api.github.com"


async def create_repo(token: str, repo_name: str) -> dict:
    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{GITHUB_API}/user/repos",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
            json={"name": repo_name, "private": False, "auto_init": True},
        )
        if res.status_code >= 400:
            raise ValueError(f"GitHub repo creation failed ({res.status_code}): {res.text}")
        return res.json()


async def push_files(token: str, owner: str, repo: str, files: dict[str, str]) -> None:
    """
    Pushes each file via the Contents API. Simple and reliable for a small
    file set — one commit per file rather than a single atomic tree commit,
    which is a fine trade-off for a handful of generated files.
    """
    async with httpx.AsyncClient() as client:
        for path, content in files.items():
            clean_path = path.lstrip("/")
            encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
            res = await client.put(
                f"{GITHUB_API}/repos/{owner}/{repo}/contents/{clean_path}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Accept": "application/vnd.github+json",
                },
                json={"message": f"Add {clean_path}", "content": encoded},
            )
            if res.status_code >= 400:
                raise ValueError(
                    f"Failed to push {clean_path} ({res.status_code}): {res.text}"
                )


def build_vercel_deploy_url(repo_html_url: str) -> str:
    return f"https://vercel.com/new/clone?repository-url={repo_html_url}"
