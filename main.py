from fastapi import FastAPI

from src.apps.project.api import router as project_router
from src.apps.user.api import router as user_router
from src.core.domain.exception import (
    AsyncTaskException,
    AuthException,
    NoPermissionException,
    NotFoundException,
    async_task_handler,
    authing_handler,
    no_permission_handler,
    not_found_handler,
)
from src.core.domain.settings import FAST_API_DOCS_URL, FAST_API_REDOC_URL

app = FastAPI(
    title="Nebula API", docs_url=FAST_API_DOCS_URL, redoc_url=FAST_API_REDOC_URL
)

app.include_router(project_router, prefix="/api/v1/project", tags=["project"])
app.include_router(user_router, prefix="/api/v1/user", tags=["user"])

app.add_exception_handler(NoPermissionException, no_permission_handler)
app.add_exception_handler(NotFoundException, not_found_handler)
app.add_exception_handler(AsyncTaskException, async_task_handler)
app.add_exception_handler(AuthException, authing_handler)
