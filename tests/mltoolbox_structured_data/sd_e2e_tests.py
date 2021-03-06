# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
"""Test the structured data package e2e locally.
"""
from __future__ import absolute_import
from __future__ import print_function

import logging
import os
import six
import sys
import unittest

# Set up the path so that we can import local packages.
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__),
                    '../../solutionbox/structured_data/')))

import test_mltoolbox.test_datalab_e2e as e2e  # noqa


@unittest.skipIf(not six.PY2, 'Python 2 is required')
class TestLinearRegression(e2e.TestLinearRegression):
  """Test linear regression works e2e locally.
  """
  def __init__(self, *args, **kwargs):
    super(TestLinearRegression, self).__init__(*args, **kwargs)

    # Don't print debugging info
    self._logger.setLevel(logging.INFO)
