from typing import Optional, Union, List, Dict, Tuple, Any
import pinecone
from pinecone import FetchResponse, SparseValues, QueryResponse, QueryVector, UpsertResponse, Vector
import time
from datetime import datetime
from gentrace.providers.step_run import StepRun
from gentrace.providers.pipeline import Pipeline
from gentrace.providers.pipeline_run import PipelineRun

class PineconePipelineHandler:
    pipeline: Optional[Pipeline] = None
    pipeline_run: Optional[PipelineRun] = None

    def __init__(self, pipeline = None):
        self.pipeline : Optional[Pipeline]  = pipeline

    def set_pipeline_run(self, pipeline_run):
        self.pipeline_run : Optional[PipelineRun] = pipeline_run
    
    class Index(pinecone.Index):
        def __init__(self, index_name: str, pool_threads=1, *args, **kwargs):
            super().__init__(index_name, pool_threads, *args, **kwargs)

        def fetch(self, ids: List[str], namespace: Optional[str] = None, **kwargs) -> FetchResponse:
            start_time = time.time()
            response = super().fetch(ids, namespace, **kwargs)
            end_time = time.time()
            elapsed_time = int((end_time - start_time) * 1000)

            self.pipeline_run.add_step_run(
                PineconeFetchStepRun(
                    elapsed_time,
                    datetime.fromtimestamp(start_time).isoformat(),
                    datetime.fromtimestamp(end_time).isoformat(),
                    {'ids': ids, 'namespace': namespace},
                    response
                )
            )

            return response

        def update(self, id: str, values: Optional[List[float]] = None, set_metadata: Optional[Dict[str,
                                           Union[str, float, int, bool, List[int], List[float], List[str]]]] = None,
               namespace: Optional[str] = None,
               sparse_values: Optional[Union[SparseValues, Dict[str, Union[List[float], List[int]]]]] = None,
               **kwargs) -> Dict[str, any]:
            start_time = time.time()
            response = super().update(values, set_metadata, namespace, sparse_values, **kwargs)
            end_time = time.time()
            elapsed_time = int((end_time - start_time) * 1000)

            self.pipeline_run.add_step_run(
                PineconeUpdateStepRun(
                    elapsed_time,
                    datetime.fromtimestamp(start_time).isoformat(),
                    datetime.fromtimestamp(end_time).isoformat(),
                    {'id': id, 'values': values, 'set_metadata': set_metadata, 'namespace': namespace, 'sparse_values': sparse_values},
                    response
                )
            )

            return response

        def query(self,
              vector: Optional[List[float]] = None,
              id: Optional[str] = None,
              queries: Optional[Union[List[QueryVector], List[Tuple]]] = None,
              top_k: Optional[int] = None,
              namespace: Optional[str] = None,
              filter: Optional[Dict[str, Union[str, float, int, bool, List, dict]]] = None,
              include_values: Optional[bool] = None,
              include_metadata: Optional[bool] = None,
              sparse_vector: Optional[Union[SparseValues, Dict[str, Union[List[float], List[int]]]]] = None,
              **kwargs) -> QueryResponse:
            bound_query = super().query
            start_time = time.time()
            response = bound_query(vector, id, queries, top_k, namespace, filter, include_values, 
                                   include_metadata, sparse_vector, **kwargs)
            end_time = time.time()
            elapsed_time = int((end_time - start_time) * 1000)

            inputs = {'vector': vector, 'id': id, 'queries': queries, 'namespace': namespace, 'include_values': include_values, 
                      'include_metadata': include_metadata, 'sparse_vector': sparse_vector}
            model_params = {'top_k': top_k, 'filter': filter}

            self.pipeline_run.add_step_run(
                PineconeQueryStepRun(
                    elapsed_time,
                    datetime.fromtimestamp(start_time).isoformat(),
                    datetime.fromtimestamp(end_time).isoformat(),
                    {**inputs},
                    {**model_params},
                    response
                )
            )

            return response
        
        def upsert(self,
               vectors: Union[List[Vector], List[tuple], List[dict]],
               namespace: Optional[str] = None,
               batch_size: Optional[int] = None,
               show_progress: bool = True,
               **kwargs) -> UpsertResponse:
            start_time = time.time()
            response = super().upsert(vectors, namespace, batch_size, show_progress, **kwargs)
            end_time = time.time()
            elapsed_time = int((end_time - start_time) * 1000)

            self.pipeline_run.add_step_run(
                PineconeUpsertStepRun(
                    elapsed_time,
                    datetime.fromtimestamp(start_time).isoformat(),
                    datetime.fromtimestamp(end_time).isoformat(),
                    {'vectors': vectors, 'namespace': namespace, 'batch_size': batch_size, 'show_progress': show_progress},
                    response
                )
            )

            return response

        def delete(self,
               ids: Optional[List[str]] = None,
               delete_all: Optional[bool] = None,
               namespace: Optional[str] = None,
               filter: Optional[Dict[str, Union[str, float, int, bool, List, dict]]] = None,
               **kwargs) -> Dict[str, Any]:
            start_time = time.time()
            response = super().delete(ids, delete_all, namespace, filter, **kwargs)
            end_time = time.time()
            elapsed_time = int((end_time - start_time) * 1000)

            self.pipeline_run.add_step_run(
                PineconeDeleteStepRun(
                    elapsed_time,
                    datetime.fromtimestamp(start_time).isoformat(),
                    datetime.fromtimestamp(end_time).isoformat(),
                    {'ids': ids, 'delete_all': delete_all, 'namespace': namespace, 'filter': filter},
                    response
                )
            )

            return response


class PineconeFetchStepRun(StepRun):
    def __init__(self, elapsed_time: int, start_time: str, end_time: str, inputs: dict, response: dict):
        super().__init__(
            'pinecone',
            'pinecone_indexFetch',
            elapsed_time,
            start_time,
            end_time,
            inputs,
            {},
            response
        )
        self.inputs = inputs
        self.response = response


class PineconeQueryStepRun(StepRun):
    def __init__(self, elapsed_time: int, start_time: str, end_time: str, inputs: dict, model_params: dict, response: dict):
        super().__init__(
            'pinecone',
            'pinecone_indexQuery',
            elapsed_time,
            start_time,
            end_time,
            inputs,
            model_params,
            response
        )
        self.inputs = inputs
        self.response = response


class PineconeUpdateStepRun(StepRun):
    def __init__(self, elapsed_time: int, start_time: str, end_time: str, inputs: dict, response: dict):
        super().__init__(
            'pinecone',
            'pinecone_indexUpdate',
            elapsed_time,
            start_time,
            end_time,
            inputs,
            {},
            response
        )
        self.inputs = inputs
        self.response = response


class PineconeUpsertStepRun(StepRun):
    def __init__(self, elapsed_time: int, start_time: str, end_time: str, inputs: dict, response: dict):
        super().__init__(
            'pinecone',
            'pinecone_indexUpsert',
            elapsed_time,
            start_time,
            end_time,
            inputs,
            {},
            response
        )
        self.inputs = inputs
        self.response = response


class PineconeDeleteStepRun(StepRun):
    def __init__(self, elapsed_time: int, start_time: str, end_time: str, inputs: dict, response: dict):
        super().__init__(
            'pinecone',
            'pinecone_indexDelete1',
            elapsed_time,
            start_time,
            end_time,
            inputs,
            {},
            response
        )
        self.inputs = inputs
        self.response = response
