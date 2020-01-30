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
import org.openapitools.client.model.AddressGeofencePolygonVertices;

/**
 * Information about a polygon geofence. This field is only needed if the geofence is a polygon.
 */
@ApiModel(description = "Information about a polygon geofence. This field is only needed if the geofence is a polygon.")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-01-30T14:01:37.954-08:00[US/Pacific]")
public class AddressGeofencePolygon {
  public static final String SERIALIZED_NAME_VERTICES = "vertices";
  @SerializedName(SERIALIZED_NAME_VERTICES)
  private List<AddressGeofencePolygonVertices> vertices = new ArrayList<AddressGeofencePolygonVertices>();


  public AddressGeofencePolygon vertices(List<AddressGeofencePolygonVertices> vertices) {
    
    this.vertices = vertices;
    return this;
  }

  public AddressGeofencePolygon addVerticesItem(AddressGeofencePolygonVertices verticesItem) {
    this.vertices.add(verticesItem);
    return this;
  }

   /**
   * The vertices of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40.
   * @return vertices
  **/
  @ApiModelProperty(example = "[{latitude=37.765363, longitude=-122.403098}, {latitude=38.765363, longitude=-122.403098}, {latitude=37.765363, longitude=-123.403098}]", required = true, value = "The vertices of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40.")

  public List<AddressGeofencePolygonVertices> getVertices() {
    return vertices;
  }


  public void setVertices(List<AddressGeofencePolygonVertices> vertices) {
    this.vertices = vertices;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AddressGeofencePolygon addressGeofencePolygon = (AddressGeofencePolygon) o;
    return Objects.equals(this.vertices, addressGeofencePolygon.vertices);
  }

  @Override
  public int hashCode() {
    return Objects.hash(vertices);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AddressGeofencePolygon {\n");
    sb.append("    vertices: ").append(toIndentedString(vertices)).append("\n");
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

