"""示例 1：使用 ChatPromptTemplate 生成结构化提示词。"""

from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一名耐心的 Python 教师。"),
        ("human", "请用三个要点解释什么是 {topic}，面向 {audience}。"),
    ]
)

messages = prompt.invoke({"topic": "LangChain", "audience": "初学者"})

for message in messages.messages:
    print(f"[{message.type}] {message.content}")
