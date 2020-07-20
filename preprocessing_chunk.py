from nlprecsysutility import RecSysUtility
from config import PreproDatasetConfig

utility = RecSysUtility(PreproDatasetConfig._test_file)
utility.create_chunk_csv(output_dir=PreproDatasetConfig._output_dir, chunk_size = PreproDatasetConfig._chunk_size)
