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

    result = await openai.Completion.acreate(
        pipeline_slug="text-generation",
        model="text-davinci-003",
        prompt_template="Hello world {{ name }}",
        prompt_inputs={"name": "test"},
        stream=True,
    )

    pipeline_run_id = None
    async for value in result:
        if value.get("pipelineRunId"):
            pipeline_run_id = value.get("pipelineRunId")

    gentrace.flush()

    print("Result: ", pipeline_run_id)


asyncio.run(main())
