{
"action_title": "Get Status for given DAG",
"action_description": "Get Status for given DAG",
"action_type": "LEGO_TYPE_AIRFLOW",
"action_entry_function": "airflow_check_dag_status",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_DICT",
"action_supports_iteration": true,
"action_verbs": [
"get"
],
"action_nouns": [
"dag",
"status"
]
}