""" This module implements Messages sent out by the simulator-based drivers. """

import erdos
import carla

from pylot.utils import Vector3D, LaneMarking, LaneType


class CollisionMessage(erdos.Message):
    """ Message class to be used to send collision events.

    Args:
        collided_actor (:py:class:`carla.Actor`): The actor with which the
            ego-vehicle collided.
        impulse (:py:class:`pylot.utils.Vector3D`): The impulse as a result of
            the collision.
        timestamp (:py:class:`erdos.timestamp.Timestamp`): The timestamp of the
            message.

    Attributes:
        collided_actor (:py:class:`str`): The type of the actor with which the
            ego-vehicle collided.
        impulse (:py:class:`pyot.utils.Vector3D`): The impulse as a result of
            the collision.
        intensity (:py:class:`float`): The intensity of the collision.
    """

    def __init__(self, collided_actor, impulse, timestamp):
        super(CollisionMessage, self).__init__(timestamp, None)

        # Ensure the correct types of the arguments.
        if not isinstance(collided_actor, carla.Actor):
            raise ValueError(
                "The collided_actor should be of type carla.Actor")

        if not isinstance(impulse, Vector3D):
            raise ValueError(
                "The impulse should be of type pylot.utils.Vector3D")

        # Set the required attributes.
        self.collided_actor = collided_actor.type_id
        self.impulse = impulse
        self.intensity = self.impulse.magnitude()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'CollisionMessage(timestamp: {}, collided_actor: {}, ' \
            'impulse: {}, intensity: {})'.format(self.timestamp,
                                                self.collided_actor,
                                                self.impulse,
                                                self.intensity)


class LaneInvasionMessage(erdos.Message):
    """ Message class to be used to send lane-invasion events.

    Args:
        lane_markings (list(:py:class:`pylot.utils.LaneMarking`)): The lane
            markings that were invaded.
        lane_type (:py:class:`pylot.utils.LaneType`): The type of the lane
            that was invaded.
        timestamp: (:py:class:`erdos.timestamp.Timestamp`): The timestamp of
            the message.

    Attributes:
        lane_markings (list(:py:class:`pylot.utils.LaneMarking`)): The lane
            markings that were invaded.
        lane_type (:py:class:`pylot.utils.LaneType`): The type of the lane
            that was invaded.
        timestamp: (:py:class:`erdos.timestamp.Timestamp`): The timestamp of
            the message.
    """

    def __init__(self, lane_markings, lane_type, timestamp):
        super(LaneInvasionMessage, self).__init__(timestamp, None)

        # Ensure the correct types of the arguments.
        if not all(map(lambda a: isinstance(a, LaneMarking), lane_markings)):
            raise ValueError("Expected the lane_markings to be of type "
                             "pylot.utils.LaneMarking")
        if not isinstance(lane_type, LaneType):
            raise ValueError("Expected the lane_type to be of type "
                             "pylot.utils.LaneType")

        # Set the required attributes.
        self.lane_markings = lane_markings
        self.lane_type = lane_type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "LaneInvasionMessage(timestamp: {}, Lane Markings: {}, " \
                "Lane Type: {})".format(
            self.timestamp, self.lane_markings, self.lane_type)
