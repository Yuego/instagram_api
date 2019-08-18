from .mapper import ApiResponse, ApiResponseInterface
from .mapper.types import Timestamp, AnyType

__all__ = ['CreateLiveResponse']


class CreateLiveResponseInterface(ApiResponseInterface):
    broadcast_id: int
    upload_url: str
    max_time_in_seconds: int
    speed_test_ui_timeout: int
    stream_network_speed_test_payload_chunk_size_in_bytes: int
    stream_network_speed_test_payload_size_in_bytes: int
    stream_network_speed_test_payload_timeout_in_seconds: int
    speed_test_minimum_bandwidth_threshold: int
    speed_test_retry_max_count: int
    speed_test_retry_time_delay: int
    disable_speed_test: int
    stream_video_allow_b_frames: int
    stream_video_width: int
    stream_video_bit_rate: int
    stream_video_fps: int
    stream_audio_bit_rate: int
    stream_audio_sample_rate: int
    stream_audio_channels: int
    heartbeat_interval: int
    broadcaster_update_frequency: int
    stream_video_adaptive_bitrate_config: AnyType
    stream_network_connection_retry_count: int
    stream_network_connection_retry_delay_in_seconds: int
    connect_with_1rtt: int
    avc_rtmp_payload: int
    allow_resolution_change: int


class CreateLiveResponse(ApiResponse, CreateLiveResponseInterface):
    pass
