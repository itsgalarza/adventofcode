from pyspark.sql import SparkSession
from src.y22.d02 import p1, p2


INPUT_DATA = "src/y22/d02/inputs/input.csv"

def init_spark() -> SparkSession:
    spark = (
        SparkSession.builder.config("spark.sql.session.timeZone", "UTC")
        .config("spark.databricks.delta.optimizeWrite.enabled", "true")
        .config("spark.databricks.delta.autoCompact.enabled", "true")
        .config("spark.databricks.delta.schema.autoMerge.enabled", "true")
        .config("spark.databricks.delta.overwriteSchema.enabled", "true")
        .config("spark.sql.sources.partitionOverwriteMode", "dynamic")
        .getOrCreate()
    )
    return spark


if __name__=="__main__":
    ss = init_spark()

    hypothetical_scoring = p1.solver(ss, INPUT_DATA)
    print(f"Guessing our hypothesis is right, we'll be scoring {hypothetical_scoring} points")

    final_scoring = p2.solver(ss, INPUT_DATA)
    print(f"Following the given rules, we'd score: {final_scoring}")

