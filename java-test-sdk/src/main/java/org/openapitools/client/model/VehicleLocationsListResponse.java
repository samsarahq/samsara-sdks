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
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.PaginationResponse;
import org.openapitools.client.model.VehicleLocationsListResponseData;

/**
 * List of vehicle locations and pagination info.
 */
@ApiModel(description = "List of vehicle locations and pagination info.")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-01-30T14:01:37.954-08:00[US/Pacific]")
public class VehicleLocationsListResponse {
  public static final String SERIALIZED_NAME_DATA = "data";
  @SerializedName(SERIALIZED_NAME_DATA)
  private List<VehicleLocationsListResponseData> data = null;

  public static final String SERIALIZED_NAME_PAGINATION = "pagination";
  @SerializedName(SERIALIZED_NAME_PAGINATION)
  private PaginationResponse pagination;


  public VehicleLocationsListResponse data(List<VehicleLocationsListResponseData> data) {
    
    this.data = data;
    return this;
  }

  public VehicleLocationsListResponse addDataItem(VehicleLocationsListResponseData dataItem) {
    if (this.data == null) {
      this.data = new ArrayList<VehicleLocationsListResponseData>();
    }
    this.data.add(dataItem);
    return this;
  }

   /**
   * List of vehicle locations.
   * @return data
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "List of vehicle locations.")

  public List<VehicleLocationsListResponseData> getData() {
    return data;
  }


  public void setData(List<VehicleLocationsListResponseData> data) {
    this.data = data;
  }


  public VehicleLocationsListResponse pagination(PaginationResponse pagination) {
    
    this.pagination = pagination;
    return this;
  }

   /**
   * Get pagination
   * @return pagination
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public PaginationResponse getPagination() {
    return pagination;
  }


  public void setPagination(PaginationResponse pagination) {
    this.pagination = pagination;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VehicleLocationsListResponse vehicleLocationsListResponse = (VehicleLocationsListResponse) o;
    return Objects.equals(this.data, vehicleLocationsListResponse.data) &&
        Objects.equals(this.pagination, vehicleLocationsListResponse.pagination);
  }

  @Override
  public int hashCode() {
    return Objects.hash(data, pagination);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VehicleLocationsListResponse {\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
    sb.append("    pagination: ").append(toIndentedString(pagination)).append("\n");
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

