##
##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
from pydantic import BaseModel, Field
from typing import List, Optional, Tuple
from unskript.legos.aws.aws_list_all_regions.aws_list_all_regions import aws_list_all_regions
from unskript.legos.aws.aws_get_s3_bucket_list.aws_get_s3_bucket_list import aws_get_s3_buckets
import pprint


class InputSchema(BaseModel):
    region: Optional[str] = Field(
    default="",
    title='Region',
    description='Name of the AWS Region'
    )
    
def aws_get_public_s3_buckets_printer(output):
    if output is None:
        return
    pprint.pprint(output)

def check_publicly_accessible_buckets(s3Client,b,permission):
    public_check = ["http://acs.amazonaws.com/groups/global/AuthenticatedUsers",
                   "http://acs.amazonaws.com/groups/global/AllUsers"]
    public_buckets = False
    try:
        res = s3Client.get_bucket_acl(Bucket=b)
        for perm in permission:
            for grant in res["Grants"]:
                if 'Permission' in grant.keys() and perm == grant["Permission"]:
                    if 'URI' in grant["Grantee"] and grant["Grantee"]["URI"] in public_check:
                        public_buckets = True
    except Exception as e:
        pass
    return public_buckets

def aws_get_public_s3_buckets(handle, region: str=None) -> Tuple:
    """aws_get_public_s3_buckets get list of public buckets.
        
        Note- Only READ and WRITE ACL Permission S3 buckets are chekced for public access. Other ACL Permissions are - "READ_ACP"|"WRITE_ACP"|"FULL_CONTROL"
        :type handle: object
        :param handle: Object returned from task.validate(...).

        :type region: string
        :param region: location of the bucket.
        
        :rtype: Tuple with the execution result and list of public S3 buckets with READ/WRITE ACL Permissions
    """
    permission = ["READ","WRITE"]
    result = []
    all_buckets = []
    all_regions = [region]
    if region is None or len(region)==0:
        all_regions = aws_list_all_regions(handle=handle)
    try:
        for r in all_regions:
            s3Client = handle.client('s3',region_name=r)
            output = aws_get_s3_buckets(handle=handle, region=r)
            if len(output)!= 0:
                for o in output:
                    all_buckets_dict = {}
                    all_buckets_dict["region"]=r
                    all_buckets_dict["bucket"]=o
                    all_buckets.append(all_buckets_dict)
    except Exception as e:
        pass
    for bucket in all_buckets:
        try:
            s3Client = handle.client('s3',region_name= bucket['region'])
            flag = check_publicly_accessible_buckets(s3Client,bucket['bucket'], permission)
            if flag:
                result.append(bucket)
        except Exception as e:
            pass
    execution_flag = False
    if len(result) > 0:
        execution_flag = True
    output = (execution_flag, result)
    return output