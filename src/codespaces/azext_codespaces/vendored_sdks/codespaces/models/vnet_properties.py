# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VnetProperties(Model):
    """Model representing Vnet Injection properties for Codespaces Plan.

    :param subnet_id: The ARM resource identifier of the virtual network
     subnet which the codespaces of the Codespaces Plan will join. This is of
     the form
     /subscriptions/{subscription}/resourceGroups/{group}/providers/{provider}/virtualNetworks/{network}/subnets/{subnet}.The
     virtual network must be in the same region and subscription as the
     Codespaces Plan.
    :type subnet_id: str
    """

    _attribute_map = {
        'subnet_id': {'key': 'subnetId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VnetProperties, self).__init__(**kwargs)
        self.subnet_id = kwargs.get('subnet_id', None)
