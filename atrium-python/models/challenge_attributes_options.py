# coding: utf-8

"""
    MX API

    The MX Atrium API supports over 48,000 data connections to thousands of financial institutions. It provides secure access to your users' accounts and transactions with industry-leading cleansing, categorization, and classification.  Atrium is designed according to resource-oriented REST architecture and responds with JSON bodies and HTTP response codes.  Use Atrium's development environment, vestibule.mx.com, to quickly get up and running. The development environment limits are 100 users, 25 members per user, and access to the top 15 institutions. Contact MX to purchase production access.   # noqa: E501
"""


import pprint
import re  # noqa: F401

import six


class ChallengeAttributesOptions(object):


    """
    Attributes:
      mx_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    mx_types = {
        'image_data': 'str',
        'label': 'str',
        'value': 'str'
    }

    attribute_map = {
        'image_data': 'image_data',
        'label': 'label',
        'value': 'value'
    }

    def __init__(self, image_data=None, label=None, value=None):  # noqa: E501
        """ChallengeAttributesOptions - a model defined in Swagger"""  # noqa: E501

        self._image_data = None
        self._label = None
        self._value = None
        self.discriminator = None

        if image_data is not None:
            self.image_data = image_data
        if label is not None:
            self.label = label
        if value is not None:
            self.value = value

    @property
    def image_data(self):
        """Gets the image_data of this ChallengeAttributesOptions.  # noqa: E501


        :return: The image_data of this ChallengeAttributesOptions.  # noqa: E501
        :rtype: str
        """
        return self._image_data

    @image_data.setter
    def image_data(self, image_data):
        """Sets the image_data of this ChallengeAttributesOptions.


        :param image_data: The image_data of this ChallengeAttributesOptions.  # noqa: E501
        :type: str
        """

        self._image_data = image_data

    @property
    def label(self):
        """Gets the label of this ChallengeAttributesOptions.  # noqa: E501


        :return: The label of this ChallengeAttributesOptions.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ChallengeAttributesOptions.


        :param label: The label of this ChallengeAttributesOptions.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def value(self):
        """Gets the value of this ChallengeAttributesOptions.  # noqa: E501


        :return: The value of this ChallengeAttributesOptions.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ChallengeAttributesOptions.


        :param value: The value of this ChallengeAttributesOptions.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.mx_types):
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
        if issubclass(ChallengeAttributesOptions, dict):
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
        if not isinstance(other, ChallengeAttributesOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
