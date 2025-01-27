import asyncio
import os

import gentrace
import openai
from dotenv import load_dotenv

load_dotenv()


async def main():
    gentrace.init(
        api_key=os.getenv("GENTRACE_API_KEY"),
        host="http://localhost:3000/api/v1",
    )

    gentrace.configure_openai()

    openai.api_key = os.getenv("OPENAI_KEY")

    result = await openai.ChatCompletion.acreate(
        pipeline_slug="testing-chat-completion-value",
        messages=[
            {
                "role": "user",
                "content": "Hello, I'm testing the acreate() async completion!",
            }
        ],
        model="gpt-3.5-turbo",
        stream=True,
    )

    pipeline_run_id = None
    async for value in result:
        if value.get("pipelineRunId"):
            pipeline_run_id = value.get("pipelineRunId")

    gentrace.flush()

    print("Result: ", pipeline_run_id)


asyncio.run(main())
