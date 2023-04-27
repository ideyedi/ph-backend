from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import (users,
                         products,
                         )
from src.version import __version__ as proj_version

app = FastAPI(
    title="ph-server",
    version=proj_version,
    docs_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(products.router)
