from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class CVESchema(BaseModel):
    cve_id: str
    identifier: Optional[str] = None
    published: Optional[str]
    lastmodified: Optional[str]
    status: Optional[str]
    description: str
    severity: Optional[str]
    base_score: Optional[float]
    vector_string: Optional[str]
    exploitability_score: Optional[float]
    impact_score: Optional[float]
    access_vector: Optional[str]
    attack_complexity: Optional[str]
    authentication: Optional[str]
    confidentiality_impact: Optional[str]
    integrity_impact: Optional[str]
    availability_impact: Optional[str]
    cpes: Optional[List[Dict[str, Any]]]

    class Config:
        from_attributes = True
