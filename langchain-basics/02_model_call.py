"""示例 2：调用聊天模型。

运行前请复制 .env.example 为 .env，并设置 OPENAI_API_KEY。
"""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("请先在 .env 中设置 OPENAI_API_KEY")

model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)

response = model.invoke("用一句话介绍 LangChain。")
print(response.content)
