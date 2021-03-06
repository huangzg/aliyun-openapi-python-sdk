# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkalidns.endpoint import endpoint_data

class AddGtmAccessStrategyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Alidns', '2015-01-09', 'AddGtmAccessStrategy','alidns')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DefaultAddrPoolId(self):
		return self.get_query_params().get('DefaultAddrPoolId')

	def set_DefaultAddrPoolId(self,DefaultAddrPoolId):
		self.add_query_param('DefaultAddrPoolId',DefaultAddrPoolId)

	def get_FailoverAddrPoolId(self):
		return self.get_query_params().get('FailoverAddrPoolId')

	def set_FailoverAddrPoolId(self,FailoverAddrPoolId):
		self.add_query_param('FailoverAddrPoolId',FailoverAddrPoolId)

	def get_StrategyName(self):
		return self.get_query_params().get('StrategyName')

	def set_StrategyName(self,StrategyName):
		self.add_query_param('StrategyName',StrategyName)

	def get_AccessLines(self):
		return self.get_query_params().get('AccessLines')

	def set_AccessLines(self,AccessLines):
		self.add_query_param('AccessLines',AccessLines)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)