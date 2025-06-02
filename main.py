from typing import Any, Annotated
import httpx
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# ---------- App Info ----------

app = FastAPI(
    title="Navigator Tool Template",
    description="The Navigator tool template provides a starting point for creating new Navigator tools.",
    version="1.0.0",
)

# Enable CORS for external service communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Schemas ----------

class Input(BaseModel):
    """
    Form-based input schema for template.
    """
    data: Annotated[
        str,
        Form(..., description="Verbose description of the input data expected by this tool.")
    ]


class Output(BaseModel):
    """
    Form-based output schema for template.
    """
    data: Any = Field(
        ...,
        title="Output Data",
        examples=["Example output data."],
        description="Verbose description of the output data returned by this tool.",
    )

# ---------- Only one endpoint ----------

@app.post("/call/", response_model=Output)
async def call(
    data: Annotated[str, Form(description="Verbose description of the input data expected by this tool.")]
) -> Output | JSONResponse:
    """
    Process the input data and return the output.
    """
    async with httpx.AsyncClient() as client:
        try:
            return Output(data=data)
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            return JSONResponse({"error": f"Request failed: {e}"}, status_code=500)

@app.get("/health", response_class=JSONResponse)
async def health_check():
    """Health check endpoint."""
    return {"status": "Application is running."}
