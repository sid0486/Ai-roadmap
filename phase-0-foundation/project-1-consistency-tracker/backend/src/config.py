from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    app_name : str = "consistency tracker"
    debug : bool = False
    database_url : str 
    secret_key : str
    postgres_user: str
    postgres_password : str
    postgres_db : str
    model_config = SettingsConfigDict(env_file = ".env",extra= "ignore")
settings = Settings()