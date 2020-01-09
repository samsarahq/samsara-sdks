# coding: utf-8

# flake8: noqa

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-11-19
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from samsara.api.addresses_api import AddressesApi
from samsara.api.contacts_api import ContactsApi
from samsara.api.documents_api import DocumentsApi
from samsara.api.drivers_api import DriversApi
from samsara.api.hours_of_service_api import HoursOfServiceApi
from samsara.api.industrial_api import IndustrialApi
from samsara.api.maintenance_api import MaintenanceApi
from samsara.api.messages_api import MessagesApi
from samsara.api.routes_api import RoutesApi
from samsara.api.safety_api import SafetyApi
from samsara.api.sensors_api import SensorsApi
from samsara.api.tags_api import TagsApi
from samsara.api.trips_api import TripsApi
from samsara.api.users_api import UsersApi
from samsara.api.vehicles_api import VehiclesApi

# import ApiClient
from samsara.api_client import ApiClient
from samsara.configuration import Configuration
from samsara.exceptions import OpenApiException
from samsara.exceptions import ApiTypeError
from samsara.exceptions import ApiValueError
from samsara.exceptions import ApiKeyError
from samsara.exceptions import ApiException
# import models into sdk package
from samsara.models.address import Address
from samsara.models.address_all_of import AddressAllOf
from samsara.models.address_all_of_contacts import AddressAllOfContacts
from samsara.models.address_all_of_tags import AddressAllOfTags
from samsara.models.address_core import AddressCore
from samsara.models.address_create import AddressCreate
from samsara.models.address_create_all_of import AddressCreateAllOf
from samsara.models.address_geofence_request import AddressGeofenceRequest
from samsara.models.address_geofence_request_circle import AddressGeofenceRequestCircle
from samsara.models.address_geofence_request_polygon import AddressGeofenceRequestPolygon
from samsara.models.address_geofence_request_polygon_vertices import AddressGeofenceRequestPolygonVertices
from samsara.models.address_geofence_response import AddressGeofenceResponse
from samsara.models.address_geofence_response_circle import AddressGeofenceResponseCircle
from samsara.models.address_geofence_response_polygon import AddressGeofenceResponsePolygon
from samsara.models.address_patch import AddressPatch
from samsara.models.address_patch_all_of import AddressPatchAllOf
from samsara.models.address_request_core import AddressRequestCore
from samsara.models.address_request_core_all_of import AddressRequestCoreAllOf
from samsara.models.address_request_core_all_of1 import AddressRequestCoreAllOf1
from samsara.models.address_request_core_all_of_geofence import AddressRequestCoreAllOfGeofence
from samsara.models.address_response_core import AddressResponseCore
from samsara.models.address_response_core_all_of import AddressResponseCoreAllOf
from samsara.models.address_response_core_all_of_geofence import AddressResponseCoreAllOfGeofence
from samsara.models.contact import Contact
from samsara.models.contact_input import ContactInput
from samsara.models.contact_tiny_response import ContactTinyResponse
from samsara.models.driver import Driver
from samsara.models.driver_all_of import DriverAllOf
from samsara.models.driver_all_of1 import DriverAllOf1
from samsara.models.driver_all_of1_carrier_settings import DriverAllOf1CarrierSettings
from samsara.models.driver_base import DriverBase
from samsara.models.driver_create import DriverCreate
from samsara.models.driver_tiny_response import DriverTinyResponse
from samsara.models.driver_update import DriverUpdate
from samsara.models.driver_update_all_of import DriverUpdateAllOf
from samsara.models.inline_object import InlineObject
from samsara.models.inline_object1 import InlineObject1
from samsara.models.inline_object10 import InlineObject10
from samsara.models.inline_object2 import InlineObject2
from samsara.models.inline_object3 import InlineObject3
from samsara.models.inline_object4 import InlineObject4
from samsara.models.inline_object5 import InlineObject5
from samsara.models.inline_object6 import InlineObject6
from samsara.models.inline_object7 import InlineObject7
from samsara.models.inline_object8 import InlineObject8
from samsara.models.inline_object9 import InlineObject9
from samsara.models.inline_response200 import InlineResponse200
from samsara.models.inline_response2001 import InlineResponse2001
from samsara.models.inline_response20010 import InlineResponse20010
from samsara.models.inline_response20011 import InlineResponse20011
from samsara.models.inline_response20012 import InlineResponse20012
from samsara.models.inline_response20013 import InlineResponse20013
from samsara.models.inline_response2002 import InlineResponse2002
from samsara.models.inline_response2003 import InlineResponse2003
from samsara.models.inline_response2004 import InlineResponse2004
from samsara.models.inline_response2005 import InlineResponse2005
from samsara.models.inline_response2006 import InlineResponse2006
from samsara.models.inline_response2007 import InlineResponse2007
from samsara.models.inline_response2008 import InlineResponse2008
from samsara.models.inline_response2009 import InlineResponse2009
from samsara.models.location import Location
from samsara.models.locations_wrapper import LocationsWrapper
from samsara.models.locations_wrapper_all_of import LocationsWrapperAllOf
from samsara.models.pagination_response import PaginationResponse
from samsara.models.parent_tag import ParentTag
from samsara.models.remote_obd_test_records import RemoteObdTestRecords
from samsara.models.standard_error_response import StandardErrorResponse
from samsara.models.tag import Tag
from samsara.models.tag_all_of import TagAllOf
from samsara.models.tag_all_of1 import TagAllOf1
from samsara.models.tag_all_of_addresses import TagAllOfAddresses
from samsara.models.tag_all_of_parent_tag import TagAllOfParentTag
from samsara.models.tag_tiny_response import TagTinyResponse
from samsara.models.tag_update import TagUpdate
from samsara.models.tagged_object import TaggedObject
from samsara.models.tiny_tag import TinyTag
from samsara.models.user import User
from samsara.models.user_create import UserCreate
from samsara.models.user_create_roles import UserCreateRoles
from samsara.models.user_role import UserRole
from samsara.models.user_role_input import UserRoleInput
from samsara.models.user_role_response import UserRoleResponse
from samsara.models.user_roles import UserRoles
from samsara.models.user_update import UserUpdate
from samsara.models.v1_cargo_response import V1CargoResponse
from samsara.models.v1_cargo_response_sensors import V1CargoResponseSensors
from samsara.models.v1_data_input_history_response import V1DataInputHistoryResponse
from samsara.models.v1_data_input_history_response_points import V1DataInputHistoryResponsePoints
from samsara.models.v1_dispatch_job import V1DispatchJob
from samsara.models.v1_dispatch_job_all_of import V1DispatchJobAllOf
from samsara.models.v1_dispatch_job_all_of1 import V1DispatchJobAllOf1
from samsara.models.v1_dispatch_job_all_of_documents import V1DispatchJobAllOfDocuments
from samsara.models.v1_dispatch_job_create import V1DispatchJobCreate
from samsara.models.v1_dispatch_job_document_info import V1DispatchJobDocumentInfo
from samsara.models.v1_dispatch_job_update import V1DispatchJobUpdate
from samsara.models.v1_dispatch_job_update_all_of import V1DispatchJobUpdateAllOf
from samsara.models.v1_dispatch_job_without_eta import V1DispatchJobWithoutETA
from samsara.models.v1_dispatch_job_without_eta_all_of import V1DispatchJobWithoutETAAllOf
from samsara.models.v1_dispatch_route import V1DispatchRoute
from samsara.models.v1_dispatch_route_all_of import V1DispatchRouteAllOf
from samsara.models.v1_dispatch_route_all_of1 import V1DispatchRouteAllOf1
from samsara.models.v1_dispatch_route_base import V1DispatchRouteBase
from samsara.models.v1_dispatch_route_create import V1DispatchRouteCreate
from samsara.models.v1_dispatch_route_create_all_of import V1DispatchRouteCreateAllOf
from samsara.models.v1_dispatch_route_create_all_of1 import V1DispatchRouteCreateAllOf1
from samsara.models.v1_dispatch_route_create_base import V1DispatchRouteCreateBase
from samsara.models.v1_dispatch_route_historical_entry import V1DispatchRouteHistoricalEntry
from samsara.models.v1_dispatch_route_history import V1DispatchRouteHistory
from samsara.models.v1_dispatch_route_history_history import V1DispatchRouteHistoryHistory
from samsara.models.v1_dispatch_route_update import V1DispatchRouteUpdate
from samsara.models.v1_dispatch_route_update_all_of import V1DispatchRouteUpdateAllOf
from samsara.models.v1_dispatch_route_update_base import V1DispatchRouteUpdateBase
from samsara.models.v1_dispatch_route_update_base_all_of import V1DispatchRouteUpdateBaseAllOf
from samsara.models.v1_dispatch_route_without_eta import V1DispatchRouteWithoutETA
from samsara.models.v1_dispatch_route_without_eta_all_of import V1DispatchRouteWithoutETAAllOf
from samsara.models.v1_document import V1Document
from samsara.models.v1_document_all_of import V1DocumentAllOf
from samsara.models.v1_document_all_of1 import V1DocumentAllOf1
from samsara.models.v1_document_base import V1DocumentBase
from samsara.models.v1_document_create import V1DocumentCreate
from samsara.models.v1_document_create_all_of import V1DocumentCreateAllOf
from samsara.models.v1_document_create_all_of1 import V1DocumentCreateAllOf1
from samsara.models.v1_document_create_base import V1DocumentCreateBase
from samsara.models.v1_document_field import V1DocumentField
from samsara.models.v1_document_field_all_of import V1DocumentFieldAllOf
from samsara.models.v1_document_field_all_of1 import V1DocumentFieldAllOf1
from samsara.models.v1_document_field_all_of1_multiple_choice_value import V1DocumentFieldAllOf1MultipleChoiceValue
from samsara.models.v1_document_field_all_of1_photo_value import V1DocumentFieldAllOf1PhotoValue
from samsara.models.v1_document_field_create import V1DocumentFieldCreate
from samsara.models.v1_document_field_type import V1DocumentFieldType
from samsara.models.v1_document_field_type_number_value_type_metadata import V1DocumentFieldTypeNumberValueTypeMetadata
from samsara.models.v1_document_type import V1DocumentType
from samsara.models.v1_document_type_field_types import V1DocumentTypeFieldTypes
from samsara.models.v1_door_response import V1DoorResponse
from samsara.models.v1_door_response_sensors import V1DoorResponseSensors
from samsara.models.v1_driver_daily_log_response import V1DriverDailyLogResponse
from samsara.models.v1_driver_daily_log_response_days import V1DriverDailyLogResponseDays
from samsara.models.v1_driver_safety_score_response import V1DriverSafetyScoreResponse
from samsara.models.v1_driver_safety_score_response_harsh_events import V1DriverSafetyScoreResponseHarshEvents
from samsara.models.v1_dvir_base import V1DvirBase
from samsara.models.v1_dvir_base_author_signature import V1DvirBaseAuthorSignature
from samsara.models.v1_dvir_base_mechanic_or_agent_signature import V1DvirBaseMechanicOrAgentSignature
from samsara.models.v1_dvir_base_next_driver_signature import V1DvirBaseNextDriverSignature
from samsara.models.v1_dvir_base_trailer_defects import V1DvirBaseTrailerDefects
from samsara.models.v1_dvir_base_vehicle import V1DvirBaseVehicle
from samsara.models.v1_dvir_defect_base import V1DvirDefectBase
from samsara.models.v1_dvir_list_response import V1DvirListResponse
from samsara.models.v1_dvir_list_response_dvirs import V1DvirListResponseDvirs
from samsara.models.v1_fleet_vehicle_location import V1FleetVehicleLocation
from samsara.models.v1_hos_authentication_logs_response import V1HosAuthenticationLogsResponse
from samsara.models.v1_hos_authentication_logs_response_authentication_logs import V1HosAuthenticationLogsResponseAuthenticationLogs
from samsara.models.v1_hos_logs_response import V1HosLogsResponse
from samsara.models.v1_hos_logs_response_logs import V1HosLogsResponseLogs
from samsara.models.v1_hos_logs_summary_response import V1HosLogsSummaryResponse
from samsara.models.v1_hos_logs_summary_response_drivers import V1HosLogsSummaryResponseDrivers
from samsara.models.v1_hos_logs_summary_response_pagination import V1HosLogsSummaryResponsePagination
from samsara.models.v1_humidity_response import V1HumidityResponse
from samsara.models.v1_humidity_response_sensors import V1HumidityResponseSensors
from samsara.models.v1_machine import V1Machine
from samsara.models.v1_machine_history_response import V1MachineHistoryResponse
from samsara.models.v1_machine_history_response_machines import V1MachineHistoryResponseMachines
from samsara.models.v1_machine_history_response_vibrations import V1MachineHistoryResponseVibrations
from samsara.models.v1_message import V1Message
from samsara.models.v1_message_response import V1MessageResponse
from samsara.models.v1_message_response_sender import V1MessageResponseSender
from samsara.models.v1_message_sender import V1MessageSender
from samsara.models.v1_safety_report_harsh_event import V1SafetyReportHarshEvent
from samsara.models.v1_sensor import V1Sensor
from samsara.models.v1_sensor_history_response import V1SensorHistoryResponse
from samsara.models.v1_sensor_history_response_results import V1SensorHistoryResponseResults
from samsara.models.v1_sensors_history_series import V1SensorsHistorySeries
from samsara.models.v1_temperature_response import V1TemperatureResponse
from samsara.models.v1_temperature_response_sensors import V1TemperatureResponseSensors
from samsara.models.v1_trip_response import V1TripResponse
from samsara.models.v1_trip_response_end_address import V1TripResponseEndAddress
from samsara.models.v1_trip_response_end_coordinates import V1TripResponseEndCoordinates
from samsara.models.v1_trip_response_start_address import V1TripResponseStartAddress
from samsara.models.v1_trip_response_start_coordinates import V1TripResponseStartCoordinates
from samsara.models.v1_trip_response_trips import V1TripResponseTrips
from samsara.models.v1_vehicle_harsh_event_response import V1VehicleHarshEventResponse
from samsara.models.v1_vehicle_harsh_event_response_location import V1VehicleHarshEventResponseLocation
from samsara.models.v1_vehicle_location import V1VehicleLocation
from samsara.models.v1_vehicle_maintenance import V1VehicleMaintenance
from samsara.models.v1_vehicle_maintenance_j1939 import V1VehicleMaintenanceJ1939
from samsara.models.v1_vehicle_maintenance_j1939_check_engine_light import V1VehicleMaintenanceJ1939CheckEngineLight
from samsara.models.v1_vehicle_maintenance_j1939_diagnostic_trouble_codes import V1VehicleMaintenanceJ1939DiagnosticTroubleCodes
from samsara.models.v1_vehicle_maintenance_passenger import V1VehicleMaintenancePassenger
from samsara.models.v1_vehicle_maintenance_passenger_check_engine_light import V1VehicleMaintenancePassengerCheckEngineLight
from samsara.models.v1_vehicle_maintenance_passenger_diagnostic_trouble_codes import V1VehicleMaintenancePassengerDiagnosticTroubleCodes
from samsara.models.v1_vehicle_safety_score_response import V1VehicleSafetyScoreResponse
from samsara.models.v1_vision_run_by_camera_response import V1VisionRunByCameraResponse
from samsara.models.v1_vision_run_by_camera_response_angle_check import V1VisionRunByCameraResponseAngleCheck
from samsara.models.v1_vision_run_by_camera_response_angle_check_angle_configured import V1VisionRunByCameraResponseAngleCheckAngleConfigured
from samsara.models.v1_vision_run_by_camera_response_barcode import V1VisionRunByCameraResponseBarcode
from samsara.models.v1_vision_run_by_camera_response_boolean_logic import V1VisionRunByCameraResponseBooleanLogic
from samsara.models.v1_vision_run_by_camera_response_boolean_logic_steps import V1VisionRunByCameraResponseBooleanLogicSteps
from samsara.models.v1_vision_run_by_camera_response_caliper import V1VisionRunByCameraResponseCaliper
from samsara.models.v1_vision_run_by_camera_response_caliper_angle_range import V1VisionRunByCameraResponseCaliperAngleRange
from samsara.models.v1_vision_run_by_camera_response_caliper_contrast_range import V1VisionRunByCameraResponseCaliperContrastRange
from samsara.models.v1_vision_run_by_camera_response_caliper_sharpness_range import V1VisionRunByCameraResponseCaliperSharpnessRange
from samsara.models.v1_vision_run_by_camera_response_caliper_straightness_range import V1VisionRunByCameraResponseCaliperStraightnessRange
from samsara.models.v1_vision_run_by_camera_response_contour import V1VisionRunByCameraResponseContour
from samsara.models.v1_vision_run_by_camera_response_distance import V1VisionRunByCameraResponseDistance
from samsara.models.v1_vision_run_by_camera_response_expiration_date import V1VisionRunByCameraResponseExpirationDate
from samsara.models.v1_vision_run_by_camera_response_find_copies import V1VisionRunByCameraResponseFindCopies
from samsara.models.v1_vision_run_by_camera_response_find_edge import V1VisionRunByCameraResponseFindEdge
from samsara.models.v1_vision_run_by_camera_response_find_shapes import V1VisionRunByCameraResponseFindShapes
from samsara.models.v1_vision_run_by_camera_response_fixture import V1VisionRunByCameraResponseFixture
from samsara.models.v1_vision_run_by_camera_response_fixture_coordinates import V1VisionRunByCameraResponseFixtureCoordinates
from samsara.models.v1_vision_run_by_camera_response_inspection_results import V1VisionRunByCameraResponseInspectionResults
from samsara.models.v1_vision_run_by_camera_response_label_match import V1VisionRunByCameraResponseLabelMatch
from samsara.models.v1_vision_run_by_camera_response_presence_absence import V1VisionRunByCameraResponsePresenceAbsence
from samsara.models.v1_vision_run_by_camera_response_presence_absence_blue_range import V1VisionRunByCameraResponsePresenceAbsenceBlueRange
from samsara.models.v1_vision_run_by_camera_response_presence_absence_grayscale_range import V1VisionRunByCameraResponsePresenceAbsenceGrayscaleRange
from samsara.models.v1_vision_run_by_camera_response_presence_absence_saturation_range import V1VisionRunByCameraResponsePresenceAbsenceSaturationRange
from samsara.models.v1_vision_run_by_camera_response_program import V1VisionRunByCameraResponseProgram
from samsara.models.v1_vision_run_by_camera_response_run_summary import V1VisionRunByCameraResponseRunSummary
from samsara.models.v1_vision_run_by_camera_response_step_results import V1VisionRunByCameraResponseStepResults
from samsara.models.v1_vision_run_by_camera_response_text_match import V1VisionRunByCameraResponseTextMatch
from samsara.models.v1_vision_runs_by_camera_and_program_response import V1VisionRunsByCameraAndProgramResponse
from samsara.models.v1_vision_runs_response import V1VisionRunsResponse
from samsara.models.v1_vision_runs_response_report_metadata import V1VisionRunsResponseReportMetadata
from samsara.models.v1_vision_runs_response_vision_runs import V1VisionRunsResponseVisionRuns
from samsara.models.v1all_route_job_updates import V1allRouteJobUpdates
from samsara.models.v1all_route_job_updates_job_updates import V1allRouteJobUpdatesJobUpdates
from samsara.models.v1job_status import V1jobStatus
from samsara.models.v1job_update_object import V1jobUpdateObject
from samsara.models.v1prev_job_status import V1prevJobStatus
from samsara.models.vehicle_ctp_smog_test_data import VehicleCtpSmogTestData
from samsara.models.vehicle_ctp_smog_test_data_remote_obd_test_records import VehicleCtpSmogTestDataRemoteObdTestRecords
from samsara.models.vehicle_ctp_smog_test_data_wrapper import VehicleCtpSmogTestDataWrapper
from samsara.models.vehicle_ctp_smog_test_data_wrapper_ctp_smog_test_data import VehicleCtpSmogTestDataWrapperCtpSmogTestData
from samsara.models.vehicle_engine_state import VehicleEngineState
from samsara.models.vehicle_engine_states_wrapper import VehicleEngineStatesWrapper
from samsara.models.vehicle_engine_states_wrapper_engine_states import VehicleEngineStatesWrapperEngineStates
from samsara.models.vehicle_fuel_percent import VehicleFuelPercent
from samsara.models.vehicle_fuel_percents_wrapper import VehicleFuelPercentsWrapper
from samsara.models.vehicle_fuel_percents_wrapper_fuel_percents import VehicleFuelPercentsWrapperFuelPercents
from samsara.models.vehicle_gps_odometer_meters import VehicleGpsOdometerMeters
from samsara.models.vehicle_gps_odometer_meters_wrapper import VehicleGpsOdometerMetersWrapper
from samsara.models.vehicle_gps_odometer_meters_wrapper_gps_odometer_meters import VehicleGpsOdometerMetersWrapperGpsOdometerMeters
from samsara.models.vehicle_list_response import VehicleListResponse
from samsara.models.vehicle_list_response_data import VehicleListResponseData
from samsara.models.vehicle_list_response_pagination import VehicleListResponsePagination
from samsara.models.vehicle_list_response_static_assigned_driver import VehicleListResponseStaticAssignedDriver
from samsara.models.vehicle_location import VehicleLocation
from samsara.models.vehicle_location_all_of import VehicleLocationAllOf
from samsara.models.vehicle_location_all_of1 import VehicleLocationAllOf1
from samsara.models.vehicle_location_wrapper import VehicleLocationWrapper
from samsara.models.vehicle_location_wrapper_all_of import VehicleLocationWrapperAllOf
from samsara.models.vehicle_location_wrapper_all_of1 import VehicleLocationWrapperAllOf1
from samsara.models.vehicle_location_wrapper_location import VehicleLocationWrapperLocation
from samsara.models.vehicle_locations_list_response import VehicleLocationsListResponse
from samsara.models.vehicle_locations_snapshot_response import VehicleLocationsSnapshotResponse
from samsara.models.vehicle_locations_wrapper import VehicleLocationsWrapper
from samsara.models.vehicle_locations_wrapper_all_of import VehicleLocationsWrapperAllOf
from samsara.models.vehicle_locations_wrapper_location import VehicleLocationsWrapperLocation
from samsara.models.vehicle_obd_engine_seconds import VehicleObdEngineSeconds
from samsara.models.vehicle_obd_engine_seconds_wrapper import VehicleObdEngineSecondsWrapper
from samsara.models.vehicle_obd_engine_seconds_wrapper_obd_engine_seconds import VehicleObdEngineSecondsWrapperObdEngineSeconds
from samsara.models.vehicle_obd_odometer_meters import VehicleObdOdometerMeters
from samsara.models.vehicle_obd_odometer_meters_wrapper import VehicleObdOdometerMetersWrapper
from samsara.models.vehicle_obd_odometer_meters_wrapper_obd_odometer_meters import VehicleObdOdometerMetersWrapperObdOdometerMeters
from samsara.models.vehicle_patch import VehiclePatch
from samsara.models.vehicle_response import VehicleResponse
from samsara.models.vehicle_stats_list_response import VehicleStatsListResponse
from samsara.models.vehicle_stats_snapshot_response import VehicleStatsSnapshotResponse
from samsara.models.vehicle_stats_snapshot_response_all_of import VehicleStatsSnapshotResponseAllOf
from samsara.models.vehicle_stats_snapshot_response_inner import VehicleStatsSnapshotResponseInner
from samsara.models.vehicle_tiny_response import VehicleTinyResponse

