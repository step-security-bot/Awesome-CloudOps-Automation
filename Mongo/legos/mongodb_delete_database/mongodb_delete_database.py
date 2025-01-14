##
##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
import pprint
from pydantic import BaseModel, Field
from typing import List


class InputSchema(BaseModel):
    database_name: str = Field(
        title='Database Name',
        description='Name of the MongoDB database'
    )


def mongodb_delete_database_printer(output):
    if output is None:
        return
    print("\n\n")
    if isinstance(output, Exception):
        pprint.pprint("Error : {}".format(output))
        return output
    else:
        db_names_before_drop = output[0]
        db_names_after_drop = output[1]
        pprint.pprint("db count BEFORE drop:{}".format(len(db_names_before_drop)))
        pprint.pprint("db count AFTER drop:{}".format(len(db_names_after_drop)))

        diff = len(db_names_before_drop) - len(db_names_after_drop)
        if diff != 0:
            pprint.pprint("Database deleted successfully !!!")


def mongodb_delete_database(handle, database_name: str) -> List:
    """mongodb_delete_database delete database in mongodb.

        :type handle: object
        :param handle: Object returned from task.validate(...).

        :type database_name: str
        :param database_name: Name of the MongoDB database.

        :rtype: All the results of the query.
    """
    # Input param validation.

    try:
        db_names_before_drop = handle.list_database_names()

        handle.drop_database(database_name)
        # Verification
        db_names_after_drop = handle.list_database_names()
        return [db_names_before_drop, db_names_after_drop]
    except Exception as e:
        return [e]
