"""
ZeroTier specific JSON-Schema definition
"""

from copy import deepcopy

from ...schema import schema as default_schema

base_zerotier_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": True,
    "properties": {
        "zerotier": {
            "type": "array",
            "title": "ZeroTier",
            "uniqueItems": True,
            "additionalItems": True,
            "propertyOrder": 12,
            "items": {
                "type": "object",
                "title": "Wireguard tunnel",
                "additionalProperties": True,
                "required": ["name", "id", "enabled"],
                "properties": {
                    "name": {
                        "title": "network name",
                        "description": "Zerotier Network name",
                        "type": "string",
                        "propertyOrder": 1,
                    },
                    "id": {
                        "title": "network id",
                        "description": "Zerotier Network ID",
                        "type": "string",
                        "minLength": 16,
                        "maxLength": 16,
                        "propertyOrder": 1,
                    },
                    "enabled": {
                        "title": "enabled",
                        "type": "boolean",
                        "description": "Whether or not the network is enabled.",
                    },
                },
            },
        }
    },
}

schema = deepcopy(base_zerotier_schema)
schema['properties']['files'] = default_schema['properties']['files']
