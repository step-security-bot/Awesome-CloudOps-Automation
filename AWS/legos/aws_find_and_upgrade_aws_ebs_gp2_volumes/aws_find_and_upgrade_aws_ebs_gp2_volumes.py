# Copyright (c) 2023 unSkript, Inc
# All rights reserved.
##
from pydantic import BaseModel, Field
from typing import Optional, Tuple
from unskript.legos.aws.aws_list_all_regions.aws_list_all_regions import aws_list_all_regions
import pprint

class InputSchema(BaseModel):
    region: Optional[str] = Field(
    default="",
    title='Region',
    description='Name of the AWS Region'
    )

def aws_find_and_upgrade_aws_ebs_gp2_volumes_printer(output):
    if output in None:
        return 
    pprint.pprint(output)


def aws_find_and_upgrade_aws_ebs_gp2_volumes(handle, region: str = None) -> Tuple:
    if region is None or len(region) == 0:
        all_regions = aws_list_all_regions(handle=handle)
    try:
        for r in all_regions:
            # Place holder for implementation to find out the ebs volumes to upgrade
            pass
    except Exception as e:
        raise e

    return (True, None)