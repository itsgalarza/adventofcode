import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark_session():
    """Fixture for creating a spark session."""
    delta_version = "2.0.0"  # compatible with pyspark 3.2 (see: https://docs.delta.io/latest/releases.html)
    session = (
        SparkSession.builder.master("local[*]")
        .appName("pytest-pyspark-local-testing")
        .config("spark.jars.packages", f"io.delta:delta-core_2.12:{delta_version}")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.session.timeZone", "UTC")
        .config("spark.driver.host", "localhost")
        .getOrCreate()
    )
    yield session
