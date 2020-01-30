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
 * Reverse geocoded information.
 */
@ApiModel(description = "Reverse geocoded information.")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-01-30T14:01:37.954-08:00[US/Pacific]")
public class VehicleLocationReverseGeo {
  public static final String SERIALIZED_NAME_FORMATTED_LOCATION = "formattedLocation";
  @SerializedName(SERIALIZED_NAME_FORMATTED_LOCATION)
  private String formattedLocation;


  public VehicleLocationReverseGeo formattedLocation(String formattedLocation) {
    
    this.formattedLocation = formattedLocation;
    return this;
  }

   /**
   * Formatted address of the reverse geocoding data.
   * @return formattedLocation
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(example = "16 N Fair Oaks Ave, Pasadena, CA 91103", value = "Formatted address of the reverse geocoding data.")

  public String getFormattedLocation() {
    return formattedLocation;
  }


  public void setFormattedLocation(String formattedLocation) {
    this.formattedLocation = formattedLocation;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VehicleLocationReverseGeo vehicleLocationReverseGeo = (VehicleLocationReverseGeo) o;
    return Objects.equals(this.formattedLocation, vehicleLocationReverseGeo.formattedLocation);
  }

  @Override
  public int hashCode() {
    return Objects.hash(formattedLocation);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VehicleLocationReverseGeo {\n");
    sb.append("    formattedLocation: ").append(toIndentedString(formattedLocation)).append("\n");
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

