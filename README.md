

# Real-Time IoT Data Pipeline with Azure and Databricks Structured Streaming

This project demonstrates an **end-to-end streaming data pipeline** for real-time IoT analytics. It processes sensor data from a simulated Raspberry Pi using **Azure Databricks** and stores it efficiently in **Azure Data Lake Storage (ADLS) Gen2**, leveraging **Delta Lake optimizations** to address the *small file problem*.


## 🏗️ Architecture

<img width="1791" height="480" alt="MYDEPROIJ drawio (1)" src="https://github.com/user-attachments/assets/805e388c-f80f-4806-88f4-646b0bd86992" />


The pipeline follows a sequential flow:

1. **Data Source** – Raspberry Pi web simulator generates IoT device data.
2. **Ingestion** – Azure IoT Hub securely ingests device messages.
3. **Processing** – Azure Databricks (Spark Structured Streaming) consumes and processes the real-time data stream.
4. **Storage** – Processed data is continuously written to **Delta Lake tables** in ADLS Gen2.



## 💻 Technology Stack
<img width="1919" height="876" alt="Screenshot 2025-09-28 181011" src="https://github.com/user-attachments/assets/61c004f4-e478-4ed4-b7c4-dc6eb7bf59ff" />


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
<img width="1919" height="927" alt="Screenshot 2025-09-28 180435" src="https://github.com/user-attachments/assets/d1c92f70-17a3-4051-99ec-17db1ec89ad2" />

* Configure the Raspberry Pi simulator with a connection string.
* Send sensor data (e.g., `deviceId`, `temperature`, `humidity`) to Azure IoT Hub.

### 2. Data Ingestion
<img width="1919" height="912" alt="Screenshot 2025-09-28 180621" src="https://github.com/user-attachments/assets/53995d0a-cabe-4263-818a-9fe7d81f3246" />

* IoT Hub receives the incoming device data.
* Provides a secure event streaming endpoint for downstream consumers.

### 3. Processing with Databricks
<img width="1919" height="927" alt="Screenshot 2025-09-28 174413" src="https://github.com/user-attachments/assets/4e4cf1de-a014-44d1-8c8d-dd3e22b44a22" />

* Create a Databricks Notebook with Spark Structured Streaming.
* Define schema for JSON payloads.
* Parse, clean, and transform raw data into structured format.

### 4. Writing to Storage
<img width="1919" height="913" alt="Screenshot 2025-09-28 180529" src="https://github.com/user-attachments/assets/9be992ca-a609-4f2e-ab2d-df30e91134f7" />

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

## 📊 Cost Analysis
<img width="1420" height="980" alt="costanalysis_charts (3)" src="https://github.com/user-attachments/assets/216279ae-652b-40ff-a7c1-19a345043486" />



