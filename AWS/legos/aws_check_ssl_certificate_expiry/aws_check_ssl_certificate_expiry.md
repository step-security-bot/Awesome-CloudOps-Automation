{
    "action_title": "Check SSL Certificate Expiry",
    "action_description": "Check ACM SSL Certificate expiry date",
    "action_type": "LEGO_TYPE_AWS",
    "action_entry_function": "aws_check_ssl_certificate_expiry",
    "action_needs_credential": true,
    "action_output_type": "ACTION_OUTPUT_TYPE_INT",
    "action_supports_poll": true,
    "action_supports_iteration": true,
    "action_verbs": [
    "check",
    "expiry"
    ],
    "action_nouns": [
    "ssl",
    "aws"
    ]
  }