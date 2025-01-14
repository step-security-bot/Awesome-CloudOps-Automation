##
##  Copyright (c) 2023 unSkript, Inc
##  All rights reserved.
##
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, timedelta
import botocore.config
from unskript.connectors.aws import aws_get_paginator
import pprint


class InputSchema(BaseModel):
    time_period_in_days: int = Field(
        default=30,
        title="Threshold (in days)",
        description="(in days) The threshold to filter the unused log strams.")
    region: str = Field(
        title='Region',
        description='AWS Region')


def aws_filter_unused_log_streams_printer(output):
    if output is None:
        return

    pprint.pprint(output)


def aws_filter_unused_log_streams(handle, region: str, time_period_in_days: int = 30) -> List:
    """aws_filter_unused_log_streams Returns an array of unused log strams for all log groups.

        :type region: string
        :param region: Used to filter the volume for specific region.
        
        :type time_period_in_days: int
        :param time_period_in_days: (in days) The threshold to filter the unused log strams.

        :rtype: Array of unused log strams for all log groups.
    """
    result = []
    now = datetime.utcnow()
    try:
        start_time = now - timedelta(days=time_period_in_days)
        config = botocore.config.Config(retries={'max_attempts': 10})
        ec2Client = handle.client('logs', region_name=region, config=config)
        response = aws_get_paginator(ec2Client, "describe_log_groups", "logGroups")
        for log_group in response:
            log_group_name = log_group['logGroupName']
            response1 = aws_get_paginator(ec2Client, "describe_log_streams", "logStreams",
                                          logGroupName=log_group_name,
                                          orderBy='LastEventTime',
                                          descending=True)

            for log_stream in response1:
                unused_log_streams = {}
                last_event_time = log_stream.get('lastEventTimestamp')
                if last_event_time is None:
                    # The log stream has never logged an event
                    unused_log_streams["log_group_name"] = log_group_name
                    unused_log_streams["log_stream_name"] = log_stream['logStreamName']
                    result.append(unused_log_streams)
                elif datetime.fromtimestamp(last_event_time/1000.0) < start_time:
                    # The log stream has not logged an event in the past given days
                    unused_log_streams["log_group_name"] = log_group_name
                    unused_log_streams["log_stream_name"] = log_stream['logStreamName']
                    result.append(unused_log_streams)
    except Exception as e:
        result.append({"error": e})
        
    return result
