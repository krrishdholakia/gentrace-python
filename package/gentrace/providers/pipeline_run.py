import copy
import json
from typing import Dict, List
from gentrace.api import IngestionApi
from gentrace.providers.step_run import StepRun

class PipelineRun:
    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.step_runs : List[StepRun] = []

    def get_pipeline(self):
        return self.pipeline

    def get_openai(self):
        if "openai" in self.pipeline.pipeline_handlers:
            handler = self.pipeline.pipeline_handlers.get("openai")
            cloned_handler = copy.deepcopy(handler)
            import openai.api_resources as api
            from .llms.openai import intercept_chat_completion, intercept_completion, intercept_embedding
            for name, cls in vars(api).items():
                if isinstance(cls, type):
                    # Create new class that inherits from the original class, don't directly monkey patch 
                    # the original class
                    new_class = type(name, (cls,), {})
                    if name == 'Completion':
                      new_class.create = intercept_completion(new_class.create)
                    elif name == 'ChatCompletion':
                      new_class.create = intercept_chat_completion(new_class.create)
                    elif name == 'Embedding':
                      new_class.create = intercept_embedding(new_class.create)
                      
                    new_class.pipeline_run = self

                    setattr(cloned_handler, name, new_class)

                    # TODO: Must work on a acreate() method, check that streaming works

            cloned_handler.set_pipeline_run(self)
            return cloned_handler
        else:
            raise ValueError("Did not find OpenAI handler. Did you call setup() on the pipeline?")

    def get_pinecone(self):
        if "pinecone" in self.pipeline.pipeline_handlers:
            handler = self.pipeline.pipeline_handlers.get("pinecone")
            cloned_handler = copy.deepcopy(handler)
            cloned_handler.set_pipeline_run(self)
            return cloned_handler
        else:
            raise ValueError("Did not find Pinecone handler. Did you call setup() on the pipeline?")

    def add_step_run(self, step_run: StepRun):
        self.step_runs.append(step_run)

    def submit(self) -> Dict:
        ingestion_api = IngestionApi(self.pipeline.config)
        
        print("Submitting pipeline run: ", [step_run.inputs for step_run in self.step_runs])

        step_runs_data = [
            {
                "provider": {
                    "name": step_run.provider,
                    "invocation": step_run.invocation,
                    "modelParams": step_run.model_params,
                    "inputs": step_run.inputs,
                    "outputs": step_run.outputs,
                },
                "elapsedTime": step_run.elapsed_time,
                "startTime": step_run.start_time,
                "endTime": step_run.end_time,
            }
            for step_run in self.step_runs
        ]

        pipeline_post_response = ingestion_api.pipeline_run_post(
            {
                "name": self.pipeline.id,
                "stepRuns": step_runs_data
            }
        )

        return pipeline_post_response.data
