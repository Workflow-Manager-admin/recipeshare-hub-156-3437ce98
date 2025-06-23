from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="RecipeShare Backend API",
    description=(
        "Backend API for managing recipes, user accounts, and comments "
        "in the RecipeShare web app."
    ),
    version="0.1.0",
    openapi_tags=[
        {"name": "recipes", "description": "Operations related to recipes"},
        {"name": "users", "description": "User account operations"},
        {"name": "comments", "description": "Recipe comments operations"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PUBLIC_INTERFACE
@app.get("/", tags=["Health"])
def health_check():
    """Simple health check endpoint for Recipe Backend."""
    return {"message": "Healthy"}


# --- Models ---

class RecipeStub(BaseModel):
    """Stub for recipe."""

    id: int = Field(..., description="Unique recipe ID")
    title: str = Field(..., description="Title of the recipe")


class UserStub(BaseModel):
    """Stub for user."""

    id: int = Field(..., description="Unique user ID")
    username: str = Field(..., description="Unique username")


class CommentStub(BaseModel):
    """Stub for comment."""

    id: int = Field(..., description="Unique comment ID")
    recipe_id: int = Field(
        ...,
        description="ID of the recipe this comment belongs to"
    )
    content: str = Field(..., description="Comment content")


# --- Routers ---

recipes_router = APIRouter(prefix="/recipes", tags=["recipes"])


# PUBLIC_INTERFACE
@recipes_router.get(
    "/",
    summary="Browse recipes",
    description="Get a list of all recipes.",
    response_model=list[RecipeStub]
)
async def browse_recipes():
    """Returns a list of recipe stubs (placeholder implementation)."""
    return [
        RecipeStub(id=1, title="Spaghetti Bolognese"),
        RecipeStub(id=2, title="Classic Apple Pie"),
    ]

# PUBLIC_INTERFACE
@recipes_router.get(
    "/{recipe_id}",
    summary="View recipe details",
    description="Get detailed information for a specific recipe.",
    response_model=RecipeStub
)
async def get_recipe(recipe_id: int):
    """Returns details for a single recipe (placeholder implementation)."""
    return RecipeStub(id=recipe_id, title="Sample Recipe")


users_router = APIRouter(prefix="/users", tags=["users"])


# PUBLIC_INTERFACE
@users_router.post(
    "/",
    summary="Register user",
    description="Register a new user account.",
    response_model=UserStub
)
async def register_user(username: str):
    """Registers a new user (placeholder implementation)."""
    return UserStub(id=1, username=username)


# PUBLIC_INTERFACE
@users_router.post(
    "/login",
    summary="User login",
    description="User login endpoint.",
    response_model=UserStub
)
async def login_user(username: str):
    """User login stub (placeholder implementation)."""
    return UserStub(id=1, username=username)


comments_router = APIRouter(prefix="/comments", tags=["comments"])


# PUBLIC_INTERFACE
@comments_router.post(
    "/",
    summary="Add comment",
    description="Add a comment to a recipe.",
    response_model=CommentStub
)
async def add_comment(recipe_id: int, content: str):
    """Adds a comment to a recipe (placeholder implementation)."""
    return CommentStub(id=1, recipe_id=recipe_id, content=content)


# PUBLIC_INTERFACE
@comments_router.get(
    "/by-recipe/{recipe_id}",
    summary="List comments for a recipe",
    description="Get all comments for a specific recipe.",
    response_model=list[CommentStub]
)
async def get_comments_for_recipe(recipe_id: int):
    """Fetches comments for a recipe (placeholder implementation)."""
    return [
        CommentStub(id=1, recipe_id=recipe_id, content="Looks delicious!"),
        CommentStub(id=2, recipe_id=recipe_id, content="Can't wait to try this."),
    ]


# --- Register Routers ---


app.include_router(recipes_router)
app.include_router(users_router)
app.include_router(comments_router)
