IOT_CS="my-connection-string"
ehConf={
    "eventhubs.connectionString":sc._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt(IOT_CS),
    "eventhubs.consumerGroup":"$Default"
}
eventhub_stream = (
    spark.readStream.format("eventhubs")
        .options(**ehConf)
        .load()
)
