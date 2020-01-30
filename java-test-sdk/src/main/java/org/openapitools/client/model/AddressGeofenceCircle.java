/*
 * Samsara API
 * Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.
 *
 * The version of the OpenAPI document: 2019-12-12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * Information about a circular geofence. This field is only needed if the geofence is a circle.
 */
@ApiModel(description = "Information about a circular geofence. This field is only needed if the geofence is a circle.")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-01-30T14:01:37.954-08:00[US/Pacific]")
public class AddressGeofenceCircle {
  public static final String SERIALIZED_NAME_LATITUDE = "latitude";
  @SerializedName(SERIALIZED_NAME_LATITUDE)
  private Double latitude;

  public static final String SERIALIZED_NAME_LONGITUDE = "longitude";
  @SerializedName(SERIALIZED_NAME_LONGITUDE)
  private Double longitude;

  public static final String SERIALIZED_NAME_RADIUS_METERS = "radiusMeters";
  @SerializedName(SERIALIZED_NAME_RADIUS_METERS)
  private Integer radiusMeters;


  public AddressGeofenceCircle latitude(Double latitude) {
    
    this.latitude = latitude;
    return this;
  }

   /**
   * Latitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided.
   * @return latitude
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "37.765363", value = "Latitude of the address. Will be geocoded from `formattedAddress` if not provided.")

  public Double getLatitude() {
    return latitude;
  }


  public void setLatitude(Double latitude) {
    this.latitude = latitude;
  }


  public AddressGeofenceCircle longitude(Double longitude) {
    
    this.longitude = longitude;
    return this;
  }

   /**
   * Longitude of the address. Will be geocoded from &#x60;formattedAddress&#x60; if not provided.
   * @return longitude
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "37.765363", value = "Longitude of the address. Will be geocoded from `formattedAddress` if not provided.")

  public Double getLongitude() {
    return longitude;
  }


  public void setLongitude(Double longitude) {
    this.longitude = longitude;
  }


  public AddressGeofenceCircle radiusMeters(Integer radiusMeters) {
    
    this.radiusMeters = radiusMeters;
    return this;
  }

   /**
   * The radius of the circular geofence in meters.
   * @return radiusMeters
  **/
  @ApiModelProperty(example = "250", required = true, value = "The radius of the circular geofence in meters.")

  public Integer getRadiusMeters() {
    return radiusMeters;
  }


  public void setRadiusMeters(Integer radiusMeters) {
    this.radiusMeters = radiusMeters;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddressGeofenceCircle addressGeofenceCircle = (AddressGeofenceCircle) o;
    return Objects.equals(this.latitude, addressGeofenceCircle.latitude) &&
        Objects.equals(this.longitude, addressGeofenceCircle.longitude) &&
        Objects.equals(this.radiusMeters, addressGeofenceCircle.radiusMeters);
  }

  @Override
  public int hashCode() {
    return Objects.hash(latitude, longitude, radiusMeters);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddressGeofenceCircle {\n");
    sb.append("    latitude: ").append(toIndentedString(latitude)).append("\n");
    sb.append("    longitude: ").append(toIndentedString(longitude)).append("\n");
    sb.append("    radiusMeters: ").append(toIndentedString(radiusMeters)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

