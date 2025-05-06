#!/usr/bin/env python3

"""
Task details:

Improve 12-log_stats.py by adding the top 10 of the most present IPs in the
collection nginx of the database logs:
    - The IPs top must be sorted (like the example below)
"""

from typing import Callable

from pymongo import MongoClient

display_log_stats: Callable = __import__("12-log_stats").display_log_stats


def display_ip_stats():
    """Displays the top 10 IPs in the nginx logs."""
    client = MongoClient()
    nginx = client.logs.nginx

    # Get the top 10 IPs
    ips = nginx.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
        ]
    )

    print("IPs:")
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")


if __name__ == "__main__":
    display_log_stats()
    display_ip_stats()
