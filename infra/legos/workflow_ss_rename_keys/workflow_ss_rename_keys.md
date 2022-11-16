{
"action_title": "Infra: Rename keys in workflow state store",
"action_description": "Infra: use this action to rename keys in a state store provided by the workflow.",
"action_type": "LEGO_TYPE_INFRA",
"action_entry_function": "workflow_ss_rename_keys",
"action_needs_credential": false,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_BOOL",
"action_supports_iteration": true,
"action_verbs": [
"persist",
"store",
"rename"
],
"action_nouns": [
"keys"
]
}