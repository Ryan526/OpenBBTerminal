from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from openbb_core.app.model.hub.hub_session import HubSession


class Profile(BaseModel):
    hub_session: Optional[HubSession] = Field(default=None)
    model_config = ConfigDict(validate_assignment=True)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )
