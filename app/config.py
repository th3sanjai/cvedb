from pathlib import Path
from appdirs import user_config_dir

class Config:
    def __init__(self, app_name: str = "CVEDB"):
        self.app_name = app_name
        if not self.app_name:
            raise ValueError("App name is required")
        self._ensure_config_dir_exists()
        self._ensure_config_files_exist()
        
    @property
    def config_dir(self) -> Path:
        return Path(user_config_dir(self.app_name))

    def config_db_path(self) -> Path:
        return self.config_dir / "cve.db"
    
    def _ensure_config_dir_exists(self) -> None:
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
    def _ensure_config_files_exist(self) -> None:
        db_path = self.config_db_path()
        if not db_path.exists():
            db_path.touch()
