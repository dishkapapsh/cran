from environs import Env
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str
    ADMIN_ID: id

@dataclass
class Settings:
    bots: Bots

def get_settings(path: str):
    env= Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            ADMIN_ID=env.int("admin_id")
        )
    )

settings= get_settings('env')
print(settings)