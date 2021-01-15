# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Privileges(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'list[Link]',
        'resources': 'list[str]'
    }

    attribute_map = {
        'links': 'links',
        'resources': 'resources'
    }

    def __init__(self, links=None, resources=None):  # noqa: E501
        """Privileges - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._resources = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if resources is not None:
            self.resources = resources

    @property
    def links(self):
        """Gets the links of this Privileges.  # noqa: E501


        :return: The links of this Privileges.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Privileges.


        :param links: The links of this Privileges.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def resources(self):
        """Gets the resources of this Privileges.  # noqa: E501


        :return: The resources of this Privileges.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Privileges.


        :param resources: The resources of this Privileges.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["all-permissions", "approve-vulnerability-exceptions", "assign-scan-engine", "assign-scan-template", "assign-ticket-assignee", "close-tickets", "configure-global-settings", "create-reports", "create-tickets", "delete-vulnerability-exceptions", "manage-advpolicies", "manage-asset-group-access", "manage-asset-group-assets", "manage-dynamic-asset-groups", "manage-policies", "manage-report-access", "manage-report-templates", "manage-scan-alerts", "manage-scan-engines", "manage-scan-templates", "manage-site-access", "manage-site-credentials", "manage-sites", "manage-static-asset-groups", "manage-tags", "manage-vuln-investigations", "purge-site-asset-data", "schedule-automatic-scans", "specify-scan-targets", "specify-site-metadata", "start-unscheduled-scans", "submit-vulnerability-exceptions", "use-restricted-report-sections", "view-asset-group-asset-data", "view-site-asset-data", "view-vuln-investigations" ]  # noqa: E501
        if not set(resources).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `resources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(resources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._resources = resources

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Privileges, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Privileges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
