from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_data_csv: str
    test_data_csv: str
