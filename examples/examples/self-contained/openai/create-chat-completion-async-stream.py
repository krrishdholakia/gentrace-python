import asyncio
import os

import gentrace
from dotenv import load_dotenv
from gentrace import providers

load_dotenv()


async def main():
    gentrace.api_key = os.getenv("GENTRACE_API_KEY")
    gentrace.host = "http://localhost:3000/api/v1"

    openai = providers.openai
    openai.api_key = os.getenv("OPENAI_KEY")

    result = await openai.ChatCompletion.acreate(
        pipeline_id="testing-chat-completion-value",
        messages=[{"role": "user", "content": "Hello!"}],
        model="gpt-3.5-turbo",
        stream=True,
    )

    pipeline_run_id = None
    async for value in result:
        if value.get("pipeline_run_id"):
            pipeline_run_id = value.get("pipeline_run_id")

    gentrace.flush()

    print("Result: ", pipeline_run_id)


asyncio.run(main())