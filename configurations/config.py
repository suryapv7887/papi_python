# configurations/config.py

class Config:
    ENVIRONMENTS = {
        "qa": "https://qa-papi.simelabs.in",
        "dev": "https://dev-papi.simelabs.in"
    }
    DEFAULT_BROWSER = "chrome"
    DEFAULT_ENV = "qa"

    @classmethod
    def get_base_url(cls, env):
        return cls.ENVIRONMENTS.get(env.lower(), cls.ENVIRONMENTS[cls.DEFAULT_ENV])
