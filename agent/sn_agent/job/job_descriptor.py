#
# job_descriptor.py - implementation of abstract class defining API for service specs.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

from sn_agent.ontology import DOCUMENT_SUMMARIZER_ID, IMAGE_RECOGNIZER_ID, FACE_RECOGNIZER_ID, \
    TEXT_SUMMARIZER_ID, VIDEO_SUMMARIZER_ID
from sn_agent.ontology.service_descriptor import ServiceDescriptor

test_jobs = {}

class JobDescriptor(object):
    def __init__(self, service: ServiceDescriptor, job_parameters: dict):
        self.service = service
        self.job_parameters = job_parameters

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        if not self.service:
            description = ""
        else:
            description = self.service.name()
        return '<Job: service %s>' % (description)

    @classmethod
    def get_test_jobs(cls, service_id) -> []:
        return test_jobs[service_id]


def init_test_jobs():
    test_jobs[DOCUMENT_SUMMARIZER_ID] = []
    test_jobs[IMAGE_RECOGNIZER_ID] = []
    test_jobs[FACE_RECOGNIZER_ID] = []
    test_jobs[TEXT_SUMMARIZER_ID] = []
    test_jobs[VIDEO_SUMMARIZER_ID] = []

    job_parameters = {'input_type': 'file',
                        'input_url': 'http://test.com/inputs/test_input.txt',
                        'output_type': 'file_url_put',
                        'output_url': 'http://test.com/outputs/test_output.txt'}
    job_parameters_2 = {'input_type': 'file',
                        'input_url': 'http://test.com/inputs/test_input_2.txt',
                        'output_type': 'file_url_put',
                        'output_url': 'http://test.com/outputs/test_output_2.txt'}

    service_id = DOCUMENT_SUMMARIZER_ID
    job = JobDescriptor(ServiceDescriptor(service_id), job_parameters)
    test_jobs[service_id].append(job)
    job = JobDescriptor(ServiceDescriptor(service_id), job_parameters_2)
    test_jobs[service_id].append(job)

    service_id = IMAGE_RECOGNIZER_ID
    job = JobDescriptor(ServiceDescriptor(service_id), job_parameters)
    test_jobs[service_id].append(job)
    job = JobDescriptor(ServiceDescriptor(service_id), job_parameters_2)
    test_jobs[service_id].append(job)

    service_id = FACE_RECOGNIZER_ID
    job = JobDescriptor(ServiceDescriptor(service_id), job_parameters)
    test_jobs[service_id].append(job)

    service_id = TEXT_SUMMARIZER_ID
    job = JobDescriptor(ServiceDescriptor(service_id), job_parameters)
    test_jobs[service_id].append(job)

    service_id = VIDEO_SUMMARIZER_ID
    job = JobDescriptor(ServiceDescriptor(service_id), job_parameters)
    test_jobs[service_id].append(job)
