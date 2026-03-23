from core.planner import plan_task
from core.executor import execute

print("AI Assistant started")

while True:

    user = input("\n>> ")

    plan = plan_task(user)

    print("PLAN:", plan)

    result = execute(plan)

    print("RESULT:", result)