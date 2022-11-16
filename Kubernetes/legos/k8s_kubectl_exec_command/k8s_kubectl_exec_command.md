{
"action_title": "Kubectl execute command",
"action_description": "Kubectl execute command in a given pod",
"action_type": "LEGO_TYPE_K8S",
"action_entry_function": "k8s_kubectl_exec_command",
"action_needs_credential": true,
"action_supports_poll": true,
"action_supports_iteration": true,
"action_output_type": "ACTION_OUTPUT_TYPE_STR",
"action_verbs": [
"execute"
],
"action_nouns": [
"command", 
"pod"
]
}