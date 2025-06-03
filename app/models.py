from sqlalchemy import Column, String, Float, Boolean, Text, JSON  
from db import Base

class CVE(Base):
    __tablename__ = "cves"

    cve_id                      = Column(String, primary_key=True)
    identifier                  = Column(String)
    published                   = Column(String)
    lastmodified                = Column(String)
    status                      = Column(String)
    description                 = Column(Text)
    severity                    = Column(String)
    base_score                  = Column(Float)
    vector_string               = Column(String)
    exploitability_score        = Column(Float)
    impact_score                = Column(Float)
    access_vector               = Column(String)
    attack_complexity           = Column(String)
    authentication              = Column(String)
    confidentiality_impact      = Column(String)
    integrity_impact            = Column(String)
    availability_impact         = Column(String)
    cpes                        = Column(JSON)
