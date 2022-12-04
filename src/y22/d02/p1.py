from itertools import chain
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import create_map, lit, col, when


INPUT_DATA = "src/y22/d02/inputs/input.txt"

CSV_SCHEMA = StructType(
    [
        StructField("opponent", StringType(), False),
        StructField("you", StringType(), False),
    ]
)

def _scoring(df: DataFrame) -> DataFrame:
    scoring = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }
    mapping_expr = create_map([lit(x) for x in chain(*scoring.items())])
    return (
            df
            .withColumn("shape_score", mapping_expr[df["you"]])
            .withColumn("opponents_shape_score", mapping_expr[df["opponent"]])
            .withColumn("tmp_calc", (((col("shape_score")-col("opponents_shape_score"))+lit(1))%lit(3))*lit(3))
            .withColumn("result_score", when(col("tmp_calc")==lit(-3), lit(6)).otherwise(col("tmp_calc")))
            .withColumn("final_score", col("result_score")+col("shape_score"))
    )

def _read_input(spark: SparkSession, data: str): 
    input: DataFrame = spark.read.format("csv").schema(CSV_SCHEMA).option("sep"," ").load(data)
    return input 

def solver(spark: SparkSession, data: str):
    input = _read_input(spark, data)
    return input.transform(_scoring).agg({"final_score": "sum"}).collect()[0][0]


