# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from clients_engines import pathfinder_pb2 as pathfinder__pb2


class PathfinderStub(object):
  """Service that implements Techmo Sarmata Pathfinder API.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SpotPhrase = channel.unary_unary(
        '/techmo.speechanalytics.pathfinder.Pathfinder/SpotPhrase',
        request_serializer=pathfinder__pb2.SpotPhraseRequest.SerializeToString,
        response_deserializer=pathfinder__pb2.SpotPhraseResponse.FromString,
        )
    self.SpotPhraseStreaming = channel.stream_unary(
        '/techmo.speechanalytics.pathfinder.Pathfinder/SpotPhraseStreaming',
        request_serializer=pathfinder__pb2.SpotPhraseRequest.SerializeToString,
        response_deserializer=pathfinder__pb2.SpotPhraseResponse.FromString,
        )
    self.SpotPhraseBidirectionalStreaming = channel.stream_stream(
        '/techmo.speechanalytics.pathfinder.Pathfinder/SpotPhraseBidirectionalStreaming',
        request_serializer=pathfinder__pb2.SpotPhraseRequest.SerializeToString,
        response_deserializer=pathfinder__pb2.SpotPhraseResponse.FromString,
        )
    self.DeleteData = channel.unary_unary(
        '/techmo.speechanalytics.pathfinder.Pathfinder/DeleteData',
        request_serializer=pathfinder__pb2.DeleteDataRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class PathfinderServicer(object):
  """Service that implements Techmo Sarmata Pathfinder API.
  """

  def SpotPhrase(self, request, context):
    """Perform synchronous phrase spotting: receive results after all audio
    has been sent and processed.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SpotPhraseStreaming(self, request_iterator, context):
    """Perform partially asynchronous phrase spotting by sending the audio in chunks,
    allowing the Pathfinder to analyze the data between requests.
    Receive results after all audio has been sent and processed.
    You (the client) must close the stream in order to receive the results.
    The first request must contain configuration, and further requests must not contain configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SpotPhraseBidirectionalStreaming(self, request_iterator, context):
    """Perform asynchronous phrase spotting by sending the audio in chunks,
    allowing the Pathfinder to analyze the data between requests.
    Receive results each time Pathfinder automatically detects an end of utterance.
    The first request must contain configuration, and further requests must not contain configuration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteData(self, request, context):
    """Remove audio data (lattice) cache with given ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PathfinderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SpotPhrase': grpc.unary_unary_rpc_method_handler(
          servicer.SpotPhrase,
          request_deserializer=pathfinder__pb2.SpotPhraseRequest.FromString,
          response_serializer=pathfinder__pb2.SpotPhraseResponse.SerializeToString,
      ),
      'SpotPhraseStreaming': grpc.stream_unary_rpc_method_handler(
          servicer.SpotPhraseStreaming,
          request_deserializer=pathfinder__pb2.SpotPhraseRequest.FromString,
          response_serializer=pathfinder__pb2.SpotPhraseResponse.SerializeToString,
      ),
      'SpotPhraseBidirectionalStreaming': grpc.stream_stream_rpc_method_handler(
          servicer.SpotPhraseBidirectionalStreaming,
          request_deserializer=pathfinder__pb2.SpotPhraseRequest.FromString,
          response_serializer=pathfinder__pb2.SpotPhraseResponse.SerializeToString,
      ),
      'DeleteData': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteData,
          request_deserializer=pathfinder__pb2.DeleteDataRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'techmo.speechanalytics.pathfinder.Pathfinder', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
