from typing import Any

from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):
    text: str = Field(description='the text of the option shown to the user')
    nextNode: dict[str, Any] = Field(description='the next node content and its options')


class StoryNodeLLM(BaseModel):
    content: str = Field(description='the main content for the story node')
    isEnding: bool = Field(default=False, description='whether this node is an ending node')
    isWinningEnding: bool = Field(default=False, description='whether this node is a winning ending')
    options: list[StoryOptionLLM] | None = Field(default=None, description='the options for this node')


class StoryLLMResponse(BaseModel):
    title: str = Field(description='the title of the story')
    rootNode: StoryNodeLLM = Field(description='the root node of the story with its options')
