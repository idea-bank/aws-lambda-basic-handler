"""
    :module_name: function
    :module_summary: {{cookiecutter.service_description}}
    :module_author: {{cookiecutter.service_author}}
"""

import sys
import json

def handler(event, context):
    """A simple function that returns system/event/context info with CORS headers"""
    return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*'
            },
            'body': json.dumps({
                'sysinfo': sys.version,
                'event': event,
                'context': str(context)
            })
        }

