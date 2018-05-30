# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Accesses the google.cloud.dataproc.v1beta2 WorkflowTemplateService API."""

import functools
import pkg_resources

import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.grpc_helpers
import google.api_core.operation
import google.api_core.operations_v1
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from mrjob._vendor.dataproc_v1beta2.gapic import enums
from mrjob._vendor.dataproc_v1beta2.gapic import workflow_template_service_client_config
from mrjob._vendor.dataproc_v1beta2.proto import clusters_pb2
from mrjob._vendor.dataproc_v1beta2.proto import clusters_pb2_grpc
from mrjob._vendor.dataproc_v1beta2.proto import jobs_pb2
from mrjob._vendor.dataproc_v1beta2.proto import jobs_pb2_grpc
from mrjob._vendor.dataproc_v1beta2.proto import operations_pb2 as proto_operations_pb2
from mrjob._vendor.dataproc_v1beta2.proto import workflow_templates_pb2
from mrjob._vendor.dataproc_v1beta2.proto import workflow_templates_pb2_grpc
from google.longrunning import operations_pb2 as longrunning_operations_pb2
from google.protobuf import duration_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2

_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-cloud-dataproc', ).version


class WorkflowTemplateServiceClient(object):
    """
    The API interface for managing Workflow Templates in the
    Cloud Dataproc API.
    """

    SERVICE_ADDRESS = 'dataproc.googleapis.com:443'
    """The default address of the service."""

    # The scopes needed to make gRPC calls to all of the methods defined in
    # this service
    _DEFAULT_SCOPES = ('https://www.googleapis.com/auth/cloud-platform', )

    # The name of the interface for this client. This is the key used to find
    # method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.cloud.dataproc.v1beta2.WorkflowTemplateService'

    @classmethod
    def region_path(cls, project, region):
        """Return a fully-qualified region string."""
        return google.api_core.path_template.expand(
            'projects/{project}/regions/{region}',
            project=project,
            region=region,
        )

    @classmethod
    def workflow_template_path(cls, project, region, workflow_template):
        """Return a fully-qualified workflow_template string."""
        return google.api_core.path_template.expand(
            'projects/{project}/regions/{region}/workflowTemplates/{workflow_template}',
            project=project,
            region=region,
            workflow_template=workflow_template,
        )

    def __init__(self,
                 channel=None,
                 credentials=None,
                 client_config=workflow_template_service_client_config.config,
                 client_info=None):
        """Constructor.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            client_config (dict): A dictionary of call options for each
                method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                'The `channel` and `credentials` arguments to {} are mutually '
                'exclusive.'.format(self.__class__.__name__), )

        # Create the channel.
        self.channel = channel
        if self.channel is None:
            self.channel = google.api_core.grpc_helpers.create_channel(
                self.SERVICE_ADDRESS,
                credentials=credentials,
                scopes=self._DEFAULT_SCOPES,
            )

        # Create the gRPC stubs.
        self._workflow_template_service_stub = (
            workflow_templates_pb2_grpc.WorkflowTemplateServiceStub(
                self.channel))

        # Operations client for methods that return long-running operations
        # futures.
        self._operations_client = (
            google.api_core.operations_v1.OperationsClient(self.channel))

        if client_info is None:
            client_info = (
                google.api_core.gapic_v1.client_info.DEFAULT_CLIENT_INFO)
        client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME], )

        self._inner_api_calls = {}

    def _intercept_channel(self, *interceptors):
        """ Experimental. Bind gRPC interceptors to the gRPC channel.

        Args:
            interceptors (*Union[grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamingClientInterceptor, grpc.StreamingUnaryClientInterceptor, grpc.StreamingStreamingClientInterceptor]):
              Zero or more gRPC interceptors. Interceptors are given control in the order
              they are listed.
        Raises:
            TypeError: If interceptor does not derive from any of
              UnaryUnaryClientInterceptor,
              UnaryStreamClientInterceptor,
              StreamUnaryClientInterceptor, or
              StreamStreamClientInterceptor.
        """
        self.channel = grpc.intercept_channel(self.channel, *interceptors)
        self._workflow_template_service_stub = (
            workflow_templates_pb2_grpc.WorkflowTemplateServiceStub(
                self.channel))
        # Operations client for methods that return long-running operations
        # futures.
        self._operations_client = (
            google.api_core.operations_v1.OperationsClient(self.channel))
        self._inner_api_calls.clear()

    # Service calls
    def create_workflow_template(
            self,
            parent,
            template,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates new workflow template.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> parent = client.region_path('[PROJECT]', '[REGION]')
            >>>
            >>> # TODO: Initialize ``template``:
            >>> template = {}
            >>>
            >>> response = client.create_workflow_template(parent, template)

        Args:
            parent (str): Required. The \"resource name\" of the region, as described
                in https://cloud.google.com/apis/design/resource_names of the form
                ``projects/{project_id}/regions/{region}``
            template (Union[dict, ~mrjob._vendor.dataproc_v1beta2.types.WorkflowTemplate]): Required. The Dataproc workflow template to create.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~mrjob._vendor.dataproc_v1beta2.types.WorkflowTemplate`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~mrjob._vendor.dataproc_v1beta2.types.WorkflowTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if 'create_workflow_template' not in self._inner_api_calls:
            self._inner_api_calls[
                'create_workflow_template'] = google.api_core.gapic_v1.method.wrap_method(
                    self._workflow_template_service_stub.
                    CreateWorkflowTemplate,
                    default_retry=self._method_configs[
                        'CreateWorkflowTemplate'].retry,
                    default_timeout=self._method_configs[
                        'CreateWorkflowTemplate'].timeout,
                    client_info=self._client_info,
                )

        request = workflow_templates_pb2.CreateWorkflowTemplateRequest(
            parent=parent,
            template=template,
        )
        return self._inner_api_calls['create_workflow_template'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def get_workflow_template(self,
                              name,
                              version=None,
                              retry=google.api_core.gapic_v1.method.DEFAULT,
                              timeout=google.api_core.gapic_v1.method.DEFAULT,
                              metadata=None):
        """
        Retrieves the latest workflow template.

        Can retrieve previously instantiated template by specifying optional
        version parameter.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> name = client.workflow_template_path('[PROJECT]', '[REGION]', '[WORKFLOW_TEMPLATE]')
            >>>
            >>> response = client.get_workflow_template(name)

        Args:
            name (str): Required. The \"resource name\" of the workflow template, as described
                in https://cloud.google.com/apis/design/resource_names of the form
                ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}``
            version (int): Optional. The version of workflow template to retrieve. Only previously
                instatiated versions can be retrieved.

                If unspecified, retrieves the current version.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~mrjob._vendor.dataproc_v1beta2.types.WorkflowTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if 'get_workflow_template' not in self._inner_api_calls:
            self._inner_api_calls[
                'get_workflow_template'] = google.api_core.gapic_v1.method.wrap_method(
                    self._workflow_template_service_stub.GetWorkflowTemplate,
                    default_retry=self._method_configs[
                        'GetWorkflowTemplate'].retry,
                    default_timeout=self._method_configs['GetWorkflowTemplate']
                    .timeout,
                    client_info=self._client_info,
                )

        request = workflow_templates_pb2.GetWorkflowTemplateRequest(
            name=name,
            version=version,
        )
        return self._inner_api_calls['get_workflow_template'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def instantiate_workflow_template(
            self,
            name,
            version=None,
            instance_id=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Instantiates a template and begins execution.

        The returned Operation can be used to track execution of
        workflow by polling
        ``operations.get``.
        The Operation will complete when entire workflow is finished.

        The running workflow can be aborted via
        ``operations.cancel``.
        This will cause any inflight jobs to be cancelled and workflow-owned
        clusters to be deleted.

        The ``Operation.metadata`` will be
        ``WorkflowMetadata``.

        On successful completion,
        ``Operation.response`` will be
        ``Empty``.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> name = client.workflow_template_path('[PROJECT]', '[REGION]', '[WORKFLOW_TEMPLATE]')
            >>>
            >>> response = client.instantiate_workflow_template(name)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            name (str): Required. The \"resource name\" of the workflow template, as described
                in https://cloud.google.com/apis/design/resource_names of the form
                ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}``
            version (int): Optional. The version of workflow template to instantiate. If specified,
                the workflow will be instantiated only if the current version of
                the workflow template has the supplied version.

                This option cannot be used to instantiate a previous version of
                workflow template.
            instance_id (str): Optional. A tag that prevents multiple concurrent workflow
                instances with the same tag from running. This mitigates risk of
                concurrent instances started due to retries.

                It is recommended to always set this value to a
                `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_.

                The tag must contain only letters (a-z, A-Z), numbers (0-9),
                underscores (_), and hyphens (-). The maximum length is 40 characters.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~mrjob._vendor.dataproc_v1beta2.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if 'instantiate_workflow_template' not in self._inner_api_calls:
            self._inner_api_calls[
                'instantiate_workflow_template'] = google.api_core.gapic_v1.method.wrap_method(
                    self._workflow_template_service_stub.
                    InstantiateWorkflowTemplate,
                    default_retry=self._method_configs[
                        'InstantiateWorkflowTemplate'].retry,
                    default_timeout=self._method_configs[
                        'InstantiateWorkflowTemplate'].timeout,
                    client_info=self._client_info,
                )

        request = workflow_templates_pb2.InstantiateWorkflowTemplateRequest(
            name=name,
            version=version,
            instance_id=instance_id,
        )
        operation = self._inner_api_calls['instantiate_workflow_template'](
            request, retry=retry, timeout=timeout, metadata=metadata)
        return google.api_core.operation.from_gapic(
            operation,
            self._operations_client,
            empty_pb2.Empty,
            metadata_type=workflow_templates_pb2.WorkflowMetadata,
        )

    def update_workflow_template(
            self,
            template,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Updates (replaces) workflow template. The updated template
        must contain version that matches the current server version.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> # TODO: Initialize ``template``:
            >>> template = {}
            >>>
            >>> response = client.update_workflow_template(template)

        Args:
            template (Union[dict, ~mrjob._vendor.dataproc_v1beta2.types.WorkflowTemplate]): Required. The updated workflow template.

                The ``template.version`` field must match the current version.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~mrjob._vendor.dataproc_v1beta2.types.WorkflowTemplate`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~mrjob._vendor.dataproc_v1beta2.types.WorkflowTemplate` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if 'update_workflow_template' not in self._inner_api_calls:
            self._inner_api_calls[
                'update_workflow_template'] = google.api_core.gapic_v1.method.wrap_method(
                    self._workflow_template_service_stub.
                    UpdateWorkflowTemplate,
                    default_retry=self._method_configs[
                        'UpdateWorkflowTemplate'].retry,
                    default_timeout=self._method_configs[
                        'UpdateWorkflowTemplate'].timeout,
                    client_info=self._client_info,
                )

        request = workflow_templates_pb2.UpdateWorkflowTemplateRequest(
            template=template, )
        return self._inner_api_calls['update_workflow_template'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def list_workflow_templates(
            self,
            parent,
            page_size=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Lists workflows that match the specified filter in the request.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> parent = client.region_path('[PROJECT]', '[REGION]')
            >>>
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_workflow_templates(parent):
            ...     # process element
            ...     pass
            >>>
            >>> # Or iterate over results one page at a time
            >>> for page in client.list_workflow_templates(parent, options=CallOptions(page_token=INITIAL_PAGE)):
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The \"resource name\" of the region, as described
                in https://cloud.google.com/apis/design/resource_names of the form
                ``projects/{project_id}/regions/{region}``
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.gax.PageIterator` instance. By default, this
            is an iterable of :class:`~mrjob._vendor.dataproc_v1beta2.types.WorkflowTemplate` instances.
            This object can also be configured to iterate over the pages
            of the response through the `options` parameter.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if 'list_workflow_templates' not in self._inner_api_calls:
            self._inner_api_calls[
                'list_workflow_templates'] = google.api_core.gapic_v1.method.wrap_method(
                    self._workflow_template_service_stub.ListWorkflowTemplates,
                    default_retry=self._method_configs['ListWorkflowTemplates']
                    .retry,
                    default_timeout=self._method_configs[
                        'ListWorkflowTemplates'].timeout,
                    client_info=self._client_info,
                )

        request = workflow_templates_pb2.ListWorkflowTemplatesRequest(
            parent=parent,
            page_size=page_size,
        )
        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls['list_workflow_templates'],
                retry=retry,
                timeout=timeout,
                metadata=metadata),
            request=request,
            items_field='templates',
            request_token_field='page_token',
            response_token_field='next_page_token',
        )
        return iterator

    def delete_workflow_template(
            self,
            name,
            version=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes a workflow template. It does not cancel in-progress workflows.

        Example:
            >>> from google.cloud import dataproc_v1beta2
            >>>
            >>> client = dataproc_v1beta2.WorkflowTemplateServiceClient()
            >>>
            >>> name = client.workflow_template_path('[PROJECT]', '[REGION]', '[WORKFLOW_TEMPLATE]')
            >>>
            >>> client.delete_workflow_template(name)

        Args:
            name (str): Required. The \"resource name\" of the workflow template, as described
                in https://cloud.google.com/apis/design/resource_names of the form
                ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}``
            version (int): Optional. The version of workflow template to delete. If specified,
                will only delete the template if the current server version matches
                specified version.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        if 'delete_workflow_template' not in self._inner_api_calls:
            self._inner_api_calls[
                'delete_workflow_template'] = google.api_core.gapic_v1.method.wrap_method(
                    self._workflow_template_service_stub.
                    DeleteWorkflowTemplate,
                    default_retry=self._method_configs[
                        'DeleteWorkflowTemplate'].retry,
                    default_timeout=self._method_configs[
                        'DeleteWorkflowTemplate'].timeout,
                    client_info=self._client_info,
                )

        request = workflow_templates_pb2.DeleteWorkflowTemplateRequest(
            name=name,
            version=version,
        )
        self._inner_api_calls['delete_workflow_template'](
            request, retry=retry, timeout=timeout, metadata=metadata)
