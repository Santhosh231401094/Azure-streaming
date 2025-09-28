

# Real-Time IoT Data Pipeline with Azure and Databricks

This project demonstrates an **end-to-end streaming data pipeline** for real-time IoT analytics. It processes sensor data from a simulated Raspberry Pi using **Azure Databricks** and stores it efficiently in **Azure Data Lake Storage (ADLS) Gen2**, leveraging **Delta Lake optimizations** to address the *small file problem*.


## 🏗️ Architecture

The pipeline follows a sequential flow:

1. **Data Source** – Raspberry Pi web simulator generates IoT device data.
2. **Ingestion** – Azure IoT Hub securely ingests device messages.
3. **Processing** – Azure Databricks (Spark Structured Streaming) consumes and processes the real-time data stream.
4. **Storage** – Processed data is continuously written to **Delta Lake tables** in ADLS Gen2.



## 💻 Technology Stack

* **Cloud Provider**: Microsoft Azure
* **Ingestion**: Azure IoT Hub
* **Processing**: Azure Databricks (Apache Spark Structured Streaming)
* **Storage**: Azure Data Lake Storage Gen2 + Delta Lake



## ✨ Key Features

* **Real-Time Processing**: End-to-end low-latency pipeline.
* **Scalability**: Fully managed Azure services that scale with demand.
* **Efficient Storage**: Delta Lake’s **Optimize Write** and **Auto Compaction** features prevent small file issues and ensure fast queries.



## 🚀 Implementation Steps

### 1. Device Configuration

* Configure the Raspberry Pi simulator with a connection string.
* Send sensor data (e.g., `deviceId`, `temperature`, `humidity`) to Azure IoT Hub.

### 2. Data Ingestion

* IoT Hub receives the incoming device data.
* Provides a secure event streaming endpoint for downstream consumers.

### 3. Processing with Databricks

* Create a Databricks Notebook with Spark Structured Streaming.
* Define schema for JSON payloads.
* Parse, clean, and transform raw data into structured format.

### 4. Writing to Storage

* Write the transformed stream into ADLS Gen2 in **Delta format**.
* Configure **checkpointing** for fault tolerance.
* Enable Delta Lake optimizations (`optimizeWrite`, `autoCompact`).



## 🔧 Solving the Small File Problem

Streaming jobs typically create **thousands of small files**, leading to poor query performance. This project leverages **Delta Lake optimizations**:

* **Optimize Write** – Combines small files into optimally sized ones during ingestion.
* **Auto Compaction** – Runs in the background to merge leftover small files.

✅ Together, they ensure **high performance** and **healthy data lakes** without manual maintenance.



## 📂 Repository Structure

```
.
├── notebooks/                # Databricks notebooks for streaming logic
├── configs/                  # Connection configs (IoT Hub, ADLS paths, etc.)
├── README.md                 # Project documentation
```




