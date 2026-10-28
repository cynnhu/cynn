"""示例 3：使用 StrOutputParser 将模型消息转换为字符串。"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_template("请用一句话解释：{topic}")
parser = StrOutputParser()

print("提示词模板：")
print(prompt.invoke({"topic": "Runnable"}).to_string())
print("\n解析器的作用：接收 AIMessage，并提取其中的文本内容。")
print(f"解析器类型：{type(parser).__name__}")
