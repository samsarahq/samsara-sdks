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
import org.openapitools.client.model.VehicleLocation;

/**
 * A vehicle and its most recent location.
 */
@ApiModel(description = "A vehicle and its most recent location.")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-01-30T14:01:37.954-08:00[US/Pacific]")
public class VehicleLocationsResponseData {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private VehicleLocation location;


  public VehicleLocationsResponseData id(String id) {
    
    this.id = id;
    return this;
  }

   /**
   * ID of the vehicle.
   * @return id
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "123456789", value = "ID of the vehicle.")

  public String getId() {
    return id;
  }


  public void setId(String id) {
    this.id = id;
  }


  public VehicleLocationsResponseData name(String name) {
    
    this.name = name;
    return this;
  }

   /**
   * Name of the vehicle.
   * @return name
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "Midwest Truck #4", value = "Name of the vehicle.")

  public String getName() {
    return name;
  }


  public void setName(String name) {
    this.name = name;
  }


  public VehicleLocationsResponseData location(VehicleLocation location) {
    
    this.location = location;
    return this;
  }

   /**
   * Get location
   * @return location
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public VehicleLocation getLocation() {
    return location;
  }


  public void setLocation(VehicleLocation location) {
    this.location = location;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VehicleLocationsResponseData vehicleLocationsResponseData = (VehicleLocationsResponseData) o;
    return Objects.equals(this.id, vehicleLocationsResponseData.id) &&
        Objects.equals(this.name, vehicleLocationsResponseData.name) &&
        Objects.equals(this.location, vehicleLocationsResponseData.location);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, name, location);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VehicleLocationsResponseData {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
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

