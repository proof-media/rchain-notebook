from datetime import datetime
import functools
import secrets

from google.protobuf.empty_pb2 import Empty

from .generated import CasperMessage_pb2_grpc
from .generated.CasperMessage_pb2 import DeployData

from . import rho_types
from .exceptions import CasperException
from .utils import create_ch_builder


def throw_if_not_successful(response, name):
    if response.get('success') is not True:
        raise CasperException(f'Operation "{name}": not successfull', response)
    return response


build_ch = create_ch_builder(CasperMessage_pb2_grpc.DeployServiceStub)


def get_blocks(ch):
    output = ch.showBlocks(Empty())
    return [rho_types.to_dict(i) for i in output]


def deploy(ch, term, from_='0x0', phlo_limit=0, phlo_price=0, nonce=0):
    dt = datetime.now()
    timestamp = dt.microsecond
    deployData = rho_types.from_dict({
        'term': term,
        'from': from_,
        'phloLimit': phlo_limit,
        'phloPrice': phlo_price,
        'nonce': nonce,
        'timestamp': timestamp
    }, DeployData)

    output = ch.DoDeploy(deployData)
    return throw_if_not_successful(rho_types.to_dict(output), 'deploy')


def propose(ch):
    output = ch.createBlock(Empty())
    return throw_if_not_successful(rho_types.to_dict(output), 'propose')


def listen_on(ch, name):
    rchain_channel = rho_types.to_channel([name])
    output = ch.listenForDataAtName(rchain_channel)
    return rho_types.to_dict(output)


def run_and_listen_on(ch,
                      term,
                      output_placeholder='proof_output',
                      **deploy_kargs):
    """function deploy and propose given term and if in term is used channel
    `proof_output` (eg. `proof_output!("hello")`") will listen on replace this
    name with the internal channel and start listening on this. Name of this
    channel can be configured by `output_placeholder`. Rest of kargs will be
    passed to `deploy` function."""

    channel_name = f'rchain_grpc_{secrets.token_hex(5)}'
    preprocessed_term = term.replace(output_placeholder, f'@"{channel_name}"')
    deploy(ch, preprocessed_term, **deploy_kargs)
    propose(ch)
    return listen_on(ch, channel_name)
