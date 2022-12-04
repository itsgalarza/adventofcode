from itertools import chain
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import create_map, lit, col, when

from src.y22.d02.p1 import _read_input


wins = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

loses = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

ties = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

fixed_scoring = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

shape_scoring = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

def _scoring(df: DataFrame) -> DataFrame:
    result_score_mapping = create_map([lit(x) for x in chain(*fixed_scoring.items())])
    lose_mapping = create_map([lit(x) for x in chain(*loses.items())])
    win_mapping = create_map([lit(x) for x in chain(*wins.items())])
    tie_mapping = create_map([lit(x) for x in chain(*ties.items())])
    shape_mapping = create_map([lit(x) for x in chain(*shape_scoring.items())])

    shape_to_play_df = ( 
      df.withColumn("result_score", result_score_mapping[df["you"]])
        .withColumn("shape_to_play", when(col("you")=="X", lose_mapping[df["opponent"]]).when(col("you")=="Z", win_mapping[df["opponent"]]).otherwise(tie_mapping[df["opponent"]]))
    )

    final_scoring_df = (
        shape_to_play_df.withColumn("shape_score", shape_mapping[col("shape_to_play")])
                        .withColumn("final_score", col("shape_score")+col("result_score"))
    )


    return final_scoring_df

def solver(spark: SparkSession, data: str):
    input = _read_input(spark, data)
    return input.transform(_scoring).agg({"final_score":"sum"}).collect()[0][0]


