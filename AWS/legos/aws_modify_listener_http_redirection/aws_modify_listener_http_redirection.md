{
"action_title": "AWS Modify ALB Listeners HTTP Redirection",
"action_description": "AWS Modify ALB Listeners HTTP Redirection",
"action_type": "LEGO_TYPE_AWS",
"action_entry_function": "aws_modify_listener_for_http_redirection",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_LIST",
"action_supports_iteration": true,
"action_verbs": [
"modify"
],
"action_nouns": [
"listeners",
"loadbalancers"
]
}