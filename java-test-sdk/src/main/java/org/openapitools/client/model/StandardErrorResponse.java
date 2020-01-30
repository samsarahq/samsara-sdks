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
 * Error response
 */
@ApiModel(description = "Error response")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-01-30T14:01:37.954-08:00[US/Pacific]")
public class StandardErrorResponse {
  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private String requestId;


  public StandardErrorResponse message(String message) {
    
    this.message = message;
    return this;
  }

   /**
   * The message of the error.
   * @return message
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "The message of the error.")

  public String getMessage() {
    return message;
  }


  public void setMessage(String message) {
    this.message = message;
  }


  public StandardErrorResponse requestId(String requestId) {
    
    this.requestId = requestId;
    return this;
  }

   /**
   * The ID of the request.
   * @return requestId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "The ID of the request.")

  public String getRequestId() {
    return requestId;
  }


  public void setRequestId(String requestId) {
    this.requestId = requestId;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StandardErrorResponse standardErrorResponse = (StandardErrorResponse) o;
    return Objects.equals(this.message, standardErrorResponse.message) &&
        Objects.equals(this.requestId, standardErrorResponse.requestId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(message, requestId);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StandardErrorResponse {\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
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

