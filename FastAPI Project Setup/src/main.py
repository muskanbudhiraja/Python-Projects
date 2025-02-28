from typing import Any
from fastapi import FastAPI
import uvicorn
from src.api.router import router
from fastapi.openapi.utils import get_openapi

app= FastAPI()
app.include_router(router)

def custom_openapi() -> Any:
    """custom_openapi

    Returns:
        Any: any
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="settings_title",
        version="settings.appversion",
        description="settings.description",
        routes=app.routes,
        servers=[
            {
                "url": f"{"settings.hostname"}{"settings.base_path"}",
                "description": "Server url",
            },
        ],
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

## custom swagger open api specs if want to do changes
app.openapi = custom_openapi  # type: ignore[method-assign]

def start() -> None:
    ##start uvicorn server
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__== "__main__":
    ## entrypoint
    start()