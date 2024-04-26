def measure_performance(interface_monitor_output):
    total_latency = 0
    total_bytes_transferred = 0
    total_transactions = 0

    for entry in interface_monitor_output:
        timestamp, txn_type, data = entry

        if txn_type == "Rd":
            next_entry = interface_monitor_output[total_transactions + 1]
            next_timestamp, next_txn_type, next_data = next_entry
            latency = next_timestamp - timestamp
            total_latency += latency
            total_bytes_transferred += 32
        elif txn_type == "Wr":
            total_bytes_transferred += 32

            total_transactions += 1

            average_latency = total_latency / total_transactions
            bandwidth = total_bytes_transferred / total_transactions

    return average_latency, bandwidth