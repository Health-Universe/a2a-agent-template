# tool-template
Template for making navigator tools

- 1 endpoint with a form based post

## Quickstart

```bash
# Create a new repository from this template
# Either use the GitHub "Use this template" button
# Or manually clone and reinitialize:
git clone https://github.com/Health-Universe/tool-template.git your-tool-name
cd your-tool-name
rm -rf .git
git init

# Start the application
docker-compose up --build

# Access the app at http://localhost:80
# API docs available at http://localhost:80/docs
```

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started/) and [Docker Compose](https://docs.docker.com/compose/install/)

### Running the Application
1. Create a new repository from this template:
   ```bash
   # Option 1: Use GitHub's "Use this template" button
   # Option 2: Clone and reinitialize manually:
   git clone https://github.com/Health-Universe/tool-template.git your-tool-name
   cd your-tool-name
   rm -rf .git
   git init
   ```

2. Start the application:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - FastAPI application: http://localhost:80
   - FastAPI documentation: http://localhost:80/docs

### Development
To make changes to the application:
1. Modify the FastAPI application in `main.py`
2. Update the API schema in `schemas.py`
3. The application includes hot reloading, so changes to the code will automatically reload the FastAPI server in development

For major changes:
- Rebuild the containers with `docker-compose up --build`

## Notes and Caveats
- multiselect fields must be specified like this:
```python
from pydantic import Field
from typing import List

multiselect_field: List[str] = Field(
  title="Multiselect Field",
    description="This is a multiselect field",
    json_schema_extra={
        "schema": {
            "items": ["Item 1", "Item 2", "Item 3"],
        }
    }
)
```


