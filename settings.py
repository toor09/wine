from pydantic import BaseSettings, validator


class Settings(BaseSettings):

    DEFAULT_NAMES: str = "category,title,sort,price,image,promotion"
    FOUNDATION_YEAR: int = 1920
    PORT: int = 8000
    ROOT_PATH_IMG: str = "images/"

    @validator("DEFAULT_NAMES")
    def default_names(cls, v: str) -> list:
        if isinstance(v, str):
            return [_v.strip() for _v in v.split(",")]

    class Config:
        case_sensitive = True
        env_file = ".env"
