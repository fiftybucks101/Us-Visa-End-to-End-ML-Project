from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_data_csv: str
    test_data_csv: str

@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str
