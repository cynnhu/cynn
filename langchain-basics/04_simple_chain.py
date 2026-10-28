"""示例 4：组合提示词、模型和输出解析器。

运行前请复制 .env.example 为 .env，并设置 OPENAI_API_KEY。
"""

import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("请先在 .env 中设置 OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一名简洁的技术导师。"),
        ("human", "用不超过两句话解释 {concept}。"),
    ]
)
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)
parser = StrOutputParser()

chain = prompt | model | parser
answer = chain.invoke({"concept": "LangChain Runnable"})
print(answer)
