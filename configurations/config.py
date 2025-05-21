from pytest_metadata.plugin import metadata


class Config:
    ENVIRONMENTS = {
        "qa": "https://qa-papi.simelabs.in",
        "dev": "https://dev-papi.simelabs.in"
    }
    DEFAULT_BROWSER = "chrome"
    DEFAULT_ENV = "qa"
    DEFAULT_HEADLESS = False

    LOGIN_USERNAME = "dev@simelabs.in"
    LOGIN_PASSWORD = "1~5An)4VlQrl"



    @classmethod
    def get_base_url(cls, env):
        return cls.ENVIRONMENTS.get(env.lower(), cls.ENVIRONMENTS[cls.DEFAULT_ENV])


