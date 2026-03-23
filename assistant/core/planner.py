from core.llm import ask_llm

TOOLS = [
"search_web",
"open_browser"
]

def plan_task(user_input):

    prompt = f"""
You are a local system assistant.

Available tools:
search_web(query)
open_browser(url)
read_emails()

Return only the tool command.

User request:
{user_input}
"""

    response = ask_llm(prompt)

    return response.strip()