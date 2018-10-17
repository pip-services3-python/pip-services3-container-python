# -*- coding: utf-8 -*-
"""
    pip_services_container.build.DefaultContainerFactory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Default container factory implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_commons.refer import Descriptor
from pip_services_components.build import CompositeFactory
from pip_services_components.log import DefaultLoggerFactory
from pip_services_components.count import DefaultCountersFactory
from pip_services_components.config import DefaultConfigReaderFactory
from pip_services_components.cache import DefaultCacheFactory
from pip_services_components.auth import DefaultCredentialStoreFactory
from pip_services_components.connect import DefaultDiscoveryFactory
from pip_services_components.info._DefaultInfoFactory import DefaultInfoFactory

DefaultContainerFactoryDescriptor = Descriptor(
    "pip-services-container", "factory", "container", "default", "1.0"
)

class DefaultContainerFactory(CompositeFactory):

    def __init__(self):
        super(DefaultContainerFactory, self).__init__()
        self.add(DefaultInfoFactory())
        self.add(DefaultLoggerFactory())
        self.add(DefaultCountersFactory())
        self.add(DefaultConfigReaderFactory())
        self.add(DefaultCacheFactory())
        self.add(DefaultCredentialStoreFactory())
        self.add(DefaultDiscoveryFactory())

