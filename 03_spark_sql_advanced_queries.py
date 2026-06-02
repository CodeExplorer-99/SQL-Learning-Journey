# ---------------------------------------------
# ✅ PySpark Setup
# ---------------------------------------------
import sys
import os
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

# Set environment paths
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['JAVA_HOME'] = r'C:\Users\ADMIN\.jdks\ms-17.0.15'

# Configure Spark
conf = SparkConf() \
    .setAppName("Spark_SQL_Learning") \
    .setMaster("local[*]") \
    .set("spark.default.parallelism", "1")

sc = SparkContext(conf=conf)
spark = SparkSession(sc)

# ---------------------------------------------
# ✅ Sample Data Creation
# ---------------------------------------------
data = [
    (0, "06-26-2011", 300.4, "Exercise", "GymnasticsPro", "cash"),
    (1, "05-26-2011", 200.0, "Exercise Band", "Weightlifting", "credit"),
    (2, "06-01-2011", 300.4, "Exercise", "Gymnastics Pro", "cash"),
    (3, "06-05-2011", 100.0, "Gymnastics", "Rings", "credit"),
    (4, "12-17-2011", 300.0, "Team Sports", "Field", "cash"),
    (5, "02-14-2011", 200.0, "Gymnastics", None, "cash")
]

df = spark.createDataFrame(data,
    ["id", "tdate", "amount", "category", "product", "spendby"]
)

df.createOrReplaceTempView("df")

# ---------------------------------------------
# ✅ Filtering Examples
# ---------------------------------------------
spark.sql("SELECT * FROM df WHERE category = 'Exercise'").show()
spark.sql("SELECT * FROM df WHERE category IN ('Exercise', 'Gymnastics')").show()
spark.sql("SELECT * FROM df WHERE product LIKE '%Gymnastics%'").show()
spark.sql("SELECT * FROM df WHERE product IS NULL").show()

# ---------------------------------------------
# ✅ Aggregations
# ---------------------------------------------
spark.sql("SELECT MAX(id) AS max_id FROM df").show()
spark.sql("SELECT MIN(id) AS min_id FROM df").show()
spark.sql("SELECT COUNT(*) FROM df").show()

# ---------------------------------------------
# ✅ CASE WHEN
# ---------------------------------------------
spark.sql("""
    SELECT *,
           CASE WHEN spendby = 'cash' THEN 1 ELSE 0 END AS is_cash
    FROM df
""").show()

# ---------------------------------------------
# ✅ String Functions
# ---------------------------------------------
spark.sql("SELECT id, CONCAT(id, '-', category) AS concat_val FROM df").show()
spark.sql("SELECT category, LOWER(category), UPPER(category) FROM df").show()
spark.sql("SELECT product, COALESCE(product, 'NA') FROM df").show()

# ---------------------------------------------
# ✅ Numeric Functions
# ---------------------------------------------
spark.sql("SELECT amount, CEIL(amount), ROUND(amount) FROM df").show()

# ---------------------------------------------
# ✅ Data Cleaning
# ---------------------------------------------
spark.sql("SELECT TRIM(product) FROM df").show()

# ---------------------------------------------
# ✅ Distinct & Substring
# ---------------------------------------------
spark.sql("SELECT DISTINCT category FROM df").show()
spark.sql("SELECT SUBSTRING(product, 1, 10) FROM df").show()

# ---------------------------------------------
# ✅ Group By + Aggregation
# ---------------------------------------------
spark.sql("""
    SELECT category, SUM(amount) AS total_amount
    FROM df
    GROUP BY category
""").show()

# ---------------------------------------------
# ✅ Window Functions
# ---------------------------------------------
spark.sql("""
    SELECT category,
           amount,
           ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) AS row_num,
           DENSE_RANK() OVER (PARTITION BY category ORDER BY amount DESC) AS rank
    FROM df
""").show()

# ---------------------------------------------
# ✅ HAVING Clause
# ---------------------------------------------
spark.sql("""
    SELECT category, COUNT(*) AS cnt
    FROM df
    GROUP BY category
    HAVING COUNT(*) > 1
""").show()
