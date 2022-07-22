from typing import Any, List, Optional

from pydantic import BaseModel
from regression_model.processing.validation import SalesDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class SalesDataInputs(BaseModel):
    inputs: List[SalesDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                    }
                ]
            }
        }
