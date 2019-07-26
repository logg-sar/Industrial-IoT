# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BrowsePathRequestApiModel(Model):
    """Browse nodes by path.

    :param node_id: Node to browse from.
     (default: RootFolder).
    :type node_id: str
    :param browse_paths: The paths to browse from node.
     (mandatory)
    :type browse_paths: list[list[str]]
    :param read_variable_values: Whether to read variable values on target
     nodes.
     (default is false). Default value: False .
    :type read_variable_values: bool
    :param header: Optional request header
    :type header: ~azure-iiot-opc-twin.models.RequestHeaderApiModel
    """

    _validation = {
        'browse_paths': {'required': True},
    }

    _attribute_map = {
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'browse_paths': {'key': 'browsePaths', 'type': '[[str]]'},
        'read_variable_values': {'key': 'readVariableValues', 'type': 'bool'},
        'header': {'key': 'header', 'type': 'RequestHeaderApiModel'},
    }

    def __init__(self, browse_paths, node_id=None, read_variable_values=False, header=None):
        super(BrowsePathRequestApiModel, self).__init__()
        self.node_id = node_id
        self.browse_paths = browse_paths
        self.read_variable_values = read_variable_values
        self.header = header