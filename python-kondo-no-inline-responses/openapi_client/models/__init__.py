# coding: utf-8

# flake8: noqa
"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api-legacy).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api-legacy) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.models.address import Address
from openapi_client.models.address_all_of import AddressAllOf
from openapi_client.models.address_core import AddressCore
from openapi_client.models.address_create import AddressCreate
from openapi_client.models.address_create_all_of import AddressCreateAllOf
from openapi_client.models.address_geofence_request import AddressGeofenceRequest
from openapi_client.models.address_geofence_request_circle import AddressGeofenceRequestCircle
from openapi_client.models.address_geofence_request_polygon import AddressGeofenceRequestPolygon
from openapi_client.models.address_geofence_request_polygon_vertices import AddressGeofenceRequestPolygonVertices
from openapi_client.models.address_geofence_response import AddressGeofenceResponse
from openapi_client.models.address_geofence_response_circle import AddressGeofenceResponseCircle
from openapi_client.models.address_geofence_response_polygon import AddressGeofenceResponsePolygon
from openapi_client.models.address_patch import AddressPatch
from openapi_client.models.address_patch_all_of import AddressPatchAllOf
from openapi_client.models.address_request_core import AddressRequestCore
from openapi_client.models.address_request_core_all_of import AddressRequestCoreAllOf
from openapi_client.models.address_response_core import AddressResponseCore
from openapi_client.models.address_response_core_all_of import AddressResponseCoreAllOf
from openapi_client.models.contact import Contact
from openapi_client.models.contact_input import ContactInput
from openapi_client.models.contact_tiny_response import ContactTinyResponse
from openapi_client.models.create_address_response import CreateAddressResponse
from openapi_client.models.create_contact_response import CreateContactResponse
from openapi_client.models.create_driver_response import CreateDriverResponse
from openapi_client.models.create_tag_response import CreateTagResponse
from openapi_client.models.create_user_response import CreateUserResponse
from openapi_client.models.driver import Driver
from openapi_client.models.driver_all_of import DriverAllOf
from openapi_client.models.driver_base import DriverBase
from openapi_client.models.driver_base_carrier_settings import DriverBaseCarrierSettings
from openapi_client.models.driver_create import DriverCreate
from openapi_client.models.driver_tiny_response import DriverTinyResponse
from openapi_client.models.driver_update import DriverUpdate
from openapi_client.models.driver_update_all_of import DriverUpdateAllOf
from openapi_client.models.get_address_by_id_response import GetAddressByIdResponse
from openapi_client.models.get_addresses_response import GetAddressesResponse
from openapi_client.models.get_all_tags_response import GetAllTagsResponse
from openapi_client.models.get_contact_by_id_response import GetContactByIdResponse
from openapi_client.models.get_contacts_response import GetContactsResponse
from openapi_client.models.get_driver_by_id_response import GetDriverByIdResponse
from openapi_client.models.get_drivers_response import GetDriversResponse
from openapi_client.models.get_tag_by_id_response import GetTagByIdResponse
from openapi_client.models.get_user_by_id_response import GetUserByIdResponse
from openapi_client.models.get_user_roles_response import GetUserRolesResponse
from openapi_client.models.get_users_response import GetUsersResponse
from openapi_client.models.get_vehicle_by_id_response import GetVehicleByIdResponse
from openapi_client.models.get_vehicle_stats_snapshot_response import GetVehicleStatsSnapshotResponse
from openapi_client.models.inline_object import InlineObject
from openapi_client.models.inline_object1 import InlineObject1
from openapi_client.models.inline_object2 import InlineObject2
from openapi_client.models.inline_object3 import InlineObject3
from openapi_client.models.inline_object4 import InlineObject4
from openapi_client.models.inline_object5 import InlineObject5
from openapi_client.models.inline_object6 import InlineObject6
from openapi_client.models.inline_object7 import InlineObject7
from openapi_client.models.inline_object8 import InlineObject8
from openapi_client.models.inline_object9 import InlineObject9
from openapi_client.models.location import Location
from openapi_client.models.locations_wrapper import LocationsWrapper
from openapi_client.models.locations_wrapper_all_of import LocationsWrapperAllOf
from openapi_client.models.pagination_response import PaginationResponse
from openapi_client.models.parent_tag import ParentTag
from openapi_client.models.put_tag_by_id_response import PutTagByIdResponse
from openapi_client.models.remote_obd_test_records import RemoteObdTestRecords
from openapi_client.models.standard_error_response import StandardErrorResponse
from openapi_client.models.tag import Tag
from openapi_client.models.tag_all_of import TagAllOf
from openapi_client.models.tag_tiny_response import TagTinyResponse
from openapi_client.models.tag_update import TagUpdate
from openapi_client.models.tagged_object import TaggedObject
from openapi_client.models.tiny_tag import TinyTag
from openapi_client.models.update_address_by_id_response import UpdateAddressByIdResponse
from openapi_client.models.update_contact_by_id_response import UpdateContactByIdResponse
from openapi_client.models.update_driver_by_id_response import UpdateDriverByIdResponse
from openapi_client.models.update_user_by_id_response import UpdateUserByIdResponse
from openapi_client.models.update_vehicle_by_id_response import UpdateVehicleByIdResponse
from openapi_client.models.user import User
from openapi_client.models.user_create import UserCreate
from openapi_client.models.user_role import UserRole
from openapi_client.models.user_role_input import UserRoleInput
from openapi_client.models.user_role_response import UserRoleResponse
from openapi_client.models.user_role_tiny_response import UserRoleTinyResponse
from openapi_client.models.user_update import UserUpdate
from openapi_client.models.v1_asset import V1Asset
from openapi_client.models.v1_asset_cable import V1AssetCable
from openapi_client.models.v1_asset_current_location import V1AssetCurrentLocation
from openapi_client.models.v1_asset_current_locations_response import V1AssetCurrentLocationsResponse
from openapi_client.models.v1_asset_current_locations_response_cable import V1AssetCurrentLocationsResponseCable
from openapi_client.models.v1_asset_reefer_response import V1AssetReeferResponse
from openapi_client.models.v1_asset_reefer_response_reefer_stats import V1AssetReeferResponseReeferStats
from openapi_client.models.v1_asset_reefer_response_reefer_stats_alarms import V1AssetReeferResponseReeferStatsAlarms
from openapi_client.models.v1_asset_reefer_response_reefer_stats_alarms1 import V1AssetReeferResponseReeferStatsAlarms1
from openapi_client.models.v1_asset_reefer_response_reefer_stats_engine_hours import V1AssetReeferResponseReeferStatsEngineHours
from openapi_client.models.v1_asset_reefer_response_reefer_stats_fuel_percentage import V1AssetReeferResponseReeferStatsFuelPercentage
from openapi_client.models.v1_asset_reefer_response_reefer_stats_power_status import V1AssetReeferResponseReeferStatsPowerStatus
from openapi_client.models.v1_asset_reefer_response_reefer_stats_return_air_temp import V1AssetReeferResponseReeferStatsReturnAirTemp
from openapi_client.models.v1_asset_reefer_response_reefer_stats_set_point import V1AssetReeferResponseReeferStatsSetPoint
from openapi_client.models.v1_assets_reefer import V1AssetsReefer
from openapi_client.models.v1_assets_reefer_reefer_stats import V1AssetsReeferReeferStats
from openapi_client.models.v1_assets_reefer_reefer_stats_ambient_air_temperature import V1AssetsReeferReeferStatsAmbientAirTemperature
from openapi_client.models.v1_assets_reefer_reefer_stats_discharge_air_temperature import V1AssetsReeferReeferStatsDischargeAirTemperature
from openapi_client.models.v1_assets_reefer_reefer_stats_power_status import V1AssetsReeferReeferStatsPowerStatus
from openapi_client.models.v1_cargo_response import V1CargoResponse
from openapi_client.models.v1_cargo_response_sensors import V1CargoResponseSensors
from openapi_client.models.v1_data_input_history_response import V1DataInputHistoryResponse
from openapi_client.models.v1_data_input_history_response_points import V1DataInputHistoryResponsePoints
from openapi_client.models.v1_dispatch_job import V1DispatchJob
from openapi_client.models.v1_dispatch_job_all_of import V1DispatchJobAllOf
from openapi_client.models.v1_dispatch_job_create import V1DispatchJobCreate
from openapi_client.models.v1_dispatch_job_document_info import V1DispatchJobDocumentInfo
from openapi_client.models.v1_dispatch_job_update import V1DispatchJobUpdate
from openapi_client.models.v1_dispatch_job_update_all_of import V1DispatchJobUpdateAllOf
from openapi_client.models.v1_dispatch_job_without_eta import V1DispatchJobWithoutETA
from openapi_client.models.v1_dispatch_job_without_eta_all_of import V1DispatchJobWithoutETAAllOf
from openapi_client.models.v1_dispatch_route import V1DispatchRoute
from openapi_client.models.v1_dispatch_route_all_of import V1DispatchRouteAllOf
from openapi_client.models.v1_dispatch_route_base import V1DispatchRouteBase
from openapi_client.models.v1_dispatch_route_create import V1DispatchRouteCreate
from openapi_client.models.v1_dispatch_route_create_all_of import V1DispatchRouteCreateAllOf
from openapi_client.models.v1_dispatch_route_create_base import V1DispatchRouteCreateBase
from openapi_client.models.v1_dispatch_route_historical_entry import V1DispatchRouteHistoricalEntry
from openapi_client.models.v1_dispatch_route_history import V1DispatchRouteHistory
from openapi_client.models.v1_dispatch_route_update import V1DispatchRouteUpdate
from openapi_client.models.v1_dispatch_route_update_all_of import V1DispatchRouteUpdateAllOf
from openapi_client.models.v1_dispatch_route_update_base import V1DispatchRouteUpdateBase
from openapi_client.models.v1_dispatch_route_update_base_all_of import V1DispatchRouteUpdateBaseAllOf
from openapi_client.models.v1_dispatch_route_without_eta import V1DispatchRouteWithoutETA
from openapi_client.models.v1_dispatch_route_without_eta_all_of import V1DispatchRouteWithoutETAAllOf
from openapi_client.models.v1_document import V1Document
from openapi_client.models.v1_document_all_of import V1DocumentAllOf
from openapi_client.models.v1_document_base import V1DocumentBase
from openapi_client.models.v1_document_create import V1DocumentCreate
from openapi_client.models.v1_document_create_all_of import V1DocumentCreateAllOf
from openapi_client.models.v1_document_create_base import V1DocumentCreateBase
from openapi_client.models.v1_document_field import V1DocumentField
from openapi_client.models.v1_document_field_all_of import V1DocumentFieldAllOf
from openapi_client.models.v1_document_field_create import V1DocumentFieldCreate
from openapi_client.models.v1_document_field_create_multiple_choice_value import V1DocumentFieldCreateMultipleChoiceValue
from openapi_client.models.v1_document_field_create_photo_value import V1DocumentFieldCreatePhotoValue
from openapi_client.models.v1_document_field_type import V1DocumentFieldType
from openapi_client.models.v1_document_field_type_number_value_type_metadata import V1DocumentFieldTypeNumberValueTypeMetadata
from openapi_client.models.v1_document_type import V1DocumentType
from openapi_client.models.v1_door_response import V1DoorResponse
from openapi_client.models.v1_door_response_sensors import V1DoorResponseSensors
from openapi_client.models.v1_driver_daily_log_response import V1DriverDailyLogResponse
from openapi_client.models.v1_driver_daily_log_response_days import V1DriverDailyLogResponseDays
from openapi_client.models.v1_driver_safety_score_response import V1DriverSafetyScoreResponse
from openapi_client.models.v1_dvir_base import V1DvirBase
from openapi_client.models.v1_dvir_base_author_signature import V1DvirBaseAuthorSignature
from openapi_client.models.v1_dvir_base_mechanic_or_agent_signature import V1DvirBaseMechanicOrAgentSignature
from openapi_client.models.v1_dvir_base_next_driver_signature import V1DvirBaseNextDriverSignature
from openapi_client.models.v1_dvir_base_vehicle import V1DvirBaseVehicle
from openapi_client.models.v1_dvir_defect_base import V1DvirDefectBase
from openapi_client.models.v1_dvir_list_response import V1DvirListResponse
from openapi_client.models.v1_fleet_vehicle_location import V1FleetVehicleLocation
from openapi_client.models.v1_hos_authentication_logs_response import V1HosAuthenticationLogsResponse
from openapi_client.models.v1_hos_authentication_logs_response_authentication_logs import V1HosAuthenticationLogsResponseAuthenticationLogs
from openapi_client.models.v1_hos_logs_response import V1HosLogsResponse
from openapi_client.models.v1_hos_logs_response_logs import V1HosLogsResponseLogs
from openapi_client.models.v1_hos_logs_summary_response import V1HosLogsSummaryResponse
from openapi_client.models.v1_hos_logs_summary_response_drivers import V1HosLogsSummaryResponseDrivers
from openapi_client.models.v1_hos_logs_summary_response_pagination import V1HosLogsSummaryResponsePagination
from openapi_client.models.v1_humidity_response import V1HumidityResponse
from openapi_client.models.v1_humidity_response_sensors import V1HumidityResponseSensors
from openapi_client.models.v1_machine import V1Machine
from openapi_client.models.v1_machine_history_response import V1MachineHistoryResponse
from openapi_client.models.v1_machine_history_response_machines import V1MachineHistoryResponseMachines
from openapi_client.models.v1_machine_history_response_vibrations import V1MachineHistoryResponseVibrations
from openapi_client.models.v1_message import V1Message
from openapi_client.models.v1_message_response import V1MessageResponse
from openapi_client.models.v1_message_sender import V1MessageSender
from openapi_client.models.v1_pagination import V1Pagination
from openapi_client.models.v1_safety_report_harsh_event import V1SafetyReportHarshEvent
from openapi_client.models.v1_sensor import V1Sensor
from openapi_client.models.v1_sensor_history_response import V1SensorHistoryResponse
from openapi_client.models.v1_sensor_history_response_results import V1SensorHistoryResponseResults
from openapi_client.models.v1_sensors_history_series import V1SensorsHistorySeries
from openapi_client.models.v1_temperature_response import V1TemperatureResponse
from openapi_client.models.v1_temperature_response_sensors import V1TemperatureResponseSensors
from openapi_client.models.v1_trailer_assignment_response import V1TrailerAssignmentResponse
from openapi_client.models.v1_trailer_assignments_response import V1TrailerAssignmentsResponse
from openapi_client.models.v1_trailer_assignments_response_all_of import V1TrailerAssignmentsResponseAllOf
from openapi_client.models.v1_trailer_base import V1TrailerBase
from openapi_client.models.v1_trip_response import V1TripResponse
from openapi_client.models.v1_trip_response_end_address import V1TripResponseEndAddress
from openapi_client.models.v1_trip_response_end_coordinates import V1TripResponseEndCoordinates
from openapi_client.models.v1_trip_response_start_address import V1TripResponseStartAddress
from openapi_client.models.v1_trip_response_start_coordinates import V1TripResponseStartCoordinates
from openapi_client.models.v1_trip_response_trips import V1TripResponseTrips
from openapi_client.models.v1_vehicle_harsh_event_response import V1VehicleHarshEventResponse
from openapi_client.models.v1_vehicle_harsh_event_response_location import V1VehicleHarshEventResponseLocation
from openapi_client.models.v1_vehicle_location import V1VehicleLocation
from openapi_client.models.v1_vehicle_maintenance import V1VehicleMaintenance
from openapi_client.models.v1_vehicle_maintenance_j1939 import V1VehicleMaintenanceJ1939
from openapi_client.models.v1_vehicle_maintenance_j1939_check_engine_light import V1VehicleMaintenanceJ1939CheckEngineLight
from openapi_client.models.v1_vehicle_maintenance_j1939_diagnostic_trouble_codes import V1VehicleMaintenanceJ1939DiagnosticTroubleCodes
from openapi_client.models.v1_vehicle_maintenance_passenger import V1VehicleMaintenancePassenger
from openapi_client.models.v1_vehicle_maintenance_passenger_check_engine_light import V1VehicleMaintenancePassengerCheckEngineLight
from openapi_client.models.v1_vehicle_maintenance_passenger_diagnostic_trouble_codes import V1VehicleMaintenancePassengerDiagnosticTroubleCodes
from openapi_client.models.v1_vehicle_safety_score_response import V1VehicleSafetyScoreResponse
from openapi_client.models.v1_vision_run_by_camera_response import V1VisionRunByCameraResponse
from openapi_client.models.v1_vision_run_by_camera_response_inspection_results import V1VisionRunByCameraResponseInspectionResults
from openapi_client.models.v1_vision_run_by_camera_response_program import V1VisionRunByCameraResponseProgram
from openapi_client.models.v1_vision_run_by_camera_response_run_summary import V1VisionRunByCameraResponseRunSummary
from openapi_client.models.v1_vision_runs_by_camera_and_program_response import V1VisionRunsByCameraAndProgramResponse
from openapi_client.models.v1_vision_runs_response import V1VisionRunsResponse
from openapi_client.models.v1_vision_runs_response_report_metadata import V1VisionRunsResponseReportMetadata
from openapi_client.models.v1_vision_runs_response_vision_runs import V1VisionRunsResponseVisionRuns
from openapi_client.models.v1all_route_job_updates import V1allRouteJobUpdates
from openapi_client.models.v1create_messages_response import V1createMessagesResponse
from openapi_client.models.v1get_all_asset_current_locations_response import V1getAllAssetCurrentLocationsResponse
from openapi_client.models.v1get_all_assets_response import V1getAllAssetsResponse
from openapi_client.models.v1get_all_data_inputs_response import V1getAllDataInputsResponse
from openapi_client.models.v1get_all_trailer_assignments_response import V1getAllTrailerAssignmentsResponse
from openapi_client.models.v1get_assets_reefers_response import V1getAssetsReefersResponse
from openapi_client.models.v1get_fleet_maintenance_list_response import V1getFleetMaintenanceListResponse
from openapi_client.models.v1get_machines_response import V1getMachinesResponse
from openapi_client.models.v1get_messages_response import V1getMessagesResponse
from openapi_client.models.v1get_sensors_response import V1getSensorsResponse
from openapi_client.models.v1job_status import V1jobStatus
from openapi_client.models.v1job_update_object import V1jobUpdateObject
from openapi_client.models.v1prev_job_status import V1prevJobStatus
from openapi_client.models.vehicle_ctp_smog_test_data import VehicleCtpSmogTestData
from openapi_client.models.vehicle_ctp_smog_test_data_wrapper import VehicleCtpSmogTestDataWrapper
from openapi_client.models.vehicle_engine_state import VehicleEngineState
from openapi_client.models.vehicle_engine_states_wrapper import VehicleEngineStatesWrapper
from openapi_client.models.vehicle_fuel_percent import VehicleFuelPercent
from openapi_client.models.vehicle_fuel_percents_wrapper import VehicleFuelPercentsWrapper
from openapi_client.models.vehicle_gps_distance_meters import VehicleGpsDistanceMeters
from openapi_client.models.vehicle_gps_distance_meters_wrapper import VehicleGpsDistanceMetersWrapper
from openapi_client.models.vehicle_gps_odometer_meters import VehicleGpsOdometerMeters
from openapi_client.models.vehicle_gps_odometer_meters_wrapper import VehicleGpsOdometerMetersWrapper
from openapi_client.models.vehicle_list_response import VehicleListResponse
from openapi_client.models.vehicle_location import VehicleLocation
from openapi_client.models.vehicle_location_all_of import VehicleLocationAllOf
from openapi_client.models.vehicle_location_wrapper import VehicleLocationWrapper
from openapi_client.models.vehicle_location_wrapper_all_of import VehicleLocationWrapperAllOf
from openapi_client.models.vehicle_locations_list_response import VehicleLocationsListResponse
from openapi_client.models.vehicle_locations_snapshot_response import VehicleLocationsSnapshotResponse
from openapi_client.models.vehicle_locations_wrapper import VehicleLocationsWrapper
from openapi_client.models.vehicle_locations_wrapper_all_of import VehicleLocationsWrapperAllOf
from openapi_client.models.vehicle_obd_engine_seconds import VehicleObdEngineSeconds
from openapi_client.models.vehicle_obd_engine_seconds_wrapper import VehicleObdEngineSecondsWrapper
from openapi_client.models.vehicle_obd_odometer_meters import VehicleObdOdometerMeters
from openapi_client.models.vehicle_obd_odometer_meters_wrapper import VehicleObdOdometerMetersWrapper
from openapi_client.models.vehicle_patch import VehiclePatch
from openapi_client.models.vehicle_response import VehicleResponse
from openapi_client.models.vehicle_stats_list_response import VehicleStatsListResponse
from openapi_client.models.vehicle_stats_snapshot_response import VehicleStatsSnapshotResponse
from openapi_client.models.vehicle_stats_snapshot_response_all_of import VehicleStatsSnapshotResponseAllOf
from openapi_client.models.vehicle_tiny_response import VehicleTinyResponse
